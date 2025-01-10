from colorama import Fore
from datetime import time


class InvalidTimeFormat(Exception):
    pass


class InvalidGroupNumber(Exception):
    pass


class InvalidRoomNumber(Exception):
    pass


class DisplayNameError(Exception):
    pass


class RoomCollisionError(Exception):
    pass


class NotUniqueTeacherIdError(Exception):
    pass


class GroupCollisionError(Exception):
    pass


class WrongCourseIdError(Exception):
    pass


class WrongDayError(Exception):
    pass


class TeacherCollisionError(Exception):
    pass


class WrongTeacherIdError(Exception):
    pass


class Database():
    """
    Class Database, Contains attributes:
    :param allcourseslist: list of all courses
    :param type: list

    :param allteacherslist: list of all teachers
    :param type: list
    """
    def __init__(self, allcourseslist, allteacherslist):
        if not allcourseslist:
            allcourseslist = []
        self._allcourseslist = allcourseslist
        if not allteacherslist:
            allteacherslist = []
        self._allteacherslist = allteacherslist
        for teacher in self._allteacherslist:
            for course in teacher.get_courselist():
                self._allcourseslist.append(course)

    def add_teacher(self, newteacher):
        """
        Adds specified teacher object to the database.
        """
        self._allteacherslist.append(newteacher)
        for course in newteacher.get_courselist():
            self._allcourseslist.append(course)

    def add_course(self, newcourse):
        """
        Adds specified course object to the database.
        """
        self._allcourseslist.append(newcourse)

    def remove_teacher(self, oldteacherID):
        """
        Removes a teacher object of the specified ID
        from the database.
        """
        for teacher in self._allteacherslist:
            teacherID = teacher.get_id()
            if oldteacherID == teacherID:
                for course in teacher.get_courselist():
                    self.remove_course(course)
                self._allteacherslist.remove(teacher)
                return 0
        raise WrongTeacherIdError("No teacher with specified ID in database.")

    def remove_course(self, oldcourse):
        """
        Removes specified course from the database.
        """
        self._allcourseslist.remove(oldcourse)

    def get_allteacherslist(self):
        """
        Returns the list of all teachers in the database.
        """
        return self._allteacherslist

    def get_allcourseslist(self):
        """
        Returns the list of all courses in the database.
        """
        return self._allcourseslist

    def set_allteacherslist(self, allteacherslist):
        """
        Sets the specified list as the list of all teachers.
        """
        self._allteacherslist = allteacherslist

    def set_allcourseslist(self, allcourseslist):
        """
        Sets the specified list as the list of all courses.
        """
        self._allcourseslist = allcourseslist

    def get_alldatalist(self):
        """
        Returns the list of all teachers and courses in the database.
        """
        teachers = self._allteacherslist
        courses = self._allcourseslist
        return (teachers, courses)

    def check_room_availability(self, nroom, nday, nstart_time, nfinish_time):
        """
        Checks the availability of the specified room
        in the specified day and time period.
        """
        for course in self._allcourseslist:
            day = course.get_day()
            start_time = course.get_start_time()
            finish_time = course.get_finish_time()
            room = course.get_room()
            if nroom == room:
                if nday != day:
                    pass
                elif nstart_time > finish_time:
                    pass
                elif nfinish_time < start_time:
                    pass
                else:
                    return False
        return True

    def check_group_availability(self, ngroup, nday,
                                 nstart_time, nfinish_time):
        """
        Checks the availability of the specified group
        in the specified day and time period.
        """
        for course in self._allcourseslist:
            day = course.get_day()
            start_time = course.get_start_time()
            finish_time = course.get_finish_time()
            group = course.get_group()
            if ngroup == group:
                if nday != day:
                    pass
                elif nstart_time > finish_time:
                    pass
                elif nfinish_time < start_time:
                    pass
                else:
                    return False
        return True


class Course:
    """
    Class Course, Contains attributes:
    :param id: unique id of the course
    :param type: string

    :param displayname: display name of the course
    :param type: string

    :param group: the number of course's group
    :param type: int

    :param room: the number of course's room
    :param type: int

    :param start_time: the start time of the course
    :param type: time

    :param finish_time: the finish time of the course
    :param type: time

    :param day: the day of the course
    :param type: string
    """
    def __init__(self, id, displayname, group,
                 room, start_time, finish_time, day):
        self._id = id
        if len(displayname) > 8:
            raise DisplayNameError("Display name must be under 8 characters")
        self._displayname = displayname
        try:
            int(group)
            self._group = group
        except ValueError:
            raise InvalidGroupNumber("Group is not a number")

        try:
            int(room)
            self._room = room
        except ValueError:
            raise InvalidRoomNumber("Room is not a number")
        self._start_time = start_time
        self._finish_time = finish_time
        self._day = day

    def get_id(self):
        return self._id

    def get_displayname(self):
        return self._displayname

    def get_group(self):
        return self._group

    def get_room(self):
        return self._room

    def get_start_time(self):
        return self._start_time

    def get_finish_time(self):
        return self._finish_time

    def get_day(self):
        return self._day


