from fastapi import FastAPI,Query
from enum import Enum
from pydantic import BaseModel
from datetime import datetime

class status_choose(str,Enum):
    Available="available"
    Booked="booked"
    

class seat_list(BaseModel):
    seat_no:str
    status:status_choose

class req_body(BaseModel):
    title:str
    genre:str or None=None
    current_date:datetime
    seats:list[seat_list] or None=None
    duration:int or None=Query(default=120,gt=100)

class resp_body(req_body):
    id:str
    Days_after_release:int
    release_date:datetime


"basemodel for customer booking"

class pay(str,Enum):
    Online="UPI"
    NetCash="Cash"

class cust_req(BaseModel):
    seat_no:str
    name:str or None=None
    email:str=Query(min_length=3,example="example@gmail.com",max_length=30,regex=r"^[a-zA-Z0-9\.+_]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",default="example@gmail.com")

    payment_method:pay
    price:int or None=Query(default=100,gt=50)

class status_pay_choose(str,Enum):
    Booked="booked"
    Confirmed="confirmed"

class cust_resp(cust_req):
    id:str
    payment_status:status_pay_choose

"basemodel for patch customer booking"

class patch_req(BaseModel):
    seat_no:str
    name:str or None=None
    email:str=Query(default = "example@gmail.com",min_length=3,max_length=30,regex=r"^[a-zA-Z0-9\.+_]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
                    )
    payment_method: pay or None
    price:int or None=Query(default=100,gt=50)

class patch_resp(patch_req):
    id:str
    payment_status:status_pay_choose


"basemodel for book api"

class book_req(BaseModel):
    isbn:int or None=None
    title:str or None=None
    author:str
    publication_year:datetime or None=None
