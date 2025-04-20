from fastapi import APIRouter
from model import Member
from repository import MemberRepository

router = APIRouter(prefix="/book", tags=["Book"])


@router.post("/")
def create_member(member: Member):
    return MemberRepository.add(member)
