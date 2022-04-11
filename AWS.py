import pandas as pd
import pymysql
from sqlalchemy import create_engine

#Sample code, information is found elsewhere
host=’deneme.cykgvlpxbgsw.us-east-2.rds.amazonaws.com’
port=int(3306)
user=”cvadmin”
passw=”yourpassw”
database=”deneme”

mydb = create_engine(‘mysql+pymysql://’ + user + ‘:’ + passw + ‘@’ + host + ‘:’ + str(port) + ‘/’ + database , echo=False)