from all_course_list import allcourselist


class RoomCollisionError(Exception):
    pass


class GroupCollisionError(Exception):
    pass


class Course:
    def __init__(self, name, group, room, start_time, finish_time, day):
        self._name = name
        self._group = group
        self._room = room
        self._start_time = start_time
        self._finish_time = finish_time
        self._day = day

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

    def check_room_availability(self, nroom, nday, nstart_time, nfinish_time):
        for course in allcourselist:
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
        for course in allcourselist:
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

    def add_course(self, newcourse):
        nday = newcourse.get_day()
        nstart_time = newcourse.get_start_time()
        nfinish_time = newcourse.get_finish_time()
        nroom = newcourse.get_room()
        ngroup = newcourse.get_group()
        if not self.check_room_availability(nroom, nday,
                                            nstart_time, nfinish_time):
            raise RoomCollisionError("Room is not available at the time")
        if not self.check_group_availability(ngroup, nday,
                                             nstart_time, nfinish_time):
            raise GroupCollisionError("Group is not availavle at the time")
        self._courselist.append(newcourse)
        allcourselist.append(newcourse)
