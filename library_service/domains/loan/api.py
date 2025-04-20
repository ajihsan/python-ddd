from fastapi import APIRouter
from model import Loan
from repository import LoanRepository

router = APIRouter(prefix="/loan", tags=["Loan"])


@router.post("/")
def create_loan(loan: Loan):
    return LoanRepository.add(loan)
