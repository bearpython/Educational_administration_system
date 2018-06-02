#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# Author:bear

import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

class School(object):
    '''
    基础的学校类，学校信息
    提供学员注册、老师入职等功能
    '''
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staffs = []
        self.courses = []
        self.grades = []

    def creat_course(self,course_obj):
        self.courses.append(course_obj)
        print("您创建了新的课程：%s" %course_obj.name)

    def creat_grade(self,grade_obj):
        self.grades.append(grade_obj)
        print("您创建了新的班级：%s" %grade_obj.name)

    def enroll(self,stu_obj):
        print("为%s学员办理注册手续" % stu_obj.name)
        self.students.append(stu_obj)

    def hire(self,staff_obj):
        print("雇佣了%s新员工" % staff_obj.name)
        self.staffs.append(staff_obj)

class SchoolMember(object):
    '''学校里的人，包括老师、学生'''
    def __init__(self,name,age,sex,sch_name):
        self.name = name
        self.age = age
        self.sex = sex
        self.sch_name = sch_name

    def tell(self,name,age,sex,school_id):
         pass

class Teacher(SchoolMember):
    def __init__(self, name, age, sex,sch_name,salary, course):
        super(Teacher, self).__init__(name, age, sex,sch_name)
        self.salary = salary
        self.course = course

    def tell(self):
        print("""
        ---------info of Teacher:%s ---------
        Nmae:%s
        Age:%s
        Sex:%s
        School_id:%s
        Salary:%s
        Course:%s
        """%(self.name,self.name,self.age,self.sex,self.sch_name,self.salary,self.course))

    def teach_grade(self,grade):
        pass

    def students_list(self):
        pass

class Students(SchoolMember):
    def __init__(self,name,age,sex,sch_name,stu_id,grade,pay_status):
        super(Students,self).__init__(name,age,sex,sch_name)
        self.stu_id = stu_id
        self.grade = grade
        self.pay_status = pay_status

    def pay_tuition(self,amount):
        pass

class Grade(object):
    '''班级类，包括班级名称，老师，课程，通过学校进行创建'''
    def __init__(self,name,teacher,course):
        self.name = name
        self.teacher = teacher
        self.course = course

class Course(object):
    '''课程类，包括学期，价格，通过学校进行创建'''
    def __init__(self,name,semester,price,sh_id):
        self.name = name
        self.semester = semester
        self.price = price
        self.sh_id = sh_id

# 实例化两个学校对象
school_bj = School("北京教育培训学校","沙河")
school_sh = School("上海教育培训学校","陆家嘴")

