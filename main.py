from interface import (print_main_menu,
                       clear)
from classes import Course, TeacherPlan
from data_files import data
from datetime import time


def add_template_teachers():

    course1 = Course('c1', 'mako', 102, '014',
                     time(7, 15), time(9, 0), 'mon')
    course2 = Course('c2', 'anma', 104, '015',
                     time(11, 15), time(12, 0), 'fri')
    course3 = Course('c3', 'mako', 103, '014',
                     time(9, 15), time(11, 0), 'mon')
    course4 = Course('c4', 'mako', 105, '014',
                     time(12, 15), time(14, 0), 'wed')

    teacher1 = TeacherPlan('t1', 'Stan', 'Ban', [course1, course2,
                                                 course3, course4])
    teacher2 = TeacherPlan('t2', 'John', 'Pork', [])

    data.database0.add_teacher(teacher1)
    data.database0.add_teacher(teacher2)


def main():
    clear()
    add_template_teachers()
    print_main_menu()


if __name__ == '__main__':
    main()
