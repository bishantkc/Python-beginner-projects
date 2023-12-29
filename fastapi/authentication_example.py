from fastapi import FastAPI, Depends, HTTPException, status
from datetime import datetime, timedelta
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine, Column, Integer, String, Sequence, Boolean
from sqlalchemy.ext.declarative import declarative_base


app = FastAPI()

# Loads environment variables from .env file
load_dotenv()

# Constants
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = (os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
DATABASE_URL = os.getenv('DATABASE_URL')

'''
(Used this data for checking/sample)
SECRET_KEY = "1K1H314HKJ"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15
DATABASE_URL = "sqlite:///mydb.db"
'''

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String(100), unique=True)
    full_name = Column(String(100))
    hashed_password = Column(String)
    disabled = Column(Boolean, default=True) # to know user active or inactive

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class UserDB(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    hashed_password: str
    disabled: bool | None = None

class UserResponce(BaseModel):
    id: int
    username: str
    email: str
    full_name: str
    disabled: bool

DATABASE_URL = os.getenv('DATABASE_URL')

# SQLAlchemy setup
engine = create_engine("sqlite:///mydb.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

# Password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 setup
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Dependency to get the current database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Hashing passwords
def hash_password(password):
    return pwd_context.hash(password)

# Verify passwords
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Get user from database by username
def get_user(username: str, db: Session = Depends(get_db)):
    return db.query(User).filter(User.username == username).first()
    # if user exist it returns user otherwise None

# Authenticate user
def authenticate_user(username: str, password: str, db : Session = Depends(get_db)):
    user = get_user(username, db)

    if user and verify_password(password, user.hashed_password):
        return user
    else:
        return None

# Create access token
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Get current user from the token
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={'WWW-Authenticate': "Bearer"},
    )

    try: 
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = get_user(username=token_data.username, db=db)
    if user is None:
        raise credentials_exception
    return user 

async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Register endpoint
@app.post("/register/")
def register(username: str, password: str, email: str, full_name: str, db: Session = Depends(get_db)):
    hashed_password = hash_password(password)

    existing_user = db.query(User).filter(User.username == username).first()
    if existing_user:
        raise HTTPException(status_code=409, detail=f"User {username} already exists")

    new_user_data = {"username": username, "hashed_password": hashed_password,
                     "full_name": full_name, "email": email, "disabled": False}
    user_create = UserDB(**new_user_data)
    new_user = User(**user_create.dict())
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return {"Username": new_user.username} 

# Login endpoint
@app.post("/login/")
def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Aunthenticate": "Bearer"}
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


# Demo function to get user's email securely
@app.get("/users_email/")
async def get_users_email(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user.email

# Demo function to define a way of getting info about a user securely
@app.get("/user")
async def get_user_details(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user