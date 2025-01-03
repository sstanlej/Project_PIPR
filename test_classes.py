from classes import (Course, TeacherPlan,
                     GroupCollisionError, RoomCollisionError)

from all_course_list import allcourselist
from datetime import time


def test_create_course():
    start_time = time(8, 15)
    finish_time = time(10, 0)
    course1 = Course('mako', 104, 's13', start_time, finish_time, 'wednesday')
    assert course1.get_name() == 'mako'
    assert course1.get_group() == 104
    assert course1.get_room() == 's13'
    assert course1.get_start_time() == start_time
    assert course1.get_finish_time() == finish_time
    assert course1.get_day() == 'wednesday'


def test_create_teacherplan():
    start_time1 = time(8, 15)
    finish_time1 = time(10, 0)
    course1 = Course('mako', 104, 's13',
                     start_time1, finish_time1, 'wednesday')
    start_time2 = time(10, 15)
    finish_time2 = time(12, 0)
    course2 = Course('mako', 104, 's13',
                     start_time2, finish_time2, 'wednesday')
    teacherplan1 = TeacherPlan('Jan', 'Ban', [104], [course1, course2])
    assert teacherplan1.get_name() == 'Jan'
    assert teacherplan1.get_surname() == 'Ban'
    courselist = teacherplan1.get_courselist()
    assert courselist[0].get_name() == 'mako'
    assert courselist[1].get_finish_time() == finish_time2
