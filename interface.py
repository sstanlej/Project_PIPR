import os
from datetime import time
from data_handler import write_to_json, read_from_json
from classes import (Database, TeacherPlan, Course,
                     GroupCollisionError,
                     TeacherCollisionError,
                     RoomCollisionError)


maindatabase = Database([], [])


def clear():
    os.system('cls')


def print_teachers_info(printplan):
    teacherlist = maindatabase.get_allteacherslist()
    x = 1
    for teacher in teacherlist:
        tname = teacher.get_name()
        tsurname = teacher.get_surname()
        tid = teacher.get_id()
        line = f'{x}. {tname} {tsurname} (id: {tid})'
        printline(line, 112)
        if printplan == 1:
            if teacher.get_courselist() == []:
                printline('This teacher has no courses planned.', 112)
                printline(' ', 112)
                printline(' ', 112)
            else:
                printline('Teacher plan:', 112)
                teacher.print_plan()
                printline(' ', 112)
                printline(' ', 112)
        x += 1


def option1():
    clear()
    teacherlist = maindatabase.get_allteacherslist()
    if teacherlist == []:
        no_teachers()
    else:
        print('='*114)
        printline('The list of all teachers:', 112)
        print('='*114)
        printline(' ', 112)
        print_teachers_info(1)
        print('='*114)
        input_back_to_menu()


def option2():
    clear()
    printbox(['Welcome to teacher creator'],
             ['Please specify unique teacher id:',
              '(Can not be "0", must be shorter than 20 characters)'], 60)

    newtid = input_newid('Teacher')
    line1 = f'Teacher\'s chosen ID: {newtid}'

    clear()
    printbox([line1],
             ['Please specify teacher\'s name:'], 60)

    newtname = input('>> ')
    while not newtname:
        newtname = input('>> ')
    line2 = f'Teacher\'s chosen name: {newtname}'

    clear()
    printbox([line1, line2],
             ['Please specify teacher\'s surname:'], 60)

    newtsurname = input('>> ')
    while not newtsurname:
        newtsurname = input('>> ')
    line3 = f'Teacher\'s chosen surname: {newtsurname}'

    newteacher = TeacherPlan(newtid, newtname,
                             newtsurname, [])
    maindatabase.add_teacher(newteacher)

    clear()
    printbox([line1, line2, line3],
             [f'Teacher {newtname} {newtsurname} succesfully created!'], 60)

    input_back_to_menu()


def option3():
    clear()
    teacherlist = maindatabase.get_allteacherslist()
    if teacherlist == []:
        no_teachers()
    else:
        print('='*114)
        printline('Please type the ID of the teacher you\'d like to remove.',
                  112)
        print('='*114)
        remflag = 0
        print_teachers_info(0)
        printline(' ', 112)
        printline('To go back, type 0', 112)
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
                    maindatabase.remove_teacher(remtid)
                    print(f'Teacher {tname} {tsurname} successfully removed.')
                    print('\n')
                    input_back_to_menu()
                    remflag = 1
                    break
            if remflag == 0:
                print('There is no teacher with specified ID\n')
                input_back_to_menu()


def option4():
    clear()
    teacherlist = maindatabase.get_allteacherslist()
    if teacherlist == []:
        no_teachers()
    else:
        print('='*114)
        printline('Please type the ID of the teacher you\'d like to log in as',
                  112)
        logflag = 0
        print_teachers_info(0)
        printline(' ', 112)
        printline('To go back, type 0', 112)
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


def printline(text, chars):
    print(f'|{text:^{chars}}|')


def printbox(title, contents, chars):
    if not title == 0:
        print('='*chars)
        for item in title:
            print(f'|{item:^{chars-2}}|')
    print('='*chars)
    if contents == []:
        return
    space = ' '
    print(f'|{space:^{chars-2}}|')
    for item in contents:
        print(f'|{item:^{chars-2}}|')
    print(f'|{space:^{chars-2}}|')
    print('='*chars)


