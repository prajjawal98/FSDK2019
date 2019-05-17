
import sqlite3
from pandas import DataFrame


conn = sqlite3.connect ( 'employee.db' )


# creating cursor
c = conn.cursor()


c.execute ("""CREATE TABLE employees(
          name TEXT,
          age  INTEGER,
          roll INTEGER,
          branch TEXT
          )""")

c.execute("DROP TABLE employees")

c.execute("INSERT INTO employees VALUES ('Sylvester',21, 01, 'CSE')")
c.execute("INSERT INTO employees VALUES ('prajjawal',22, 02, 'IT')")
c.execute("INSERT INTO employees VALUES ('abhishek',20, 03, 'CSE')")
c.execute("INSERT INTO employees VALUES ('tarun',19, 04, 'IT')")
c.execute("INSERT INTO employees VALUES ('yash',16, 05, 'MECH')")
c.execute("INSERT INTO employees VALUES ('mukul',23, 06, 'CSE')")
c.execute("INSERT INTO employees VALUES ('utkarsh',10, 07, 'ECE')")

c.execute("SELECT * FROM employees")



print ( c.fetchall() )

c.execute("SELECT * FROM employees")



df = DataFrame(c.fetchall())  
df.columns = ["name","age","roll","branch"]



conn.commit()


conn.close()

#..............................................



import pymongo





client = pymongo.MongoClient("mongodb://prajjawal97:Prajjawal%40123@cluster0-shard-00-00-mv6ef.mongodb.net:27017,cluster0-shard-00-01-mv6ef.mongodb.net:27017,cluster0-shard-00-02-mv6ef.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")


mydb = client.prajjawal_db

def add_employee(name, age, roll, branch):
   
    mydb.prajjawal_coll.insert_one(
            {
            "name" :name,
            "age" : age,
            "roll" : roll,
            "branch" : branch
            })
    return "Employee added successfully"


def fetch_all_employee():
    user = mydb.prajjawal_coll.find()
    for i in user:
        print (i)




add_employee('prajjawal',21, 11, 'CSE')
add_employee('abhishek',20, 12, 'IT')
add_employee('utkarsh',29, 13, 'CSE')
add_employee('tarun',29, 14, 'IT')
add_employee('mukul',11, 15, 'ECE')
add_employee('yash',22, 16, 'MECH')



fetch_all_employee()


#............................................

from bs4 import BeautifulSoup
import requests




wiki = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(wiki).text
#or
#source = urllib.request.urlopen(wiki)

soup = BeautifulSoup(source,"lxml")

print (soup.prettify())



right_table=soup.find('table', class_='table')

print (right_table)


#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
tb=right_table.find('tbody')


for row in tb.findAll('tr'):
    cells = row.findAll('td')
 
   
    A.append(cells[0].text.strip())
    B.append(cells[1].text.strip())
    C.append(cells[2].text.strip())
    D.append(cells[3].text.strip())
    E.append(cells[4].text.strip())
   
import pandas as pd
from collections import OrderedDict

col_name = ["pos","Team","weighted match","points","ratings"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))
df = pd.DataFrame(col_data) 
df.to_csv("Data_file.csv")




import sqlite3
from pandas import DataFrame


conn = sqlite3.connect ( 'cricket.db' )


# creating cursor
c = conn.cursor()


c.execute ("""CREATE TABLE teams(
          pos INTEGER,
          team  TEXT,
          weighted match INTEGER,
          ponits INTEGER,
          ratings INTEGER
          )""")

c.execute("DROP TABLE teams")

for i in range(0,11):
    c.execute("INSERT INTO teams VALUES('{}','{}','{}','{}','{}')".format(A[i],B[i],C[i],D[i],E[i]))


c.execute("SELECT * FROM teams")
# STEP 6
df1 = DataFrame(c.fetchall())  # putting the result into Dataframe
df1.columns = ["pos","team_name","weighted match","points","rating"]
conn.commit()

# STEP 7
# closing the connection 
conn.close()




    
    
    









