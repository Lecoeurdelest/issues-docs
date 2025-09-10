from fastapi import APIRouter

router = APIRouter()

@router.get("/answers/{answer_id}")
def get_answer(answer_id: int):
    return {"answer_id": answer_id, "content": "This is a sample answer."}