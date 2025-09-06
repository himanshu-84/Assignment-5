dict = {'himanshu':'34', 'rahul':'78', 'rohit':'91', 'sachin':'45', 'sagar':'67'}
username = input("Enter the student name :")
if username in dict:
    print(f"{username}'s marks are {dict[username]}")
else:
    print("student not found in the records.")