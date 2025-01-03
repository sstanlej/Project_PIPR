import os
from data_files import data
from classes import (Database, Course, TeacherPlan,
                     RoomCollisionError, WrongCourseIdError,
                     GroupCollisionError)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def option1():
    clear()
    print('============================================================')
    print('The list of all teachers:\n')
    teacherlist = data.database0.get_allteacherslist()
    if teacherlist == []:
        print('There are no teachers in the database.')
        print('Would you like to add a new teacher?')
    else:
        for teacher in teacherlist:
            x = 1
            print(f'{x}. {teacher.get_name()} {teacher.get_surname()}')
            print(' groups: ')
            groups = ''
            for group in teacher.get_grouplist():
                groups += f'{str(group)} '
            print(groups)


def option2():
    clear()


def option3():
    clear()


def option4():
    clear()


def option5():
    clear()


def wrong_input():
    print("Wrong input, please input a number from 0 to 5")
    input_and_go()


def input_and_go():
    choice = input(">> ")
    if choice == '0':
        return
    elif choice == '1':
        option1()
    elif choice == '2':
        option2()
    elif choice == '3':
        option3()
    elif choice == '4':
        option4()
    elif choice == '5':
        option5()
    else:
        wrong_input()


def print_main_menu():
    clear()
    print('============================================================')
    print('Welcome to Course Planner app,')
    print(' that will help you plan courses for multiple groups.\n')
    print('What do you want to do?\n')
    print('1. See the list of all teachers and their plans')
    print('2. Sign in as a new teacher')
    print('3. Log in as a teacher')
    print('4. Save current data into a file')
    print('5. Load data from a file')
    print('0. Exit')
    print('============================================================')
    input_and_go()
