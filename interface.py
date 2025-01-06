import os
from data_files import data
from classes import TeacherPlan


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_teacher_info(printplan):
    teacherlist = data.database0.get_allteacherslist()
    x = 1
    for teacher in teacherlist:
        tname = teacher.get_name()
        tsurname = teacher.get_surname()
        tid = teacher.get_id()
        line = f'{x}. {tname} {tsurname} (id: {tid})'
        printbox(line, 112)
        if printplan == 1:
            if teacher.get_courselist() == []:
                printbox('This teacher has no courses planned.', 112)
                printbox(' ', 112)
                printbox(' ', 112)
            else:
                printbox('Teacher plan:', 112)
                teacher.print_plan()
                printbox(' ', 112)
                printbox(' ', 112)
        x += 1


def option1():
    clear()
    teacherlist = data.database0.get_allteacherslist()
    if teacherlist == []:
        print('='*60)
        no_teachers()
    else:
        print('='*114)
        printbox('The list of all teachers:', 112)
        print('='*114)
        printbox(' ', 112)
        print_teacher_info(1)
        print('='*114)
        input_back_to_menu()


def option2():
    clear()
    print('='*60)
    print('Welcome to teacher creator.\n')
    print('Please specify unique teacher ID:')

    newtid = input_newid('Teacher')

    print(f'Your chosen ID: {newtid}\n')
    print('Please specify teacher\'s name:')
    newtname = input('>> ')
    while not newtname:
        newtname = input('>> ')
    print(f'Your chosen name: {newtname}\n')
    print('Please specify teacher\'s surname:')
    newtsurname = input('>> ')
    while not newtsurname:
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
    print('='*60)
    teacherlist = data.database0.get_allteacherslist()
    if teacherlist == []:
        print('There are no teachers in the database.')
        input_back_to_menu()
    else:
        print('Please type the ID of the teacher you\'d like to remove.')
        remflag = 0
        print_teacher_info(0)
        print('\n')
        print('To go back, type 0')
        print('='*60)
        remtid = input('>> ')
        if remtid == '0':
            print_main_menu()
        else:
            for teacher in teacherlist:
                tid = teacher.get_id()
                if remtid == tid:
                    tname = teacher.get_name()
                    tsurname = teacher.get_surname()
                    data.database0.remove_teacher(remtid)
                    print(f'Teacher {tname} {tsurname} successfully removed.')
                    print('\n')
                    input_back_to_menu()
                    remflag = 1
                    break
            if remflag == 0:
                print('There is no teacher with specified ID\n')
                print('='*60)
                input_back_to_menu()


def option4():
    clear()
    print('='*114)
    teacherlist = data.database0.get_allteacherslist()
    if teacherlist == []:
        no_teachers()
    else:
        printbox('Please type the ID of the teacher you\'d like to log in as',
                 112)
        logflag = 0
        print_teacher_info(0)
        printbox(' ', 112)
        printbox('To go back, type 0', 112)
        print('='*114)
        logid = input('>> ')
        if logid == '0':
            print_main_menu()
        else:
            for teacher in teacherlist:
                tid = teacher.get_id()
                if logid == tid:
                    logflag = 1
                    logged_in(teacher)
        if logflag == 0:
            print('There is no teacher with specified ID, cannot log in\n')
            print('='*60)
            input_back_to_menu()


def printbox(text, chars):
    print(f'|{text:^{chars}}|')


def logged_in(teacher):
    tname = teacher.get_name()
    tsurename = teacher.get_surname()
    tid = teacher.get_id()
    clear()
    print('='*60)
    printbox(f'You are logged in as {tname} {tsurename} (id: {tid})', 58)
    print('='*60)
    printbox('What would you like to do?', 58)
    printbox(' ', 58)
    printbox('1. See your plan', 58)
    printbox('2. Add a course', 58)
    printbox('0. Go back to menu', 58)
    print('='*60)
    input_logged_in(teacher)


def input_logged_in(teacher):
    choice = input('>> ')
    if choice == '1':
        clear()
        teacher.print_plan()
        printbox('To go back, type 0', 58)
        print('='*60)
        while choice != '0':
            choice = input('>> ')
        logged_in(teacher)
    elif choice == '2':
        course_creator(teacher)
    elif choice == '0':
        print_main_menu()


