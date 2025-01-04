from classes import Database, TeacherPlan, Course
from datetime import time

database0 = Database([], [])

teacher1 = TeacherPlan('Stan', 'Ban', [101, 102, 103, 105], [])
teacher2 = TeacherPlan('John', 'Pork', [101, 102, 103, 104, 105, 108], [])

database0.add_teacher(teacher1)
database0.add_teacher(teacher2)

time1 = time(8, 15)
time2 = time(10, 0)
time3 = time(10, 15)
time4 = time(12, 0)

course1 = Course(0, 'mako1', 102, 's14', time1, time2, 'wed')
course2 = Course(1, 'anma1', 102, 's15', time3, time4, 'wed')

teacher1.add_course(course1, database0)
teacher2.add_course(course2, database0)

teacher1.print_plan('wed')
