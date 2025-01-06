import os
from data_files import data
from datetime import time
from classes import TeacherPlan, Course


def add_template_teachers():

    course1 = Course(0, 'mako', 102, 's14', time(7, 15), time(9, 0), 'mon')
    course2 = Course(1, 'anma', 104, 's15', time(11, 15), time(12, 0), 'fri')
    course3 = Course(2, 'mako', 103, 's14', time(9, 15), time(11, 0), 'mon')
    course4 = Course(3, 'mako', 105, 's14', time(12, 15), time(14, 0), 'wed')

    teacher1 = TeacherPlan('t1', 'Stan', 'Ban', [course1, course2,
                                                 course3, course4])
    teacher2 = TeacherPlan('t2', 'John', 'Pork', [])

    data.database0.add_teacher(teacher1)
    data.database0.add_teacher(teacher2)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_teacher_info(printplan):
    teacherlist = data.database0.get_allteacherslist()
    x = 1
    for teacher in teacherlist:
        tname = teacher.get_name()
        tsurname = teacher.get_surname()
        tid = teacher.get_id()
        print(f'{x}. {tname} {tsurname} (id: {tid})')
        if printplan == 1:
            if teacher.get_courselist() == []:
                print('This teacher has no courses planned.\n\n')
            else:
                print('Teacher plan:\n')
                teacher.print_plan()
                print('\n\n')
        x += 1


def option1():
    clear()
    print('='*60)
    teacherlist = data.database0.get_allteacherslist()
    if teacherlist == []:
        no_teachers()
    else:
        print('The list of all teachers:\n')
        print_teacher_info(1)
        print('='*60)
        input_back_to_menu()


def option2():
    clear()
    print('='*60)
    print('Welcome to teacher creator.\n')
    print('Please specify unique teacher ID:')

    teacherlist = data.database0.get_allteacherslist()
    newtid = input('>> ')
    for teacher in teacherlist:
        teacherid = teacher.get_id()
        while newtid == teacherid:
            print('Teacher with specified ID already exists, please try again.')
            newtid = input('>> ')

    print(f'Your chosen ID: {newtid}\n')
    print('Please specify teacher\'s name:')
    newtname = input('>> ')
    print(f'Your chosen name: {newtname}\n')
    print('Please specify teacher\'s surname:')
    newtsurname = input('>> ')
    print(f'Your chosen surname: {newtsurname}\n')
    newteacher = TeacherPlan(newtid, newtname,
                             newtsurname, [])
    data.database0.add_teacher(newteacher)
    print(f'Teacher {newtname} {newtsurname} succesfully created!\n')
    print('='*60)
    input_back_to_menu()


def option3():
    clear()
    teacherlist = data.database0.get_allteacherslist()
    if teacherlist == []:
        print('There are no teachers in the database.')
        print('='*60)
        input_back_to_menu()
    else:
        print('Please type the ID of the teacher you\'d like to remove.')
        print_teacher_info(0)
        print('\n')
        remtid = input('>> ')
        for teacher in teacherlist:
            tid = teacher.get_id()
            if remtid == tid:
                tname = teacher.get_name()
                tsurname = teacher.get_surname()
                data.database0.remove_teacher(remtid)
                print(f'Teacher {tname} {tsurname} successfully removed.\n')
                input_back_to_menu()
                break
        print('There is no teacher with specified ID\n')
        input_back_to_menu()


def option4():
    clear()
    print('='*60)
    teacherlist = data.database0.get_allteacherslist()
    if teacherlist == []:
        no_teachers()
    else:
        print('Choose a teacher you\'d like to log in as from the list\n')
        allcourseslist = data.database0.get_allcourseslist()
        print(allcourseslist)
        print('='*60)
        input_back_to_menu()


def option5():
    clear()
    print('='*60)
    print('Please specify the name of the file you want to save data to.\n')
    print('='*60)
    input_back_to_menu()


def option6():
    clear()
    print('='*60)
    print('Please specify the name of the file you want to load data from.\n')
    print('='*60)
    input_back_to_menu()


def no_teachers():
    print('There are no teachers in the database.')
    print('Would you like to add a new teacher?')
    print('Y - Yes')
    print('N - Go back to main menu')
    input_and_go_addT()


def input_back_to_menu():
    print('To go back to menu type 0')
    choice = input('>> ')
    if choice == '0':
        print_main_menu()
    else:
        input_back_to_menu()


def wrong_input_menu():
    print("Wrong input, please input a number from 0 to 6")
    input_and_go_menu()


def wrong_inputYN():
    print("Wrong input, please input Y or N")
    input_and_go_addT()


def input_and_go_addT():
    choice = input('>> ')
    if choice == 'Y':
        option2()
    elif choice == 'N':
        print_main_menu()
    else:
        wrong_inputYN()


def input_and_go_menu():
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
    elif choice == '6':
        option6()
    else:
        wrong_input_menu()


def print_main_menu():
    clear()
    print('='*60)
    print('Welcome to Course Planner app,')
    print(' that will help you plan courses for multiple groups.\n')
    print('What do you want to do?\n')
    print('1. See the list of all teachers and their plans')
    print('2. Add a new teacher')
    print('3. Remove a teacher from database')
    print('4. Log in as a teacher')
    print('5. Save current data into a file')
    print('6. Load data from a file')
    print('0. Exit')
    print('='*60)
    input_and_go_menu()
