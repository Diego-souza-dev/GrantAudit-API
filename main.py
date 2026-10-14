from fastapi import FastAPI, HTTPException
from schemas import FinancialStatement, AuditResponse
from services import AuditService

app = FastAPI(

    title="GrantAudit API", 

    version="1.0.0", 

    description="API para automação de pré-auditoria financeira utilizando IA"

)

audit_service = AuditService()

@app.post("/api/v1/audit/analyze", response_model=AuditResponse)

async def analyze_financials(data: FinancialStatement):

    try:

        response = audit_service.process_audit(data)

        return response

    except Exception as e:

        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/audit/health")

async def health_check():

    return {"status": "healthy", "version": "1.0.0"}
