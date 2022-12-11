import requests
import json
from flask import Flask,render_template
import jinja2

class Student:
    id = 0
    def __init__(self, full_name, age, level, mobile_number):
        self.id = Student.id
        self.full_name = full_name
        self.age = age
        self.level = level
        self.mobile_number = mobile_number
        Student.id += 1

    def get_student_details(self):
        return {
            "id ": self.id,
            "full_name": self.full_name,
            "age": self.age,
            "level": self.level,
            "mobile_number": self.mobile_number
        }
#### Register New Student ######
def register_new_student():
        register_url = "http://staging.bldt.ca/api/method/build_it.test.register_student"
        # data to be sent to api
        data = {
            "full_name": input("Enter Full Name: "),
            "age": input("Enter Age: "),
            "level": input("Enter Level(A,B,or C): "),
            "mobile_number": input("Enter Mobile Number: ")
        }
        # sending post request and saving response as response object
        r = requests.post(url=register_url, json=data)
        # extracting response text 
        std_url = r.json()
        print("Request URL is:%s" % std_url)

######## Edit Exist Student ######
def edit_student_details():
        # user_id = input("Enter Student ID : ")
        edit_url = "http://staging.bldt.ca/api/method/build_it.test.edit_student"
        # url_put =f"{edit_url}?id={user_id}"
        # response = requests.put(url_put)
        # print(response.json())
        data = {
            "id": input("Enter Student id :"),
            "full_name": input("Enter Full Name: "),
            "age": input("Enter Age: "),
            "level": input("Enter Level(A,B,or C): "),
            "mobile_number": input("Enter Mobile Number: ")
        }
        r = requests.put(url=edit_url, json=data)
        std_url = r.json()
        print("Request URL is:%s" % std_url)

def delete_student():
    delete_url = "http://staging.bldt.ca/api/method/build_it.test.delete_student"
    data = {
        "id": input("Enter Student id :")
    }
    r = requests.delete(delete_url, json=data)
    std_url = r.json()
    print("Request URL is:%s" % std_url)

def export_Student_to_text_file():
    result = requests.get("http://staging.bldt.ca/api/method/build_it.test.get_students")
    data = result.text
    data = json.loads(data)
    file = open("students.txt", "w")
    for i in data['data']:
        file.write(str(f"{[i]}\n"))
    file.close()

def export_student_detailas():
    url = "http://staging.bldt.ca/api/method/build_it.test.get_student_details"
    data ={
        "id": input("Enter student id :")
    }
    r = requests.delete(url, json=data)
    std_url = r.json()
    file = open("student_details.txt", "w")
    file.write(str(std_url['data']))
    file.close()

while(True):
    student = """
        1. Register New Student
        2. Edit Student Details
        3. Delete Student
        4.Export Student to text file
        5.Export Student Details to text file
        6.Exit :)
        """
    print(student)
    try:
        userInput = int(input("Please Select An Above Option: "))
    except ValueError:
        exit("\nOops! That's Not A Number")
    else:
        print("\n")

    if userInput == 1:
        register_new_student()
    elif userInput == 2:
        edit_student_details()
    elif userInput == 3:
        delete_student()
    elif userInput == 4:
        export_Student_to_text_file()
    elif userInput == 5:
        export_student_detailas()
    elif userInput == 6:
        exit("Thank You :)")
    else:
        exit("\nOops! That's Not A Number")



