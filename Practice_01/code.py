#pip install mysql-connector-python
import mysql.connector
import os
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python_db"
)
mycursor = mydb.cursor()
base_folder = "raw_file/"
file_list = os.listdir(base_folder)
sql = "INSERT INTO store_data (line1,line2,line3,file_name) VALUES(%s,%s,%s,%s)"
count = 0 
for a_file in file_list :
    file_name , file_ext = os.path.splitext(a_file)
    if file_ext == '.1' :
       file_data = open(base_folder+file_name+file_ext,"r")
       file_lines = file_data.readlines(); 
       row_insert = (file_lines[0],file_lines[1],file_lines[2],file_name)
       mycursor.execute(sql,row_insert)
       mydb.commit()
       count = count + 1
       print(count,file_name)

       
