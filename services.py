import os
import google.generativeai as genai
from dotenv import load_dotenv
from schemas import FinancialStatement, AuditResponse

# Carrega as variáveis do arquivo .env
load_dotenv()

# A chave agora é lida do seu arquivo .env com segurança
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class AuditService:

    def __init__(self):


        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def _calculate_liquidity(self, data: FinancialStatement) -> float:

        if data.current_liabilities == 0:

            return 0.0

        return data.current_assets / data.current_liabilities

    def _calculate_margin(self, data: FinancialStatement) -> float:

        if data.total_revenue == 0:

            return 0.0

        return (data.net_income / data.total_revenue) * 100

    def _identify_red_flags(self, liquidity: float, margin: float) -> list[str]:

        flags = []

        if liquidity < 1.0:

            flags.append(f"ALERTA: Liquidez Corrente baixa ({liquidity:.2f}). A empresa pode ter dificuldades com dívidas de curto prazo.")

        if margin < 0:

            flags.append(f"ALERTA: Margem Líquida negativa ({margin:.2f}%). Operação gerando prejuízo no período.")

        return flags

    def _determine_risk_score(self, flags: list[str]) -> str:

        if len(flags) == 0:

            return "BAIXO"

        elif len(flags) == 1:

            return "MÉDIO"

        else:

            return "ALTO"

    def _generate_ai_summary(self, data: FinancialStatement, liquidity: float, margin: float) -> str:

        prompt = f'''

        Você é um auditor sênior da Grant Thornton. Analise os seguintes dados financeiros e gere um parecer executivo sintético de até 3 parágrafos.

        

        Empresa: {data.company_name} ({data.fiscal_year})

        Receita Líquida: R$ {data.total_revenue}

        Lucro Líquido: R$ {data.net_income}

        Índice de Liquidez Corrente: {liquidity:.2f}

        Margem Líquida: {margin:.2f}%

        Notas Explicativas: {data.notes or "Nenhuma"}

        O parecer deve focar em:

        1. Avaliação da saúde financeira e capacidade de pagamento a curto prazo.

        2. Identificação de potenciais anomalias ou riscos contábeis.

        3. Recomendações práticas de pontos focais para a equipe de auditoria em campo.

        '''

        response = self.model.generate_content(prompt)

        return response.text

    def process_audit(self, data: FinancialStatement) -> AuditResponse:

        # 1. Cálculos de negócio

        liquidity = self._calculate_liquidity(data)

        margin = self._calculate_margin(data)

        

        # 2. Regras baseadas em lógica padrão

        flags = self._identify_red_flags(liquidity, margin)

        risk = self._determine_risk_score(flags)

        

        # 3. Análise qualitativa com IA

        summary = self._generate_ai_summary(data, liquidity, margin)

        

        return AuditResponse(

            risk_score=risk,

            liquidity_ratio=liquidity,

            net_margin=margin,

            red_flags=flags,

            ai_executive_summary=summary

        )
