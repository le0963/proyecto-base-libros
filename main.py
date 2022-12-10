from fastapi import FastAPI
from routes.user import user
from routes.book import book

from fastapi.middleware.cors import CORSMiddleware

import secrets
from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials


app = FastAPI(
  title="Mongodb Fastapi",
  description="Simple REstAPI for create users and books with CRUD",
  version="0.0.1",
)

app.add_middleware(
     CORSMiddleware,
     allow_origins=["*"],
     allow_credentials=True,
     allow_methods=["*"],
    allow_headers=["*"],
 )

security = HTTPBasic()

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = b"stanleyjobson"
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = b"swordfish"
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.get("/me")
def read_current_user(username: str = Depends(get_current_username)):
    return {"username": username}



app.include_router(user) 
app.include_router(book) 
