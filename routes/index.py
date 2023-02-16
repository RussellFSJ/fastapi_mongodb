from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["root"])
def read_root():
    return "Welcome to FastAPI MongoDB Server!"
