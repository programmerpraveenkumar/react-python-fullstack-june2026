from fastapi import FastAPI,HTTPException,Request
from fastapi.responses import JSONResponse

from sqlalchemy import select
from data import User
from model import UserRequest,Login
from db_connection import db
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import random
import logging
"""
logger should be added in first line of the method and last line before return the response
all excep should have logger.error() with proper message
all logger messge should be proper message to understand by everyone
logger is mainly for backend
"""
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# cors errr


# @asynccontextmanager
# async def simple_Scheduler(app=FastAPI):
#     schdeduler  = BackgroundScheduler()
#     schdeduler.add_job(
#         simple_print,"interval",seconds=10
#     )
#     schdeduler.start()

#     yield
#     #scheduler will run til app is shutdown

#     schdeduler.shutdown()

# app = FastAPI(lifespan=simple_Scheduler)
app = FastAPI()


def simple_print():
    today = datetime.today()
    print(today)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://127.0.0.1:3000'],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)

@app.middleware("http")
async def simple_middlware(request:Request,call_next):
    # for login  no token validation
    if "login" in str(request.url):
        response =  await call_next(request)
        logger.info(f"response is generated")
        return response
    token = request.headers.get("token")
    if token is None:
        logger.error("Unauthorized token is not valid becuase token is not valid")
        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "message": "Unauthorized token is not valid"
            }
        )
    # calling the endpoint with params
    response =  await call_next(request)
    logger.info(f"response is generated")
    return response


@app.get("/user")
def get_user():
    logger.info(f"request is come to the  get_user")
    # to get the records from the table using sqlalchemy
    result = db.execute(select(User))

    # to read all the records from the table
    rows = result.scalars().all()
    logger.info(f"request is completed to the  get_user")
    return rows

@app.post("/user")
def store_user(userReq:UserRequest):
    logger.info(f"request is come to the  store_user")
    user_db = User(
       id=userReq.id,
       name=userReq.name,
       email=userReq.email,
       mobile=userReq.mobile,
       password=userReq.password,
       dob=userReq.dob
    )
    logger.info(f"store_user data is ready to store") 
    db.add(user_db)
    db.commit()
    logger.info(f"store_user db process is completed") 
    return {"message":"user is added!!"}

@app.put("/user")
def update_user(userReq:UserRequest):
    """
    for update 1st steps is get the record with id
    assign the value to the column to be updated
    add and commit
    """
    user_db = db.execute(select(User).where(User.id==userReq.id)).scalar_one_or_none()
    # if user_db isempty  it will throw the exception
    if not user_db:
        raise HTTPException(status_code=500,detail='no user found')
    
    if userReq.name:
        user_db.name = userReq.name
    if userReq.email:
        user_db.email=userReq.email
    if userReq.mobile:
        user_db.mobile=userReq.mobile
    db.add(user_db)
    db.commit()
    return {"message":"user is updated!!"}

@app.delete("/user")
def delete_user(id:int):
    """
    for update 1st steps is get the record with id
    assign the value to the column to be updated
    delete and commit
    """
    user_db = db.execute(select(User).where(User.id==id)).scalar_one_or_none()
    # if user_db isempty  it will throw the exception
    if not user_db:
        raise HTTPException(status_code=500,detail='no user found')
    db.delete(user_db)
    db.commit()
    return {"message":"user is deleted!!"}

@app.post("/login")
def login(login:Login):
    user_db = db.execute(select(User).where(User.email==login.email,User.password==login.password)).scalar_one_or_none()
    if not user_db:
        raise HTTPException(status_code=400,detail="user not found")
    else:
        token = random.randint(10**9, (10**10) - 1)
        return {"token":token,"message":"Login success"}