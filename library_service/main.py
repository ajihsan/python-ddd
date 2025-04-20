from domains.book.api import router as router_book
from domains.loan.api import router as router_loan
from domains.member.api import router as router_member
from fastapi import FastAPI

app = FastAPI()

app.include_router(router_book)
app.include_router(router_member)
app.include_router(router_loan)