def logged_in(teacher):
    tname = teacher.get_name()
    tsurename = teacher.get_surname()
    tid = teacher.get_id()
    clear()
    printbox([f'You are logged in as {tname} {tsurename} (id: {tid})'],
             ['What would you like to do?',
              ' ',
              '1. See your plan',
              '2. Add a course',
              '3. Remove a course',
              '0. Go back to menu'], 60)
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
        printbox([f'Teacher {tname} {tsurname} has no courses planned.'],
                 [], 60)
        go_back_logged_in(teacher)
    else:
        line1 = f'The list of {tname} {tsurname}\'s courses:'
        lines = []
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

            line2 = f'{x}. {cdname} (id: {cid})'
            line3 = f'Group: {cgroup}, Room: {croom}'
            line4 = f'Time: {cday} {cshour}:{csminute}-{cfhour}:{cfminute}'
            line5 = ' '
            lines.append(line2)
            lines.append(line3)
            lines.append(line4)
            lines.append(line5)
            x += 1
        lines.append(' ')
        lines.append('Type the ID of the course you\'d like to remove.')
        lines.append('(To go back, type 0)')
        printbox([line1], lines, 80)

        remcid = input('>> ')
        if remcid == '0':
            logged_in(teacher)
        else:
            remflag = 0
            for course in courselist:
                cid = course.get_id()
                if remcid == cid:
                    remflag = 1
                    teacher.remove_course(cid, maindatabase)
                    cdname = course.get_displayname()
                    cid = course.get_id()
                    print('='*60)
                    printline(f'Course {cdname} (id: {cid}) removed.', 58)
                    go_back_logged_in(teacher)
            if remflag == 0:
                print('='*60)
                printline('There is no course with specified ID.', 58)
                go_back_logged_in(teacher)


def go_back_logged_in(teacher):
    printline('To go back, type 0', 58)
    print('='*60)
    choice = input('>> ')
    while choice != '0':
        choice = input('>> ')
    logged_in(teacher)


def course_creator(teacher):
    clear()
    print('='*60)
    printline('Welcome to course creator.', 58)
    print('='*60)
    printline(' ', 58)
    printline('Please specify unique course id:', 58)
    printline('(Can not be "0", must be shorter than 20 characters)', 58)
    printline(' ', 58)
    print('='*60)

    newcid = input_newid('Course')
    clear()
    print('='*60)
    printline(f'Course\'s chosen ID: {newcid}', 58)
    print('='*60)
    printline(' ', 58)
    printline('Please specify course display name:', 58)
    printline('(max 8 characters long)', 58)
    printline(' ', 58)
    print('='*60)

    newcdname = input('>> ')
    while len(newcdname) > 8:
        print('Course display name too long, try again.')
        newcdname = input('>> ')
    clear()
    print('='*60)
    printline(f'Course\'s chosen ID: {newcid}', 58)
    printline(f'Course\'s chosen display name: {newcdname}', 58)
    print('='*60)
    printline(' ', 58)
    printline('Please specify course\'s group number:', 58)
    printline('(max 3 digits long, must be an integer)', 58)
    printline(' ', 58)
    print('='*60)

    newcgroup = input_newnumber('Group')
    clear()
    teacher.print_plan()
    print('='*60)
    printline(f'Course\'s chosen ID: {newcid}', 58)
    printline(f'Course\'s chosen display name: {newcdname}', 58)
    printline(f'Course\'s chosen group number: {newcgroup}', 58)
    print('='*60)
    printline(' ', 58)
    printline('Please specify course\'s room number:', 58)
    printline('(max 3 digits long, must be an integer)', 58)
    printline(' ', 58)
    print('='*60)

    newcroom = input_newnumber('Room')
    clear()
    teacher.print_plan()
    print('='*60)
    printline(f'Course\'s chosen ID: {newcid}', 58)
    printline(f'Course\'s chosen display name: {newcdname}', 58)
    printline(f'Course\'s chosen group number: {newcgroup}', 58)
    printline(f'Course\'s chosen room number: {newcroom}', 58)
    print('='*60)
    printline(' ', 58)
    printline('Specify course\'s start and finish time:', 58)
    printline('(Format: HH:MM HH:MM e.g. 8:15 10:00)', 58)
    printline('(Important note: minutes must be a multiple of 15)', 58)
    printline(' ', 58)
    print('='*60)

    newcstart_time, newcfinish_time = input_newtime()
    shour, sminute = newcstart_time.hour, newcstart_time.minute
    fhour, fminute = newcfinish_time.hour, newcfinish_time.minute

    clear()
    teacher.print_plan()
    print('='*60)
    printline(f'Course\'s chosen ID: {newcid}', 58)
    printline(f'Course\'s chosen display name: {newcdname}', 58)
    printline(f'Course\'s chosen group number: {newcgroup}', 58)
    printline(f'Course\'s chosen room number: {newcroom}', 58)
    printline(f'Start time: {shour}:{sminute}', 58)
    printline(f'Finish time: {fhour}:{fminute}', 58)
    print('='*60)
    printline(' ', 58)
    printline('Specify course\'s day:', 58)
    printline('(Type one of the following:)', 58)
    printline('(mon, tue, wed, thu, fri)', 58)
    printline(' ', 58)
    print('='*60)

    newcday = input('>> ')
    while newcday not in ('mon', 'tue', 'wed', 'thu', 'fri'):
        print('Wrong specified day, try again.')
        newcday = input('>> ')

    newcourse = Course(newcid, newcdname, newcgroup, newcroom,
                       newcstart_time, newcfinish_time, newcday)

    try:
        teacher.add_course(newcourse, maindatabase)
        clear()
        teacher.print_plan()
        print('='*60)
        printline(f'Course\'s chosen ID: {newcid}', 58)
        printline(f'Course\'s chosen display name: {newcdname}', 58)
        printline(f'Course\'s chosen group number: {newcgroup}', 58)
        printline(f'Course\'s chosen room number: {newcroom}', 58)
        printline(f'Start time: {shour}:{sminute}', 58)
        printline(f'Finish time: {fhour}:{fminute}', 58)
        printline(f'Course\'s day: {newcday}', 58)
        print('='*60)
        printline('Course successfully added!', 58)
        print('='*60)
        go_back_logged_in(teacher)
    except GroupCollisionError:
        printline('ERROR:', 58)
        printline(f'Group {newcgroup} is busy at specified time.', 58)
        printline('Course has not been added.', 58)
        print('='*60)
        go_back_logged_in(teacher)
    except TeacherCollisionError:
        printline('ERROR:', 58)
        tname = teacher.get_name()
        tsurname = teacher.get_surname()
        printline(f'Teacher {tname} {tsurname} is busy at specified time.', 58)
        printline('Course has not been added.', 58)
        print('='*60)
        go_back_logged_in(teacher)
    except RoomCollisionError:
        printline('ERROR:', 58)
        printline(f'Room {newcroom} is occupied at specified time.', 58)
        printline('Course has not been added.', 58)
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
        thelist = maindatabase.get_allcourseslist()
    elif type == 'Teacher':
        thelist = maindatabase.get_allteacherslist()
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
    printline('Current data will be save to a .json file.', 58)
    printline('Specify the name of the file you want', 58)
    printline('to save data to (without the .json extension)', 58)
    print('='*60)
    file_name = input('>> ')
    while len(file_name) > 15:
        print('File name too long, try again.')
        file_name = input('>> ')
    file_name = 'data_files/' + file_name + '.json'

    alldatalist = maindatabase.get_alldatalist()

    with open(file_name, 'w') as fp:
        write_to_json(fp, alldatalist)

    print('='*60)
    printline(f'Data was saved to {file_name}', 58)
    print('='*60)

    input_back_to_menu()


