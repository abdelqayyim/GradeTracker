from json.decoder import JSONDecodeError
from os import confstr, error
from sys import exec_prefix
from tkinter import *
from tkinter import messagebox
import tkinter.messagebox
import json
from typing import Tuple 
import numpy
import sqlite3
from numpy.core.fromnumeric import mean
from numpy.lib.shape_base import tile
from functions import * 
COLOR1 = "#f2b4b4"
COLOR2 = "#a7c5eb"
COLOR3 = "#6ddccf"
COLOR4 = "#c5d7bd"
COLOR5 = "#eaffd0"
COLOR6 = "#822659"
COLOR7 = "#0a043c"
COLOR8 = "#09015f"
COLOR9 = '#2c061f'
FONT ="Times New Roman"

connection = sqlite3.connect("database.db") #Create a Database 
cursor = connection.cursor() #Create Cursor in Order to add tables and values 

try:
    cursor.execute('''CREATE TABLE Grades
               (Class_Name text, Assignment_Name text, Vals text,primary key(Class_Name, Assignment_Name) )''')  #Creating the table 
except sqlite3.OperationalError:
    pass

# cursor.execute("SELECT Vals FROM Grades WHERE Class_Name = 'COMP1807' AND Assignment_Name = 'QUIZ'")
# cursor.execute("DELETE FROM Grades WHERE Class_Name = 'COMP1805'")
# cursor.execute("SELECT * FROM Grades")
values = cursor.fetchall()
connection.commit() #to save the changes, to commit them 
connection.close()
# print(len(values))



def average():
    class_name = class_entry.get().upper()
    assignment_name = assignment_entry.get().upper()
    connection = sqlite3.connect("database.db") #Create a Database 
    cursor = connection.cursor() #Create Cursor in Order to add tables and values 
    
    if ClassInDatabase(class_name):#check that the class name in put is still in 
        if len(assignment_name) != 0:
            if AssignmentInDatabase(class_name, assignment_name):
                #show the average for that assignment
                cursor.execute(f"SELECT Vals FROM Grades where Class_Name='{class_name}' AND Assignment_Name='{assignment_name}'")
                connection.commit() 
                results = cursor.fetchall()[0][0]
                array = []
                for x in  results.split(","):
                    array.append(float(x))
                messagebox.showinfo(title=f'{class_name}: {assignment_name}', message=f'The average for {assignment_name} in {class_name} is {numpy.mean(array)}%') 
            else:
                #tell the user that the assignment does not exist
                messagebox.showerror(title='Assignment Does not exist',message=f'The assignment {assignment_name} does not exist in the database, make sure to add it before requesting the average')
        else:
            #just show the average for the class as a whole 
            cursor.execute(f"SELECT * FROM Grades where Class_Name='{class_name}'")
            connection.commit() 
            results = cursor.fetchall()
            array = []
            for x in results:
                for y in x[2].split():
                    array.append(float(y))
            messagebox.showinfo(title=f'{class_name}', message=f'The average for {class_name} is {numpy.mean(array)}%') 
            
    else:
        #tell the user that the class is not in the database
        messagebox.showerror(title="Class not in Database", message=f"The class {class_name} is not yet in the database. Add it before computing the average")



    
#Add a "Info button next to each button in order to let the user know what each button does."
def existing_data():
    connection = sqlite3.connect("database.db") #Create a Database 
    cursor = connection.cursor() #Create Cursor in Order to add tables and values 
    cursor.execute(f"SELECT * FROM Grades")
    results = cursor.fetchall()
    connection.commit() 
    res = ""
    for x in results:
        res += x[0]+" -> "+x[1]+": "+x[2]+"\n"
        # print( f"{x[0]} -> {x[1]}: {x[2]}")
    messagebox.showinfo(title="Data", message=f"{res}")  

 



