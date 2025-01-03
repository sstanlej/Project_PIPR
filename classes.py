from all_course_list import allcourselist


class Course:
    def __init__(self, name, group, room, start_time, finish_time, day):
        self._name = name
        self._group = group
        self._room = room
        self._start_time = start_time
        self._finish_time = finish_time
        self._day = day


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

    def add_course(self, course):
        self._courselist.append(course)
