import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_list_of_teachers():
    clear()
    print('============================================================')
    print('The list of all teachers:\n')


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
    choice = input(">> ")
    if choice == "1":
        print_list_of_teachers()
    elif choice == "0":
        return
