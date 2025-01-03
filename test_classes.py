from classes import (Course, TeacherPlan,
                     GroupCollisionError, RoomCollisionError)

from all_course_list import allcourselist
from datetime import time


def test_create_course():
    start_time = time(8, 0)
    finish_time = time(10, 0)
    course1 = Course('mako', 104, 's13', start_time, finish_time, 'wednesday')
    assert course1.get_name() == 'mako'
    assert course1.get_group() == 104
    assert course1.get_room() == 's13'
    assert course1.get_start_time() == start_time
    assert course1.get_finish_time() == finish_time
    assert course1.get_day() == 'wednesday'
