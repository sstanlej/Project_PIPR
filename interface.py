import os
from data_files import data
from classes import (TeacherPlan, Course,
                     GroupCollisionError,
                     TeacherCollisionError,
                     RoomCollisionError)
from datetime import time


def clear():
    os.system('cls')


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
    printbox('Welcome to teacher creator.', 58)
    print('='*60)
    printbox(' ', 58)
    printbox('Please specify unique teacher id:', 58)
    printbox('(Can not be "0", must be shorter than 20 characters)', 58)
    printbox(' ', 58)
    print('='*60)

    newtid = input_newid('Teacher')

    clear()
    print('='*60)
    printbox(f'Teacher\'s chosen ID: {newtid}', 58)
    print('='*60)
    printbox(' ', 58)
    printbox('Please specify teacher\'s name:', 58)
    printbox(' ', 58)
    print('='*60)

    newtname = input('>> ')
    while not newtname:
        newtname = input('>> ')

    clear()
    print('='*60)
    printbox(f'Teacher\'s chosen ID: {newtid}', 58)
    printbox(f'Teacher\'s chosen name: {newtname}', 58)
    print('='*60)
    printbox(' ', 58)
    printbox('Please specify teacher\'s surname:', 58)
    printbox(' ', 58)
    print('='*60)

    newtsurname = input('>> ')
    while not newtsurname:
        newtsurname = input('>> ')

    clear()
    print('='*60)
    printbox(f'Teacher\'s chosen ID: {newtid}', 58)
    printbox(f'Teacher\'s chosen name: {newtname}', 58)
    printbox(f'Teacher\'s chosen surname: {newtsurname}', 58)
    print('='*60)

    newteacher = TeacherPlan(newtid, newtname,
                             newtsurname, [])
    data.database0.add_teacher(newteacher)

    printbox(' ', 58)
    printbox(f'Teacher {newtname} {newtsurname} succesfully created!', 58)
    printbox(' ', 58)
    print('='*60)
    input_back_to_menu()


def option3():
    clear()
    teacherlist = data.database0.get_allteacherslist()
    if teacherlist == []:
        print('='*60)
        printbox('There are no teachers in the database.', 58)
        print('='*60)
        input_back_to_menu()
    else:
        print('='*114)
        printbox('Please type the ID of the teacher you\'d like to remove.',
                 112)
        print('='*114)
        remflag = 0
        print_teacher_info(0)
        printbox(' ', 112)
        printbox('To go back, type 0', 112)
        print('='*114)
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
    printbox('3. Remove a course', 58)
    printbox('0. Go back to menu', 58)
    print('='*60)
    input_logged_in(teacher)


def input_logged_in(teacher):
    choice = input('>> ')
    if choice == '1':
        clear()
        teacher.print_plan()
        go_back_logged_in(teacher)
    elif choice == '2':
        course_creator(teacher)
    elif choice == '3':
        course_remover(teacher)
    elif choice == '0':
        print_main_menu()


def course_remover(teacher):
    clear()
    courselist = teacher.get_courselist()
    tname = teacher.get_name()
    tsurname = teacher.get_surname()
    if courselist == []:
        print('='*60)
        printbox(f'Teacher {tname} {tsurname} has no courses planned.', 58)
        print('='*60)
        go_back_logged_in(teacher)
    else:
        print('='*80)
        printbox(f'The list of {tname} {tsurname}\'s courses:', 78)
        print('='*80)
        x = 1
        for course in courselist:
            cdname = course.get_displayname()
            cid = course.get_id()
            cgroup = course.get_group()
            croom = course.get_room()
            days = {
                'mon': 'Monday',
                'tue': 'Tuesday',
                'wed': 'Wednesday',
                'thu': 'Thursday',
                'fri': 'Friday'
            }
            cday = days[course.get_day()]
            cstime = course.get_start_time()
            cftime = course.get_finish_time()
            cshour, csminute = cstime.hour, cstime.minute
            cfhour, cfminute = cftime.hour, cftime.minute
            printbox(f'{x}. {cdname} (id: {cid})', 78)
            printbox(f'Group: {cgroup}, Room: {croom}', 78)
            printbox(f'Time: {cday} {cshour}:{csminute}-{cfhour}:{cfminute}',
                     78)
            printbox(' ', 78)
            x += 1
        printbox(' ', 78)
        printbox('Type the ID of the course you\'d like to remove.', 78)
        printbox('(To go back, type 0)', 78)
        print('='*80)
        remcid = input('>> ')
        if remcid == '0':
            logged_in(teacher)
        else:
            remflag = 0
            for course in courselist:
                cid = course.get_id()
                if remcid == cid:
                    remflag = 1
                    teacher.remove_course(cid, data.database0)
                    cdname = course.get_displayname()
                    cid = course.get_id()
                    print('='*60)
                    printbox(f'Course {cdname} (id: {cid}) removed.', 58)
                    go_back_logged_in(teacher)
            if remflag == 0:
                print('='*60)
                printbox('There is no course with specified ID.', 58)
                go_back_logged_in(teacher)


