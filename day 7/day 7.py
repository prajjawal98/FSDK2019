import json
json_student = """
{
    "student":[ {
        "name": "prajjawal kansal",
        "age": 21,
        "dob":"18-08-1998"
        },
       {
        "name": "abhishek garg",
        "age": 20,
        "dob":"25-08-1998"
        }]
    }"""
json_faculty="""
{  
        
    "faculty":[{
        "name":"utkarsh sharma",
        "photo":null,
        " Department" :"CSE",
        " Research Area":["ML","DSA"],
        " Contact Details":[{
                "mobile":9836536272,
                "email":"utkarshsharm.gmail.com"
          }
      ]
     },
    {"name":"yash gupta",
        "photo":null,
        " Department" :"IT",
        " Research Area":["PYTHON","CN"],
        " Contact Details":[{
                "mobile":9836536363,
                "email":"yashgupta.gmail.com"
          }]
        }]
        }"""
file1=json.dumps(json_student)
file2=json.dumps(json_faculty)
with open("student.json", "w") as file1:
    json.dump(json_student, file1)
with open("faculty.json", "w") as file2:
    json.dump(json_faculty, file2)
    

#......................................................



import json
import requests
entry=input("enter the city")
url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q="+entry
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
print (url)
response = requests.get(url)
response.text
response1=response.json()
print(response1)

print("Latitude ",response1["coord"]["lat"])
print("Longitude ",response1["coord"]["lon"])
print("Weather Condition",response1["weather"][0]["description"])
print(" Wind Speed",response1["wind"]["speed"])
print("Sunset Rise",response1["sys"]["sunrise"])
print("Set timing",response1["sys"]["sunset"])



#....................................



import requests
usd=int(input("Enter value in USD"))
url1 = "https://free.currconv.com/api/v7/convert?q=USD_inr&compact=ultra&apiKey=2ee2f951a44b84041f17"
response = requests.get(url1)
print(response.content)
jsondata = response.json()
print(jsondata["USD_INR"]*usd)


    
        
        
    
    
        
        
    

