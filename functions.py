from tkinter import *
import sqlite3
def inputs_valid(class_name, assignment, grade):
    if(len(class_name)==0 or len(assignment)==0 or len(grade)==0 ):
        return False
    else:
        print("all inputs are valid")
        return True
def check_interger(value):
    try:
        a = value
        b = float(a)
        return True
    except ValueError:
        return False
def AssignmentInDatabase(classN, assignment)-> (bool):
    connection = sqlite3.connect("database.db") #Create a Database 
    cursor = connection.cursor() #Create Cursor in Order to add tables and values 
    cursor.execute(f"SELECT Assignment_Name FROM Grades WHERE Class_Name = '{classN}'")
    connection.commit()
    try:
        print(cursor.fetchall()[0])
        returned_class_value = cursor.fetchall()[0] #if there is a value
        if assignment in returned_class_value:
            print("Assignment DOES  EXIST")
            return True
    except IndexError:
        print("Assignment DOES NOT EXIST")
        return False

def ClassInDatabase(passedClass):
    connection = sqlite3.connect("database.db") #Create a Database 
    cursor = connection.cursor() #Create Cursor in Order to add tables and values 
    cursor.execute(f"SELECT Class_Name FROM Grades WHERE Class_Name = '{passedClass}' ")
    connection.commit()
    try:
        returned_class_value = cursor.fetchall()[0][0] #if there is a value
        if returned_class_value == passedClass:
            print("CLASS DOES  EXIST")
            return True
    except IndexError:
        returned_class_value = cursor.fetchall() #will return an empty string
        print("CLASS DOES NOT EXIST")
        return False

def delete_entries(class_name, assignment_name, grade_input):
    class_name.delete(0, END)
    assignment_name.delete(0, END)
    grade_input.delete(0, END)
def delete_two_entries(assignment_name,grade_input):
    grade_input.delete(0, END)
    assignment_name.delete(0, END)