def go_back_logged_in(teacher):
    printbox('To go back, type 0', 58)
    print('='*60)
    choice = input('>> ')
    while choice != '0':
        choice = input('>> ')
    logged_in(teacher)


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

    newcstart_time, newcfinish_time = input_newtime()
    shour, sminute = newcstart_time.hour, newcstart_time.minute
    fhour, fminute = newcfinish_time.hour, newcfinish_time.minute

    clear()
    teacher.print_plan()
    print('='*60)
    printbox(f'Course\'s chosen ID: {newcid}', 58)
    printbox(f'Course\'s chosen display name: {newcdname}', 58)
    printbox(f'Course\'s chosen group number: {newcgroup}', 58)
    printbox(f'Course\'s chosen room number: {newcroom}', 58)
    printbox(f'Start time: {shour}:{sminute}', 58)
    printbox(f'Finish time: {fhour}:{fminute}', 58)
    print('='*60)
    printbox(' ', 58)
    printbox('Specify course\'s day:', 58)
    printbox('(Type one of the following:)', 58)
    printbox('(mon, tue, wed, thu, fri)', 58)
    printbox(' ', 58)
    print('='*60)

    newcday = input('>> ')
    while newcday not in ('mon', 'tue', 'wed', 'thu', 'fri'):
        print('Wrong specified day, try again.')
        newcday = input('>> ')

    newcourse = Course(newcid, newcdname, newcgroup, newcroom,
                       newcstart_time, newcfinish_time, newcday)

    try:
        teacher.add_course(newcourse, data.database0)
        clear()
        teacher.print_plan()
        print('='*60)
        printbox(f'Course\'s chosen ID: {newcid}', 58)
        printbox(f'Course\'s chosen display name: {newcdname}', 58)
        printbox(f'Course\'s chosen group number: {newcgroup}', 58)
        printbox(f'Course\'s chosen room number: {newcroom}', 58)
        printbox(f'Start time: {shour}:{sminute}', 58)
        printbox(f'Finish time: {fhour}:{fminute}', 58)
        printbox(f'Course\'s day: {newcday}', 58)
        print('='*60)
        printbox('Course successfully added!', 58)
        print('='*60)
        go_back_logged_in(teacher)
    except GroupCollisionError:
        printbox('ERROR:', 58)
        printbox(f'Group {newcgroup} is busy at specified time.', 58)
        printbox('Course has not been added.', 58)
        print('='*60)
        go_back_logged_in(teacher)
    except TeacherCollisionError:
        printbox('ERROR:', 58)
        tname = teacher.get_name()
        tsurname = teacher.get_surname()
        printbox(f'Teacher {tname} {tsurname} is busy at specified time.', 58)
        printbox('Course has not been added.', 58)
        print('='*60)
        go_back_logged_in(teacher)
    except RoomCollisionError:
        printbox('ERROR:', 58)
        printbox(f'Room {newcroom} is occupied at specified time.', 58)
        printbox('Course has not been added.', 58)
        print('='*60)
        go_back_logged_in(teacher)


def input_newtime():
    value = input('>> ')
    try:
        stime, ftime = value.split()
    except ValueError:
        print('No space between start and finish time, try again.')
        start_time, finish_time = input_newtime()
        return start_time, finish_time

    try:
        shour, sminute = stime.split(':')
        fhour, fminute = ftime.split(':')
    except ValueError:
        print('Incorrect time format, try again.')
        start_time, finish_time = input_newtime()
        return start_time, finish_time

    try:
        shour = int(shour)
        sminute = int(sminute)
        fhour = int(fhour)
        fminute = int(fminute)
    except ValueError:
        print('Incorrect time format, try again.')
        start_time, finish_time = input_newtime()
        return start_time, finish_time

    if not (sminute % 15 == 0 and fminute % 15 == 0):
        print('Minutes value must be a multiple of 15, try again.')
        start_time, finish_time = input_newtime()
        return start_time, finish_time

    try:
        start_time = time(shour, sminute)
        finish_time = time(fhour, fminute)
    except ValueError:
        print('Incorrect time format, try again.')
        start_time, finish_time = input_newtime()
        return start_time, finish_time

    if not finish_time > start_time:
        print('Start time must be smaller than finish time, try again.')
        start_time, finish_time = input_newtime()
        return start_time, finish_time

    if not (start_time >= time(7, 0) and finish_time <= time(23, 0)):
        print('Course must take place between 7:00 and 23:00')
        start_time, finish_time = input_newtime()
        return start_time, finish_time

    return start_time, finish_time


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
