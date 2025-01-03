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
        self._grouplist = grouplist
        self._courselist = courselist