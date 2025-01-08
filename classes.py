from colorama import Fore
from datetime import time


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
        self._allteacherslist.append(newteacher)
        for course in newteacher.get_courselist():
            self._allcourseslist.append(course)

    def add_course(self, newcourse):
        self._allcourseslist.append(newcourse)

    def remove_teacher(self, oldteacherID):
        for teacher in self._allteacherslist:
            teacherID = teacher.get_id()
            if oldteacherID == teacherID:
                for course in teacher.get_courselist():
                    self.remove_course(course)
                self._allteacherslist.remove(teacher)
                return 0
        raise WrongTeacherIdError("No teacher with specified ID in database.")

    def remove_course(self, oldcourse):
        self._allcourseslist.remove(oldcourse)

    def get_allteacherslist(self):
        return self._allteacherslist

    def get_allcourseslist(self):
        return self._allcourseslist

    def get_alldatalist(self):
        teachers = self._allteacherslist
        courses = self._allcourseslist
        return [teachers, courses]

    def check_room_availability(self, nroom, nday, nstart_time, nfinish_time):
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
    def __init__(self, id, displayname, group,
                 room, start_time, finish_time, day):
        self._id = id
        self._displayname = displayname
        self._group = group
        self._room = room
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
        for course in self._courselist:
            if course.get_id() == courseid:
                self._courselist.remove(course)
                database.remove_course(course)
                return 0
        raise WrongCourseIdError("There is no course with specified ID")

    def print_lineday(self, day, checktime, c):
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
                s = self.print_lineday(day, checktime, c)
                line += s
            print(f'{c}{hr}{c}{line} ')
            minute += 15
            if minute == 60:
                minute = 0
                hour += 1
        print('='*114)
