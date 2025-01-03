from classes import (Course, TeacherPlan,
                     GroupCollisionError, RoomCollisionError,
                     WrongCourseIdError)

from datetime import time
import pytest
from data_lists import allcourselist
import os


def print_list_of_teachers():
    pass


def print_main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('============================================================')
    print('Welcome to Course Planner app,')
    print(' that will help you plan courses for multiple groups.\n')
    print('What do you want to do?\n')
    print('1. See the list of all teachers and their plans')
    choice = input()
    if choice == 1:
        print_list_of_teachers()


print_main_menu()