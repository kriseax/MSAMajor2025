from datetime import datetime
from Student import Student

"""
Function to write an error message to a log file
Input: (string)error message
Output: None
"""
def write_to_error_log(message:str) -> None:
    the_date = datetime.now()
    #open the log file in append mode: error_log.txt
    with open("error_log.txt", "a") as log_file:
        log_file.write(f"{the_date}: {message}\n")
    #write error message to the file in the format 
    #Date: message -> 6/24/2025: Error in datafile on line 5
    #close file
    return

"""
Function to return a list of student objects
Input: none
Output: list of student objects
"""    

def load_students() -> list[Student]:
    #create an empty list and annotate that the list will store Student items
    list_of_students: list[Student] = []

    #create a file handler
    file = open("students.csv", "r")

    #create variable to keep track of line in file that we are reading
    line_number = 0
    #read file line by line in for loop
    for line_of_data in file:
        line_number += 1
        #skip first line in csv file
        if line_number == 1:
            continue
        
        #split the line of data at the comma
        student_data = line_of_data.split(",")

        if len(student_data) != 6:
            #write an error message to and error log
            message = f"Error: Data format error on line {line_number}. Did not get 6 items in line of data"
            write_to_error_log(message)
            continue
    
        #handle errors in data format. line_of_data should have 6 items
        #if error in format then write a message to a log file and continue reading from the file
        try:
            credit_hours = int(student_data[3])
            gpa = float(student_data[4])
        except Exception as err:
            #write an error message to an error log
            message = f"Error: credit hours or gpa not a number on line {line_number}"
            write_to_error_log(message)
            continue

        #get student data and create a student object for each student
        first_name = student_data[0]
        last_name = student_data[1]
        major = student_data[2]
        student_id = student_data[5].strip()

        new_student = Student(first_name, last_name, major, credit_hours, gpa, student_id)
        list_of_students.append(new_student)

    return list_of_students

"""
Function to convert student objects to student dictionaries
Input: list of studetn objects
Output: List of student dictionaries
"""
def student_to_dictionary(list_of_students: list[Student]) -> list[dict]:
    #create a list to store the dictionaries in
    student_dictionary_list = []

    #loop through the student list and write each student's data to a dictionary
    for student in list_of_students:
        #create an empty dictionary
        student_dictionary = {}

        #set the keys and values for the dictionary
        student_dictionary['first_name'] = student.get_first_name()
        student_dictionary['last_name'] = student.get_last_name()
        student_dictionary['major'] = student.get_major()
        student_dictionary['gpa'] = student.get_gpa()
        student_dictionary['class'] = student.get_class_level()
        student_dictionary['id'] = student.get_ID()

        #append the dictionary to the list of dictionaries
        student_dictionary_list.append(student_dictionary)

    #return the list of dictionaries
    return student_dictionary_list

"""
Function to get a list of student dictionaries
Input: None
Output: List of student dictionaries
"""
def get_student_dictionaries():
    #get a list of students
    student_list = load_students()

    #get a list of stuudent dictionaries
    student_dictionaries = student_to_dictionary(student_list)

    for student_dict in student_dictionaries:
        print(student_dict)

    return student_dictionaries

get_student_dictionaries()