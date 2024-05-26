from passlib.context import CryptContext
from pydantic import BaseModel

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserInDB(BaseModel):
    username: str
    email: str
    hashed_password: str


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


fake_users_db = {
    "sunflower": UserInDB(
        username="dennis",
        email="dennis@example.com",
        hashed_password=get_password_hash("0912"),
    ),
    "eustoma": UserInDB(
        username="nikky",
        email="nikky@example.com",
        hashed_password=get_password_hash("1209"),
    ),
}
