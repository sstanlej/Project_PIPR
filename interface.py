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
    """
    Prints the list of all teachers,
    and if printplan == 1 - their plans.
    """

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
    """
    Option 1 from the menu:
    Prints the list of all teachers and their plans.
    """
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
    """
    Option 2 from the menu:
    Teacher creator.
    """
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
    """
    Option 3 from the menu:
    Teacher remover.
    """
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
    """
    Option 4 from the menu:
    Logging in as a teacher.
    """
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
            printbox(['There is no teacher with specified ID, cannot log in'],
                     [], 60)
            input_back_to_menu()


def printline(text, chars):
    """
    Prints a formatted line of text,
    of the lenght specified by chars.
    """
    print(f'|{text:^{chars}}|')


def printbox(title, contents, chars):
    """
    Prints formatted box containing
    title (optionally) and contents,
    of the width specified by chars.
    """
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
    """
    Prints the interface of a logged in teacher.
    """
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
    """
    Takes input and calls the assigned function.
    """
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
    else:
        input_logged_in(teacher)


def course_remover(teacher):
    """
    Removes a specified course from a teacher's plan.
    """
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
                    printbox([f'Course {cdname} (id: {cid}) removed.'], [], 60)
                    go_back_logged_in(teacher)
            if remflag == 0:
                printbox(['There is no course with specified ID.'], [], 60)
                go_back_logged_in(teacher)


def go_back_logged_in(teacher):
    """
    Takes the input until it's 0, and returns to
    the logged in interface.
    """
    printbox(['To go back, type 0.'], [], 60)
    choice = input('>> ')
    while choice != '0':
        choice = input('>> ')
    logged_in(teacher)


def course_creator(teacher):
    """
    New course creator.
    Will not add the course if specified group
    is busy or if the specified
    room is occupied at the specified time.
    """
    clear()
    title1 = 'Welcome to course creator.'
    line1 = 'Please specify unique course id:'
    line2 = '(Can not be "0", must be shorter than 20 characters)'
    printbox([title1], [line1, line2], 60)

    newcid = input_newid('Course')

    clear()
    title1 = f'Course\'s chosen ID: {newcid}'
    line1 = 'Please specify course display name:'
    line2 = '(max 8 characters long)'
    printbox([title1], [line1, line2], 60)

    newcdname = input('>> ')
    while len(newcdname) > 8:
        print('Course display name too long, try again.')
        newcdname = input('>> ')

    clear()
    title2 = f'Course\'s chosen display name: {newcdname}'
    line1 = 'Please specify course\'s group number:'
    line2 = '(max 3 digits long, must be an integer)'
    printbox([title1, title2], [line1, line2], 60)

    newcgroup = input_newnumber('Group')

    clear()
    title3 = f'Course\'s chosen group number: {newcgroup}'
    line1 = 'Please specify course\'s room number:'
    line2 = '(max 3 digits long, must be an integer)'
    teacher.print_plan()
    printbox([title1, title2, title3], [line1, line2], 60)

    newcroom = input_newnumber('Room')

    clear()
    title4 = f'Course\'s chosen room number: {newcroom}'
    line1 = 'Specify course\'s start and finish time:'
    line2 = '(Format: HH:MM HH:MM e.g. 8:15 10:00)'
    line3 = '(Important note: minutes must be a multiple of 15)'
    teacher.print_plan()
    printbox([title1, title2, title3, title4],
             [line1, line2, line3], 60)

    newcstart_time, newcfinish_time = input_newtime()
    shour, sminute = newcstart_time.hour, newcstart_time.minute
    fhour, fminute = newcfinish_time.hour, newcfinish_time.minute

    clear()
    title5 = f'Start time: {shour}:{sminute}'
    title6 = f'Finish time: {fhour}:{fminute}'
    line1 = 'Specify course\'s day:'
    line2 = '(Type one of the following:)'
    line3 = '(mon, tue, wed, thu, fri)'
    teacher.print_plan()
    printbox([title1, title2, title3, title4, title5, title6],
             [line1, line2, line3], 60)

    newcday = input('>> ')
    while newcday not in ('mon', 'tue', 'wed', 'thu', 'fri'):
        print('Wrong specified day, try again.')
        newcday = input('>> ')

    newcourse = Course(newcid, newcdname, newcgroup, newcroom,
                       newcstart_time, newcfinish_time, newcday)

    try:
        teacher.add_course(newcourse, maindatabase)

        clear()
        title7 = f'Course\'s day: {newcday}'
        line1 = 'Course successfully added!'
        teacher.print_plan()
        printbox([title1, title2, title3, title4, title5, title6, title7],
                 [line1], 60)

        go_back_logged_in(teacher)
    except GroupCollisionError:
        printbox(['ERROR'],
                 [f'Group {newcgroup} is busy at specified time.',
                  'Course has not been added.'], 60)

        go_back_logged_in(teacher)
    except TeacherCollisionError:
        tname = teacher.get_name()
        tsurname = teacher.get_surname()
        printbox(['ERROR'],
                 [f'Teacher {tname} {tsurname} is busy at specified time.',
                  'Course has not been added.'], 60)

        go_back_logged_in(teacher)
    except RoomCollisionError:
        printbox(['ERROR'],
                 [f'Room {newcroom} is occupied at specified time.',
                  'Course has not been added.'], 60)

        go_back_logged_in(teacher)


