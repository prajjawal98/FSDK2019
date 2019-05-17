
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