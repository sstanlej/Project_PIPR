from all_course_list import allcourselist


class Course:
    def __init__(self, name, group, room, start_time, finish_time, day):
        self._name = name
        self._group = group
        self._room = room
        self._start_time = start_time
        self._finish_time = finish_time
        self._day = day
    
    def get_group(self):
        return self._group
    
    def get_room(self):
        return self._group
    
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

    def add_course(self, newcourse):
        for course in allcourselist:

        self._courselist.append(newcourse)
