from tkinter import *
import sqlite3
from tkinter import messagebox
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
        b = cursor.fetchall()
        returned_class_value = [] #if there is a value
        for x in b:
            returned_class_value.append(x[0])
        if assignment in returned_class_value:
            print("Assignment DOES  EXIST")
            return True
        else:
            return False
    except IndexError:
        print("Assignment DOES NOT EXIST")
        return False

def ClassInDatabase(passedClass):
    connection = sqlite3.connect("database.db") #Create a Database 
    cursor = connection.cursor() #Create Cursor in Order to add tables and values 
    cursor.execute(f"SELECT Class_Name FROM Grades WHERE Class_Name = '{passedClass}' ")
    connection.commit()
    try:
        b = cursor.fetchall()
        returned_class_value = [] #if there is a value
        for x in b:
            returned_class_value.append(x[0])
        if passedClass in returned_class_value:
            print("CLASS DOES  EXIST")
            return True
        else:
            return False
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

def existing_info():
    messagebox.showinfo(title="Viewing Existing Data", message="Press 'Look at Existing Data'to view the existing data, no need to input a class name or assignment")
def add_info():
    messagebox.showinfo(title="Adding Info", message="Insert a class name and class assignment name, then enter a valid grade input (integer or decimal). Then Press 'Add Grade' to add the grade/assignment and grade to the database. If the class already exists, the assignment will be added, and if both the class and the assignment exist, then the grade will be added.")
def average_info():
    messagebox.showinfo(title="Viewing Average", message="Enter a class name in order to view the average for the entire class (including all the assignments), and enter the class name and assignment name in order to see the average for the specific assignment.")
    
