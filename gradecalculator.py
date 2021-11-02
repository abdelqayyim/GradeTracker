from json.decoder import JSONDecodeError
from os import error
from sys import exec_prefix
from tkinter import *
from tkinter import messagebox
import json 
import numpy
from numpy.core.fromnumeric import mean
from numpy.lib.shape_base import tile
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
FILE = "/Users/abdelqayyimmaazouyahaya/Desktop/Projects/GradeAverageCalculator/data.json"
ASSIGNMENT_OPTIONS = ['LAB', 'MIDTERM', 'PASSAGE ANALYSIS', 'FINAL EXAM', 'SECOND ESSAY', 'QUIZ', 'TEST', 'ASSIGNMENT']
CLASS_OPTIONS = ['COIS-1020H', 'MATH-1550H', 'ENG-1001H', 'COIS-1400H', 'ADMN-1620H']


def datas():
    global grade, existing_norep_class, existing_norep_classassignment, classes_data, class_name, assignment
    grade_string = grade_entry.get()
    grade_string.strip()
    random_list = []
    length = len(grade_string)
    index = grade_string.index("/")
    num1 = ""
    num2 = ""
    for number in range(index):
        num1 += grade_string[number]
    random_list.append(float(num1))
    for number in range(index + 1, length):
        num2 += grade_string[number]
    random_list.append(float(num2))
    grade = round(random_list[0] / random_list[1], 2)
    class_name = class_entry.get().upper()
    if not (class_name in CLASS_OPTIONS):
        messagebox.showerror(title="ERROR", message="This class name is not one of the options for classes")
    else:
        assignment = assignment_entry.get().upper()
        if not (assignment in ASSIGNMENT_OPTIONS):
            messagebox.showerror(title="ERROR", message="This assignment name is not one of the options for assignment")
        else:
            classes_data = {class_name:{assignment:[grade]}}
            exisitng_classes_list = []
            existing_class_and_assignment = []
    try:
        with open(FILE, "r") as data_file:
            data = json.load(data_file)
        for key, value in data.items():
            for name in value.items():
                exisitng_classes_list.append(key)
                existing_class_and_assignment.append((key, name[0]))
            existing_norep_class = list(set(exisitng_classes_list))
            existing_norep_classassignment = list(set(existing_class_and_assignment ))
    except JSONDecodeError:
        messagebox.askokcancel(title="CONFIRMATION", message=f"You are about to add a new class '{class_name}' to the data")
        with open(FILE, "w") as data_file:
            json.dump(classes_data, data_file, indent=4)
        class_entry.delete(0, END)
        assignment_entry.delete(0, END)
        grade_entry.delete(0, END)

def delete_entries():
    class_entry.delete(0, END)
    assignment_entry.delete(0, END)
    grade_entry.delete(0, END)


def add_class():
    datas()
    print(existing_norep_class)
    with open(FILE, "r") as data_file:
        data = json.load(data_file)
    if class_name in existing_norep_class:
        if (class_name, assignment) in existing_norep_classassignment:
            messagebox.showerror(title="ERROR", message="This assignment name already exists in this class. Use the add grade button to add a grade")
        else:
            if messagebox.askokcancel(title="CONFIRMATION", message=f"You are about to add an assignment to already existing class {class_name}"):
                data[class_name][assignment] = classes_data[class_name][assignment]
                with open(FILE, "w") as data_file:
                    json.dump(data, data_file, indent=4)
                    delete_entries()
    else:
        if messagebox.askokcancel(title="CONFIRMATION", message="You are about to add a new class"):
            data[class_name] = classes_data[class_name]
            with open(FILE, "w") as data_file:
                json.dump(data, data_file, indent=4)
            delete_entries()

def add_grade():
    datas()
    with open(FILE, "r") as data_file:
        data = json.load(data_file)
    if (class_name, assignment) in existing_norep_classassignment:
        data[class_name][assignment].append(grade)
        messagebox.showinfo(title="CONFIRMATION", message=f"You are about to add a new grade to {assignment} in {class_name}")
        with open(FILE, "w") as data_file:
            json.dump(data, data_file, indent=4)
            delete_entries()
    else:
        messagebox.showerror(title='ERROR', message="To add a grade, make sure you both the assignment and grade are properly written")


