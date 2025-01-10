from classes import TeacherPlan, Course, InvalidTimeFormat
import json
from datetime import time


class InvalidFileFormat(Exception):
    pass


def read_from_json(filehandle):
    """
    Returns the list of all teachers and courses
    read from a specified file.
    """
    allteacherslist = []
    allcourseslist = []
    data = json.load(filehandle)
    try:
        for item in data:
            tid = item['tid']
            tname = item['tname']
            tsurname = item['tsurname']
            courselist = item['tcourselist']
            tcourselist = []
            for course in courselist:
                cid = course['cid']
                cdname = course['cdname']
                cgroup = course['cgroup']
                croom = course['croom']
                cshour = course['cshour']
                csminute = course['csminute']
                cfhour = course['cfhour']
                cfminute = course['cfminute']
                try:
                    cstime = time(cshour, csminute)
                    cftime = time(cfhour, cfminute)
                except ValueError:
                    raise InvalidTimeFormat('Time format is invalid')
                cday = course['cday']
                newcourse = Course(cid, cdname, cgroup, croom,
                                   cstime, cftime, cday)
                tcourselist.append(newcourse)
            newteacher = TeacherPlan(tid, tname, tsurname, tcourselist)
            allteacherslist.append(newteacher)
        for teacher in allteacherslist:
            for course in teacher.get_courselist():
                if course not in allcourseslist:
                    allcourseslist.append(course)
        return allteacherslist, allcourseslist
    except Exception:
        raise InvalidFileFormat('(teachers)File has invalid format')


def write_to_json(filehandle, alldatalist):
    """
    Saves the specified list of all teacher's and their courses
    to a specified file.
    """
    allteacherslist = []
    for teacher in alldatalist[0]:
        tid = teacher.get_id()
        tname = teacher.get_name()
        tsurname = teacher.get_surname()
        courselist = teacher.get_courselist()
        tcourselist = []
        for course in courselist:
            cid = course.get_id()
            cdname = course.get_displayname()
            cgroup = course.get_group()
            croom = course.get_room()
            stime = course.get_start_time()
            ftime = course.get_finish_time()
            cshour = stime.hour
            csminute = stime.minute
            cfhour = ftime.hour
            cfminute = ftime.minute
            cday = course.get_day()
            jsoncourselist = {
                'cid': cid,
                'cdname': cdname,
                'cgroup': cgroup,
                'croom': croom,
                'cshour': cshour,
                'csminute': csminute,
                'cfhour': cfhour,
                'cfminute': cfminute,
                'cday': cday
            }
            tcourselist.append(jsoncourselist)
        teacher_data = {
            'tid': tid,
            'tname': tname,
            'tsurname': tsurname,
            'tcourselist': tcourselist
        }
        allteacherslist.append(teacher_data)

    data = allteacherslist
    json.dump(data, filehandle, indent=4)