def input_newtime():
    """
    Takes a string from the input and tries to create two time
    variables, tries again if it fails. Correct string format:
    HH:MM HH:MM
    """
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
    """
    Takes a string from input and tries to make a
    3 digit number from it, tries again if fails.
    """
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
    """
    Takes a string from input and tries to create a unique ID
    of a specified type (teacher/course), tries again if fails.
    """
    if type == 'Course':
        thelist = maindatabase.get_allcourseslist()
    elif type == 'Teacher':
        thelist = maindatabase.get_allteacherslist()
    else:
        print('Wrong specified type')
    newid = input('>> ')
    if not newid:
        newid = input_newid(type)
    elif newid == '0':
        print(f'{type} ID cannot be "0", please choose a different ID.')
        newid = input_newid(type)
    elif len(newid) > 20:
        print(f'{type} ID too long, choose a different ID.')
        newid = input_newid(type)
    else:
        for item in thelist:
            id = item.get_id()
            if id == newid:
                print(f'{type} with this ID already exists, please try again.')
                newid = input_newid(type)
    return newid


def option5():
    """
    Option 5 from the menu:
    Saving data into a json file of specified name.
    """
    clear()
    line1 = 'Current data will be save to a .json file.'
    line2 = 'Specify the name of the file you want'
    line3 = 'to save data to (without the .json extension)'
    printbox([line1], [line2, line3], 60)

    file_name = input_file_name(0) + '.json'
    alldatalist = maindatabase.get_alldatalist()
    with open(file_name, 'w') as fp:
        write_to_json(fp, alldatalist)

    line1 = 'Data was saved to:'
    printbox([line1, file_name], [], 60)
    input_back_to_menu()


def option6():
    """
    Option 6 from the menu:
    Loading data from a json file of specified name.
    If file does not exist, prompts back to main menu.
    """
    clear()
    line1 = 'Data will be loaded from a .json file'
    line2 = 'Specify the name of the file you want'
    line3 = 'to load data from (with the .json extension)'
    line4 = '(The file must be inside data_files folder)'
    printbox([line1], [line2, line3, line4], 60)

    file_name = input_file_name(1)
    if file_name is None:
        line1 = 'File with specified name does not exist.'
        printbox([line1], [], 60)
        input_back_to_menu()
    else:
        try:
            with open(file_name, 'r') as fp:
                allteacherslist, allcourseslist = read_from_json(fp)
        except Exception:
            printbox(['File format is invalid.'], [], 60)
            input_back_to_menu()
        maindatabase.set_allcourseslist(allcourseslist)
        maindatabase.set_allteacherslist(allteacherslist)
        line1 = 'Data successfully loaded from:'
        printbox([line1, file_name], [], 60)
        input_back_to_menu()


def input_file_name(checkexists):
    """
    Takes a string from input and adds prefix
    'data_files/' to it.
    If checkexists argument == 1, checks if file
    with specified name exists in the data_files folder.
    """
    file_name = input('>> ')
    while not file_name:
        file_name = input('>> ')
    file_name = 'data_files/' + file_name
    if checkexists == 1:
        if not os.path.exists(file_name):
            return None
    return file_name


def no_teachers():
    """
    Prints information that there are no
    teachers in the database.
    """
    printbox(0, ['There are no teachers in the database.',
                 'Would you like to add a new teacher?',
                 ' ',
                 'Y - Yes',
                 'N - Go back to main menu'], 60)
    input_and_go_addT()


def input_back_to_menu():
    """
    Takes string from input until it is '0',
    and prompts back to main menu.
    """
    printbox(['To go back to menu, type 0'], [], 60)
    choice = input('>> ')
    if choice == '0':
        print_main_menu()
    else:
        input_back_to_menu()


def wrong_input_menu():
    """
    Prints information that the input is wrong,
    and takes input again.
    """
    print("Wrong input, please input a number from 0 to 6")
    input_and_go_menu()


def wrong_inputYN():
    """
    Prints information that the input is wrong,
    and takes input again.
    """
    print("Wrong input, please input Y or N")
    input_and_go_addT()


def input_and_go_addT():
    """
    Takes string as input until it is 'Y' or 'N',
    and calls corresponding function.
    """
    choice = input('>> ')
    if choice == 'Y':
        option2()
    elif choice == 'N':
        print_main_menu()
    else:
        wrong_inputYN()


def input_and_go_menu():
    """
    Takes string as input until it is a number from 0 to 6,
    and calls corresponding function.
    """
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
    """
    Prints the main menu.
    """
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