def average():
    class_name = class_entry.get().upper()
    assignment = assignment_entry.get().upper()
    with open(FILE, "r") as data_file:
        data = json.load(data_file)
    existing_classes = []
    existing_combo  = []
    assignment_for_class = []
    class_average  =[]
    if len(class_name) > 0:
        for key, value in data.items():    #gets you the existing classes in data
            existing_classes.append(key)
            for val in value.items():
                existing_combo.append((key, val[0]))
        if class_name in existing_classes:             #gets you the assignments for that class
            for key, value in data[class_name].items():
                assignment_for_class.append(key)
            if (len(assignment) == 0):       #starting here you have the assingment, assignm
                print(len(assignment))    #if there is no entry in assignment
                for ass in assignment_for_class:
                    av = numpy.mean(data[class_name][ass])
                    class_average.append(av)
                actual_class_average = numpy.mean(class_average)
                print(class_average)
                messagebox.showinfo(title=f"{class_name}", message=f"The average for {class_name} is {actual_class_average}")
                delete_entries() 
            else:
                if assignment in assignment_for_class:
                    assignment_average = mean(data[class_name][assignment])  #you get the average for the class and assignment
                    messagebox.showinfo(title=f"{class_name}", message=f"The average for {assignment} in {class_name} is {assignment_average}")
                    delete_entries() 
                else:
                    messagebox.showerror(title="ERROR", message=f"This assignment does not exist in the class {class_name}")
        else:
            messagebox.showerror(title="ERROR", message="THIS class is not part of the existing classes. Use the add class button to add a class")
    else:
        messagebox.showerror(title='ERROR', message="You must enter a class")

def existing_data():
    with open(FILE, "r") as data_file:
        data = json.load(data_file)
    classes = []
    for key, value in data.items():
        classes.append(key)
    to_print = ""
    for stuf in classes:
        to_print += f"{stuf , data[stuf]}\n"
    messagebox.showinfo(title="DATA", message=f"{to_print}")


def number_input():
    class_name = class_entry.get().upper()
    assignment = assignment_entry.get().upper()
    if class_name in CLASS_OPTIONS:
        with open(FILE, "r") as data_file:
            data = json.load(data_file)
        assignment_for_class = []
        for key, value in data[class_name].items():
            assignment_for_class.append(key)
        assignment_list = list(set(assignment_for_class))
        if assignment in ASSIGNMENT_OPTIONS:
            if assignment in assignment_list:
                amount = len(data[class_name][assignment])
                messagebox.showinfo(title="INFORMATION", message=f"There are {amount} inputs for {assignment} in {class_name}")
                delete_entries()
            else:
                messagebox.showerror(title="ERROR", message="This class does not have this assignment yet. Use the add button to add it")
        else:
            messagebox.showerror(title="ERROR", message="This assignment name does not exist")
    else:
        messagebox.showerror(title="ERROR", message="This class is not in the data yet. Use the add class button to add it")



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


class_entry = Entry(width=30, highlightthickness=0, bg=COLOR2)
class_entry.grid(row=1, column=1)

assignment_entry = Entry(width=23, highlightthickness=0, bg=COLOR2)
assignment_entry.grid(row=2, column=1, sticky=W)

grade_entry = Entry(width=30, highlightthickness=0, bg=COLOR2)
grade_entry.grid(row=3, column=1)

average_button = Button(text="Average", font=(FONT, 14, "bold"), command=average, highlightthickness=0, foreground=COLOR6)
average_button.grid(row=4,column=1)

add_button = Button(text="Add Grade", width=12, font=(FONT, 12, "bold"),command=add_grade, foreground=COLOR7) #,command=add_grade
add_button.grid(row=5,column=1)

existing_data_button = Button(text="Look at Existing Data", width=20,font=("Arial", 12, "bold"), command=existing_data, foreground=COLOR8) 
existing_data_button.grid(row=0, column=1)

add_class_or_assignment = Button(text="Add Class or Assignment",width=24, font=("Times New Roman", 12, "bold"),command=add_class, foreground=COLOR9)
add_class_or_assignment.grid(row=6,column=1)

input_button = Button(text="# Input", width=10, font=("Times New Roman", 12, "bold"), command=number_input)
input_button.grid(row=2, column=1, sticky=E)

window.mainloop()






