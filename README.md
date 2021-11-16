# GRAGE TRACKER
## Description
This Graphical User Interface (GUI) is meant to allow students to locally track their grades within having to log into their school database. The GUI also allows students to calculate their class and assignments averages. 
## Inserting Data in the Database
The database is set up using SqLite3 with a Python background. The following table represents how the data is inserted in the database. 

| Class Name | Assignment | Values | 
| :---------:  | :---------:  | :---------: |
|COMP-1406| QUIZ | [80,95, 70, 70] |
| COMP-1406 | ASSIGMENT | [88, 97, 60, 85] |
| CRIM-1010 | TEST | [90, 78, 88, 85] |

To insert a class in the database, the user has to input a **class name**, an **assignment** (assignment, quiz, test etc...), and a valid **grade** (integer or decimal). 
- A class can have as many assignments as possible. 
- If The class and assignment already exist, the grade in the grade input will just be added in the array for the assignment grade. 

Each button on the GUI has an **Info** button that should give the user information regarding the purpose of a button. 

To calculate the **average**
1. Enter either the class name or, 
2. Enter the class name and assignment name
3. If only the class name is inputted, then the average for the entire class will be calculate, all assignments included
4. If the class name and assignment name is inputted, then that specific assignment's average will be calculated. 








