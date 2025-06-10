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
        #writer.writerow([updated_data["id"], updated_data["name"], updated_data["username"], newuser["email"]])
    print("Data stored in csv")
else:
    print(f"Error: {response.status_code}")

# POST request
# Syntax: requests.post(url, data={key: value}, json={key: value}, args)

print(post) # check status code for response received
print(post.json()) #print the content

# PUT request - update user data
url1 = "https://jsonplaceholder.typicode.com/users/1"
updated_data = {'id':'1', 'name':'Lianne Graham','username':'Bret', 'email':'Sincere@april.biz'}
put = requests.put(url1, json=updated_data)
if put.status_code == 200:
    print("Post updated successfully!")
else:
    print(f"Error: {put.status_code}")

# DELETE request
url2 = "https://jsonplaceholder.typicode.com/users/1"
delete = requests.delete(url2)
if delete.status_code == 200:
    print("Post deleted successfully!")
else:
    print(f"Error: {delete.status_code}")