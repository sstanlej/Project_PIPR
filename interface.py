import os
from data_files import data


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def option1():
    clear()
    print('='*60)
    teacherlist = data.database0.get_allteacherslist()
    if teacherlist == []:
        no_teachers()
    else:
        print('The list of all teachers:\n')
        x = 1
        for teacher in teacherlist:
            print(f'{x}. {teacher.get_name()} {teacher.get_surname()}')
            groups = ''
            for group in teacher.get_grouplist():
                groups += f'{str(group)}  '
            print(f' groups: {groups}\n')
            x += 1


def option2():
    clear()
    print('='*60)
    print('Welcome to teacher creator.')


def option3():
    clear()
    print('='*60)
    teacherlist = data.database0.get_allteacherslist()
    if teacherlist == []:
        no_teachers()
    else:
        print('Choose a teacher you\'d like to log in as from the list')


def option4():
    clear()
    print('='*60)
    print('Please specify the name of the file you want to save data to.')


def option5():
    clear()
    print('='*60)
    print('Please specify the name of the file you want to load data from.')


def no_teachers():
    print('There are no teachers in the database.')
    print('Would you like to add a new teacher?')
    print('Y - Yes')
    print('N - Go back to main menu')
    input_and_go_addT()


def wrong_input_menu():
    print("Wrong input, please input a number from 0 to 5")
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
    print('3. Log in as a teacher')
    print('4. Save current data into a file')
    print('5. Load data from a file')
    print('0. Exit')
    print('='*60)
    input_and_go_menu()
