from pydantic import BaseModel, Field
from typing import List, Optional

class FinancialStatement(BaseModel):
    company_name: str
    fiscal_year: int
    current_assets: float = Field(..., description="Ativo Circulante")
    current_liabilities: float = Field(..., description="Passivo Circulante")
    total_revenue: float = Field(..., description="Receita Líquida")
    net_income: float = Field(..., description="Lucro Líquido")
    notes: Optional[str] = Field(None, description="Notas explicativas")

class AuditResponse(BaseModel):
    risk_score: str
    liquidity_ratio: float
    net_margin: float
    red_flags: List[str]
    ai_executive_summary: str