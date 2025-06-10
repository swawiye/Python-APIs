import requests

import csv

url = "https://jsonplaceholder.typicode.com/users"

# send a "GET" request
response = requests.get(url)

newuser = {'id':'11', 'name':'Darcy Wendlow','username':'DWendlow', 'email':'dwendlow@gmail.com'}

# Check if the request was successful
if response.status_code == 200:
    users = response.json() #parse to json format

    post = requests.post(url, json=newuser) # adding a new user
    
    print(f"Fetched {len(users)} users")
    for user in users[:4]:
        print(user)
    with open("users.csv", "w") as file: # newline='' - prevent blanks in the csv
        writer = csv.writer(file)
        # write header rows
        writer.writerow(["Id", "Name", "Username", "Email"])
        # write the rows
        for user in users:
            writer.writerow([user["id"], user["name"], user["username"], user["email"]])

        writer.writerow([newuser["id"], newuser["name"], newuser["username"], newuser["email"]])
    print("Data stored in csv")
else:
    print(f"Error: {response.status_code}")

# POST request
# Syntax: requests.post(url, data={key: value}, json={key: value}, args)

print(post) # check status code for response received
print(post.json()) #print the content