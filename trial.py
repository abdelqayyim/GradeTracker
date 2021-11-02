from os import name
import numpy
data = {"COIS-1400H": {
        "LAB": [
            1.0,
            1.0,
            1.0,
            1.0,
            1.0
        ],
        "ASSIGNMENT": [
            0.55
        ],
        "LAB-WORTH": 20,
        "ASSIGNMENT-WORTH": 40,
        "MIDTERM-WORTH": 20,
        "FINAL EXAM-WORTH": 20
    },
    "ENG-1001H": {
        "PASSAGE ANALYSIS": [
            0.8
        ],
        "PASSAGE ANALYSIS-WORTH": 15,
        "MIDTERM-WORTH": 20,
        "SECOND ESSAY-WORTH": 20,
        "FINAL EXAM-WORTH": 20
    },
    "MATH-1550H": {
        "QUIZ": [
            0.83,
            0.83,
            0.5,
            0.83
        ],
        "TEST": [
            0.98,
            0.67
        ],
        "QUIZ-WORTH": 14,
        "TEST-WORTH": 48,
        "FINAL EXAM-WORTH": 38
    },
    "ADMN-1620H": {
        "QUIZ": [
            0.76,
            0.96,
            1.0,
            0.92,
            0.96,
            1.0
        ],
        "QUIZ-WORTH": 15,
        "MIDTERM-WORTH": 30,
        "FINAL EXAM-WORTH": 30,
        "ASSIGNMENT-WORTH": 25

    },
    "COIS-1020H": {
        "ASSIGNMENT": [
            0.85
        ],
        "LAB": [
            1.0,
            0.91,
            1.0,
            0.81,
            0.91,
            0.82
        ],
        "TEST": [
            0.83,
            0.86
        ],
        "LAB-WORTH": 20,
        "ASSIGNMENT-WORTH": 25,
        "MIDTERM-WORTH": 20,
        "FINAL EXAM-WORTH": 35,
    },
    "PERCENTAGE": {"COIS-1020H": 
    {"LAB-WORTH": 20, "ASSIGNMENT-WORTH": 25,"MIDTERM-WORTH": 20,"FINAL EXAM-WORTH": 35 },
    "COIS-1400H":{"LAB-WORTH": 20,
        "ASSIGNMENT-WORTH": 40,
        "MIDTERM-WORTH": 20,
        "FINAL EXAM-WORTH": 20},
    "MATH-1550H": {"QUIZ-WORTH": 14,
        "TEST-WORTH": 48,
        "FINAL EXAM-WORTH": 38},
    "ADMN-1620H": {"QUIZ-WORTH": 15,
        "MIDTERM-WORTH": 30,
        "FINAL EXAM-WORTH": 30,
        "ASSIGNMENT-WORTH": 25},
    "ENG-1001H": {"PASSAGE ANALYSIS-WORTH": 15,
        "MIDTERM-WORTH": 20,
        "SECOND ESSAY-WORTH": 20,
        "FINAL EXAM-WORTH": 20},

    } }

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
                ac_av = av * data["PERCENTAGE"][class_name][f"{ass}-WORTH"]
                class_average.append(ac_av)
            actual_class_average = numpy.mean(class_average)
            print(class_average)