def course_creator(teacher):
    clear()
    print('='*60)
    printbox('Welcome to course creator.', 58)
    print('='*60)
    printbox(' ', 58)
    printbox('Please specify unique course id:', 58)
    printbox('(Can not be "0", must be shorter than 20 characters)', 58)
    printbox(' ', 58)
    print('='*60)

    newcid = input_newid('Course')
    clear()
    print('='*60)
    printbox(f'Course\'s chosen ID: {newcid}', 58)
    print('='*60)
    printbox(' ', 58)
    printbox('Please specify course display name:', 58)
    printbox('(max 8 characters long)', 58)
    printbox(' ', 58)
    print('='*60)

    newcdname = input('>> ')
    while len(newcdname) > 8:
        print('Course display name too long, try again.')
        newcdname = input('>> ')
    clear()
    print('='*60)
    printbox(f'Course\'s chosen ID: {newcid}', 58)
    printbox(f'Course\'s chosen display name: {newcdname}', 58)
    print('='*60)
    printbox(' ', 58)
    printbox('Please specify course\'s group number:', 58)
    printbox('(max 3 digits long, must be an integer)', 58)
    printbox(' ', 58)
    print('='*60)

    newcgroup = input_newnumber('Group')
    clear()
    teacher.print_plan()
    print('='*60)
    printbox(f'Course\'s chosen ID: {newcid}', 58)
    printbox(f'Course\'s chosen display name: {newcdname}', 58)
    printbox(f'Course\'s chosen group number: {newcgroup}', 58)
    print('='*60)
    printbox(' ', 58)
    printbox('Please specify course\'s room number:', 58)
    printbox('(max 3 digits long, must be an integer)', 58)
    printbox(' ', 58)
    print('='*60)

    newcroom = input_newnumber('Room')
    clear()
    teacher.print_plan()
    print('='*60)
    printbox(f'Course\'s chosen ID: {newcid}', 58)
    printbox(f'Course\'s chosen display name: {newcdname}', 58)
    printbox(f'Course\'s chosen group number: {newcgroup}', 58)
    printbox(f'Course\'s chosen room number: {newcroom}', 58)
    print('='*60)
    printbox(' ', 58)
    printbox('Specify course\'s start and finish time:', 58)
    printbox('(Format: HH:MM HH:MM e.g. 8:15 10:00)', 58)
    printbox('(Important note: minutes must be a multiple of 15)', 58)
    printbox(' ', 58)
    print('='*60)


def input_newnumber(type):
    value = input('>> ')
    if len(value) > 3:
        print(f'{type} number longer than 3 digits, try again.')
        value = input_newnumber(type)
    else:
        try:
            newnumber = int(value)
            return newnumber
        except ValueError:
            print(f'{type} number is not a number, try again')
            newnumber = input_newnumber(type)
            return newnumber
    return int(value)


def input_newid(type):
    if type == 'Course':
        thelist = data.database0.get_allcourseslist()
    elif type == 'Teacher':
        thelist = data.database0.get_allteacherslist()
    else:
        print('Wrong specified type')
    newcid = input('>> ')
    if not newcid:
        newcid = input_newid(type)
    elif newcid == '0':
        print(f'{type} ID cannot be "0", please choose a different ID.')
        newcid = input_newid(type)
    elif len(newcid) > 20:
        print(f'{type} ID too long, choose a different ID.')
        newcid = input_newid(type)
    else:
        for item in thelist:
            cid = item.get_id()
            if cid == newcid:
                print(f'{type} with this ID already exists, please try again.')
                newcid = input_newid(type)
    return newcid


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
    print('hejka')
    clear()
    print('='*60)
    printbox('Welcome to Course Planner app,', 58)
    printbox(' that will help you plan courses for multiple groups.', 58)
    print('='*60)
    printbox('What would you like to do?', 58)
    printbox(' ', 58)
    printbox('1. See the list of all teachers and their plans', 58)
    printbox('2. Add a new teacher', 58)
    printbox('3. Remove a teacher from database', 58)
    printbox('4. Log in as a teacher', 58)
    printbox('5. Save current data into a file', 58)
    printbox('6. Load data from a file', 58)
    printbox('0. Exit', 58)
    printbox(' ', 58)
    printbox('Input a number 0-6:', 58)
    print('='*60)
    input_and_go_menu()