def add_class():
    connection = sqlite3.connect("database.db") #Create a Database 
    cursor = connection.cursor() #Create Cursor in Order to add tables and values 
    class_name = class_entry.get().upper()
    assignment_name = assignment_entry.get().upper()
    grade_name = grade_entry.get().upper()
    if inputs_valid(class_name,assignment_name, grade_name): #if class inputs fields are not empty
        if ClassInDatabase(class_name) and AssignmentInDatabase(class_name, assignment_name) and check_interger(grade_name):#User inputted grade, assignment and number all valid
            connection = sqlite3.connect("database.db") #Create a Database 
            cursor = connection.cursor() #Create Cursor in Order to add tables and values 
    
            cursor.execute(f"SELECT Vals FROM Grades WHERE Class_Name = '{class_name}' AND Assignment_name='{assignment_name}' ")
            results = cursor.fetchall()[0][0] 
            connection.commit()   
            print(results.split(","))
            new_values = ""
            new_values += results
            new_values+= ","+grade_name
            cursor.execute(f"UPDATE Grades SET Vals='{str(new_values)}' WHERE Class_Name ='{class_name}' AND Assignment_Name='{assignment_name}'")
            connection.commit()
            connection.close()
            messagebox.showinfo(title="Successfully added", message="The grade has been successfully added to the database")
            delete_two_entries(assignment_entry,grade_entry)
            #THIS ONE IS THE UPDATE
            # check if the class and assignment already exist then add the grade or the class as a whole
        elif ClassInDatabase(class_name) and AssignmentInDatabase(class_name, assignment_name) and check_interger(grade_name) == False:#User inputted grade, assignment but not valid number
            messagebox.showerror(title="INVALID GRADE", message="The grade input has to be a number, no letters allowed")
        #tell the user to just fix the number
        elif ClassInDatabase(class_name) == False and AssignmentInDatabase(class_name, assignment_name) and check_interger(grade_name):#User assignment and number but not class name
            messagebox.askokcancel(title="Class not in Database", message=f"The class: {class_name} is not yet in the database. Press ok to input it along with the assignment and grade.")
            if messagebox.askokcancel() == True:
                connection = sqlite3.connect("database.db") #Create a Database 
                cursor = connection.cursor() #Create Cursor in Order to add tables and values 
                cursor.execute(f"INSERT INTO Grades VALUES('{class_name}', '{assignment_name}','{grade_name}')")
                connection.commit()
                connection.close()
            messagebox.showinfo(title="Successfully added", message="The grade has been successfully added to the database")
            delete_entries(class_entry,assignment_entry,grade_entry)
        #class does not yet exist, 
        elif ClassInDatabase(class_name) and AssignmentInDatabase(class_name, assignment_name) == False and check_interger(grade_name):#User inputted grade and number but not assignment
            messagebox.askokcancel(title="Assignment not in Database", message=f"The Assignment: {assignment_name} is not yet in the database. Press ok to input it.")
            if messagebox.askokcancel() == True:
                connection = sqlite3.connect("database.db") #Create a Database 
                cursor = connection.cursor() #Create Cursor in Order to add tables and values 
                cursor.execute(f"INSERT INTO Grades VALUES('{class_name}', '{assignment_name}','{grade_name}')")
                connection.commit()
                connection.close()
                messagebox.showinfo(title="Successfully added", message="The grade has been successfully added to the database")
                delete_entries(class_entry,assignment_entry,grade_entry)
        #press ok to add the assignment to the database, let them know that the assignment does not exist yet
        elif ClassInDatabase(class_name) and AssignmentInDatabase(class_name, assignment_name)==False and check_interger(grade_name)==False:#User inputted grade but not VALID assignment or number 
            messagebox.showerror(title="Assignment not in Database, and Not correct grade input", message=f"The Assignment: {assignment_name} is not yet in the database, and the grade is not valid (must be numbers).")
        elif ClassInDatabase(class_name) == False and AssignmentInDatabase(class_name, assignment_name)==False and check_interger(grade_name):#User inputted number but not VALID assignment or class 
            messagebox.askokcancel(title="Class And Assignment Not in Database", message=f"The class: {class_name} and Assignment: {assignment_name} not in database. Pess 'ok' to add them")
            if messagebox.askokcancel() == True:
                connection = sqlite3.connect("database.db") #Create a Database 
                cursor = connection.cursor() #Create Cursor in Order to add tables and values 
                cursor.execute(f"INSERT INTO Grades VALUES('{class_name}', '{assignment_name}','{grade_name}')")
                connection.commit()
                connection.close()
            messagebox.showinfo(title="Successfully added", message="The grade has been successfully added to the database")
            delete_entries(class_entry,assignment_entry,grade_entry)
        #class does not exist, so the assignment does not exist, press ok to add them
        elif ClassInDatabase(class_name)==False and AssignmentInDatabase(class_name, assignment_name)==False and check_interger(grade_name) == False:
             messagebox.showerror(title="Class and Assignment not in Database, and Not correct grade input", message=f"The class: {class_name} and the Assignment: {assignment_name} is not yet in the database, and the grade is not valid (must be numbers).")
    else:
        messagebox.showerror(title="EMPTY INPUT FIEL", message="You have left an input field empty. Make sure all input fields have an input")
    #tell the user that no input can be empty





    #check to see if the assignment exists
# def number_input():


window = Tk()
window.title("Grade Average Calculator")
window.minsize(height=400, width=500)
window.config(padx=100, pady=100, bg=COLOR1)

class_label = Label(text="Class:", highlightthickness=0, bg=COLOR3)          #class label
class_label.grid(row=1,column=0,sticky=E)            #class placement
assignment_label = Label(text="Assignment:", highlightthickness=0, bg=COLOR5)   #assignment label
assignment_label.grid(row=2,column=0, sticky=E)          #assignment placement
grade_label = Label(text="Grade:", highlightthickness=0, bg=COLOR4)             #grade label
grade_label.grid(row=3,column=0, sticky=E)               #grade placement


class_entry = Entry(width=23, highlightthickness=0, bg=COLOR2)
class_entry.grid(row=1, column=1)


assignment_entry = Entry(width=23, highlightthickness=0, bg=COLOR2)
assignment_entry.grid(row=2, column=1, sticky=W)

grade_entry = Entry(width=23, highlightthickness=0, bg=COLOR2)
grade_entry.grid(row=3, column=1)

average_button = Button(text="Average", font=(FONT, 14, "bold"), command=average, highlightthickness=0, foreground=COLOR6)
average_button.grid(row=4,column=1)
average_entry_info = Button(text="Info", foreground=COLOR6, command=average_info)
average_entry_info.grid(row=4,column=2)

add_button = Button(text="Add Grade", width=12, font=(FONT, 12, "bold"),command=add_class, foreground=COLOR7) #,command=add_grade
add_button.grid(row=5,column=1)
add_entry_info = Button(text="Info", foreground=COLOR6, command=add_info)
add_entry_info.grid(row=5,column=2)

existing_data_button = Button(text="Look at Existing Data", width=20,font=("Arial", 12, "bold"), command=existing_data, foreground=COLOR8) 
existing_data_button.grid(row=6, column=1)
existing_entry_info = Button(text="Info", foreground=COLOR6, command=existing_info)
existing_entry_info.grid(row=6,column=2)
# add_class_or_assignment = Button(text="Add Class or Assignment",width=24, font=("Times New Roman", 12, "bold"),command=add_class, foreground=COLOR9)
# add_class_or_assignment.grid(row=6,column=1)

# input_button = Button(text="See Inputs", width=10, font=("Times New Roman", 12, "bold"), command=number_input)
# input_button.grid(row=2, column=1, sticky=E)

window.mainloop()