def option6():
    clear()
    line1 = 'Data will be loaded from a .json file'
    line2 = 'Specify the name of the file you want'
    line3 = 'to load data from (with the .json extension)'
    line4 = '(The file must be inside data_files folder)'
    printbox([line1], [line2, line3, line4], 60)
    file_name = input('>> ')
    while not file_name:
        file_name = input('>> ')
    file_name = 'data_files/' + file_name
    if not os.path.exists(file_name):
        printline(f'{file_name} does not exist.', 58)
        print('='*60)
        input_back_to_menu()
    else:
        with open(file_name, 'r') as fp:
            allteacherslist, allcourseslist = read_from_json(fp)
        maindatabase.set_allcourseslist(allcourseslist)
        maindatabase.set_allteacherslist(allteacherslist)
        printline('Data successfully loaded', 58)
        printline(f'from {file_name}', 58)
        print('='*60)
        input_back_to_menu()


def no_teachers():
    printbox(0, ['There are no teachers in the database.',
                 'Would you like to add a new teacher?',
                 ' ',
                 'Y - Yes',
                 'N - Go back to main menu'], 60)
    input_and_go_addT()


def input_back_to_menu():
    printbox(['To go back to menu, type 0'], [], 60)
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
    elif choice == 'secret':
        secretmenu()
    else:
        wrong_input_menu()


def secretmenu():
    print('Database allcourselist:')
    for course in maindatabase._allcourseslist:
        print(course.get_id(), course)
    print('\nDatabase allteacherslist:')
    for teacher in maindatabase._allteacherslist:
        print(teacher.get_id(), teacher)
    input_back_to_menu()


def print_main_menu():
    clear()
    line1 = 'Welcome to Course Planner app,'
    line2 = ' that will help you plan courses for multiple groups.'
    line3 = 'What would you like to do?'
    line4 = ' '
    line5 = '1. See the list of all teachers and their plans'
    line6 = '2. Add a new teacher'
    line7 = '3. Remove a teacher from database'
    line8 = '4. Log in as a teacher'
    line9 = '5. Save current data into a file'
    line10 = '6. Load data from a file'
    line11 = '0. Exit'
    line12 = ' '
    line13 = 'Input a number 0-6:'
    printbox([line1, line2],
             [line3, line4, line5, line6,
              line7, line8, line9, line10,
              line11, line12, line13], 60)
    input_and_go_menu()