class TeacherPlan:
    """
    Class TeacherPlan, Contains attributes:
    :param id: unique id of the teacher
    :param type: string

    :param name: the name of the teacher
    :param type: string

    :param surname: the surname of the teacher
    :param type: string

    :param courselist: the list of teacher's courses
    :param type: list
    """
    def __init__(self, id, name, surname, courselist):
        self._id = id
        self._name = name
        self._surname = surname
        if not courselist:
            self._courselist = []
        self._courselist = courselist

    def get_id(self):
        return self._id

    def get_courselist(self):
        return self._courselist

    def get_surname(self):
        return self._surname

    def get_name(self):
        return self._name

    def check_self_availability(self, stime, ftime, day):
        """
        Check availability of the teacher on the specified
        day during specified time.
        """
        for course in self._courselist:
            cstime = course.get_start_time()
            cftime = course.get_finish_time()
            cday = course.get_day()
            if day == cday:
                if stime > cftime:
                    pass
                elif ftime < cstime:
                    pass
                else:
                    return False
        return True

    def add_course(self, newcourse, database):
        """
        Adds specified course to the teacher's course list
        and to the specified databse.
        """
        nday = newcourse.get_day()
        nstart_time = newcourse.get_start_time()
        nfinish_time = newcourse.get_finish_time()
        nroom = newcourse.get_room()
        ngroup = newcourse.get_group()
        if not self.check_self_availability(nstart_time, nfinish_time, nday):
            raise TeacherCollisionError("Teacher is not available at the time")

        if not database.check_room_availability(nroom, nday,
                                                nstart_time, nfinish_time):
            raise RoomCollisionError("Room is not available at the time")
        if not database.check_group_availability(ngroup, nday,
                                                 nstart_time, nfinish_time):
            raise GroupCollisionError("Group is not availavle at the time")
        self._courselist.append(newcourse)
        database.add_course(newcourse)

    def remove_course(self, courseid, database):
        """
        Removes course of specified id from the teacher's course list
        and from the specified databse.
        """
        for course in self._courselist:
            if course.get_id() == courseid:
                self._courselist.remove(course)
                database.remove_course(course)
                return 0
        raise WrongCourseIdError("There is no course with specified ID")

    def get_lineday(self, day, checktime, c):
        """
        Returns a string from the teacher's plan,
        of the specified day and time.
        """
        if self._courselist == []:
            return ' '*20 + c
        for course in self._courselist:
            cday = course.get_day()
            cstime = course.get_start_time()
            cftime = course.get_finish_time()
            cdname = course.get_displayname()
            cgroup = course.get_group()
            croom = course.get_room()
            if cday == day:
                if (checktime >= cstime and checktime < cftime):
                    pname = f'{cdname} g{cgroup} s{croom}'
                    line = Fore.YELLOW + f'{pname:^20}' + Fore.RESET + c
                    break
                else:
                    line = Fore.RESET + ' '*20 + c
            else:
                line = Fore.RESET + ' '*20 + c
        return line

    def print_plan(self):
        """
        Prints the whole teacher's plan.
        """
        days = {
            'mon': '|      MONDAY        ',
            'tue': '|      TUESDAY       ',
            'wed': '|     WEDNESDAY      ',
            'thu': '|     THURSDAY       ',
            'fri': '|      FRIDAY        |'
        }
        print('='*114)
        line = '|       '
        for day in days:
            line += days[day]
        print(line)
        print('='*114)

        hour = 7
        minute = 0
        dz = '00'
        for i in range(0, 65):
            checktime = time(hour, minute)
            hr = f'{checktime.hour}:{checktime.minute if minute != 0 else dz}'
            if len(hr) == 4:
                hr = '  ' + hr + ' '
            else:
                hr = ' ' + hr + ' '
            if minute == 0:
                c = '|'
            else:
                c = '~'
            line = ''
            for day in days:
                s = self.get_lineday(day, checktime, c)
                line += s
            print(f'{c}{hr}{c}{line} ')
            minute += 15
            if minute == 60:
                minute = 0
                hour += 1
        print('='*114)
