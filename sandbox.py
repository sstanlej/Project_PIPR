from classes import Database, TeacherPlan, Course
from datetime import time

database0 = Database([], [])

teacher1 = TeacherPlan('Stan', 'Ban', [101, 102, 103, 105], [])
teacher2 = TeacherPlan('John', 'Pork', [101, 102, 103, 104, 105, 108], [])

database0.add_teacher(teacher1)
database0.add_teacher(teacher2)

course1 = Course(0, 'mako', 102, 's14', time(7, 15), time(9, 0), 'mon')
course2 = Course(1, 'anma', 104, 's15', time(11, 15), time(12, 0), 'fri')
course3 = Course(2, 'mako', 103, 's14', time(9, 15), time(11, 0), 'mon')
course4 = Course(3, 'mako', 105, 's14', time(12, 15), time(14, 0), 'wed')


teacher1.add_course(course1, database0)
teacher1.add_course(course2, database0)
teacher1.add_course(course3, database0)
teacher1.add_course(course4, database0)

print('\n\n\n')
# teacher1.print_plan()
time1 = '8:77 10:00'
start, finish = time1.split()
starth, startm = start.split(':')
finishh, finishm = finish.split(':')
starth = int(starth)
startm = int(startm)
finishh = int(finishh)
finishm = int(finishm)
start_time = time(starth, startm)
finish_time = time(finishh, finishm)
print(start_time)
print(finish_time)
