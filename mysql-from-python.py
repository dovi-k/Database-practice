import os
import pymysql

username = os.getenv("C9_USER")

connection = pymysql.connect(host="localhost", 
user=username, password="", db="Chin")
