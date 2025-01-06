from colorama import Fore, Style
from datetime import time


class RoomCollisionError(Exception):
    pass


class GroupCollisionError(Exception):
    pass


class WrongCourseIdError(Exception):
    pass


class Database():
    def __init__(self, allcourseslist, allteacherslist):
        if not allcourseslist:
            allcourseslist = []
        self._allcourseslist = allcourseslist
        if not allteacherslist:
            allteacherslist = []
        self._allteacherslist = allteacherslist

    def add_teacher(self, newteacher):
        self._allteacherslist.append(newteacher)

    def add_course(self, newcourse):
        self._allcourseslist.append(newcourse)

    def remove_course(self, oldcourse):
        self._allcourseslist.remove(oldcourse)

    def get_allteacherslist(self):
        return self._allteacherslist

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
    def __init__(self, id, name, group, room, start_time, finish_time, day):
        self._id = id
        self._name = name
        self._group = group
        self._room = room
        self._start_time = start_time
        self._finish_time = finish_time
        self._day = day

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

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
    def __init__(self, name, surname, grouplist, courselist):
        self._name = name
        self._surname = surname
        if not grouplist:
            self._grouplist = []
        self._grouplist = grouplist
        if not courselist:
            self._courselist = []
        self._courselist = courselist

    def get_courselist(self):
        return self._courselist

    def get_grouplist(self):
        return self._grouplist

    def get_surname(self):
        return self._surname

    def get_name(self):
        return self._name

    def add_course(self, newcourse, database):
        nday = newcourse.get_day()
        nstart_time = newcourse.get_start_time()
        nfinish_time = newcourse.get_finish_time()
        nroom = newcourse.get_room()
        ngroup = newcourse.get_group()

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

    def print_plan(self, day):
        if day == 'mon':
            printday = '=     MONDAY       ='
        elif day == 'tue':
            printday = '=     TUESDAY      ='
        elif day == 'wed':
            printday = '=    WEDNESDAY     ='
        elif day == 'thu':
            printday = '=    THURSDAY      ='
        elif day == 'fri':
            printday = '=     FRIDAY       ='
        else:
            printday = 'wrongday'
        print('='*20)
        print(printday)
        print('='*20)
        hour = 7
        minute = 0
        dz = '00'
        last_cid = -1
        for i in range(0, 64):
            checktime = time(hour, minute)
            ph = f'{checktime.hour}:{checktime.minute if minute != 0 else dz}'
            if len(ph) == 4:
                ph = '  ' + ph
            else:
                ph = ' ' + ph
            for course in self._courselist:
                cday = course.get_day()
                cstime = course.get_start_time()
                cftime = course.get_finish_time()
                cid = course.get_id()
                cname = course.get_name()
                cgroup = course.get_group()
                if cday == day:
                    if (checktime >= cstime and checktime < cftime):
                        if last_cid == cid:
                            line = Fore.RED + f'{ph} {cname}{cgroup}'
                            last_cid = cid
                            break
                        else:
                            line = Fore.YELLOW + f'{ph} {cname}{cgroup}'
                            last_cid = cid
                            break
                    else:
                        line = Fore.RESET + ph
                else:
                    line = Fore.RESET + ph
            print(line)
            minute += 15
            if minute == 60:
                minute = 0
                hour += 1
