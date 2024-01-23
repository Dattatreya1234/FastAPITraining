import logging
from datetime import datetime,date,timedelta

def info_log():
    x=datetime.now()
    a=str(x.strftime("%c")).replace(" ","_")[0:13]
    logging.basicConfig(level=logging.INFO, filename=f"C:/Users/DPatil/Backend/log_info/{a}.log",
                        format="%(asctime)s %(levelname)s %(message)s",filemode="a")
    logging.info("--->add_details(mv:req_body) posted successfully")

def error_log():
    y=datetime.now()
    b=str(y.strftime("%c")).replace(" ","_")[0:13]
    logging.basicConfig(level=logging.ERROR, filename=f"C:/Users/DPatil/Backend/log_error/{b}.log",
                        format="%(asctime)s %(levelname)s %(message)s",filemode="a")
    logging.error("--->add_details(mv:req_body) required fields are not given")

    