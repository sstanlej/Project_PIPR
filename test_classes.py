from classes import (Course, TeacherPlan,
                     GroupCollisionError, RoomCollisionError)

from datetime import time
import pytest


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


def test_add_course():
    start_time1 = time(8, 15)
    finish_time1 = time(10, 0)
    course1 = Course('mako', 104, 's13',
                     start_time1, finish_time1, 'wednesday')
    start_time2 = time(10, 15)
    finish_time2 = time(12, 0)
    course2 = Course('mako', 104, 's13',
                     start_time2, finish_time2, 'wednesday')
    teacherplan1 = TeacherPlan('Jan', 'Ban', [104], [])
    teacherplan1.add_course(course1)
    courselist = teacherplan1.get_courselist()
    assert courselist[0].get_name() == 'mako'
    teacherplan1.add_course(course2)
    courselist = teacherplan1.get_courselist()
    assert courselist[1].get_finish_time() == finish_time2


def test_course_collision():
    start_time1 = time(8, 15)
    finish_time1 = time(10, 0)
    start_time2 = time(9, 15)
    finish_time2 = time(11, 0)

    course1 = Course('mako', 104, 's13',
                     start_time1, finish_time1, 'wednesday')
    course2 = Course('mako', 104, 's14',
                     start_time2, finish_time2, 'wednesday')
    course3 = Course('anma', 108, 's13',
                     start_time1, finish_time1, 'wednesday')

    teacherplan1 = TeacherPlan('Jan', 'Ban', [104], [])
    teacherplan1.add_course(course1)
    courselist = teacherplan1.get_courselist()
    assert courselist[0].get_name() == 'mako'
    with pytest.raises(GroupCollisionError):
        teacherplan1.add_course(course2)
    teacherplan2 = TeacherPlan('San', 'Tan', [108], [])
    with pytest.raises(RoomCollisionError):
        teacherplan2.add_course(course3)
