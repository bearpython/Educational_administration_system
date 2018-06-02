#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# Author:bear

import sys,os,json,pickle,re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import BasicLogic
from conf import setting

school_list = []
school_list.append(BasicLogic.school_bj)
school_list.append(BasicLogic.school_sh)


def add_course():
    '''创建课程，用户输入课程信息'''
    for index,i in enumerate(school_list):
        print(index,i.name)
    school_id = int(input("请选择课程所在学校的序号："))
    i = 0
    while i < 3:
        add_course_name = input("请输入课程的名称：")
        file_path = "%s\%s.text" % (setting.COURSE_PATH, add_course_name)
        if os.path.isfile(file_path):
            print("您所要创建的课程已经存在，请重新输入")
            i += 1
            if i == 3:
                print("您输入的课程名称错误三次，程序退出")
        else:
            add_course_time = input("请输入课程的周期：")
            add_course_price = input("请输入课程的价格：")
            add_course_price = int(add_course_price)
            course = BasicLogic.Course(add_course_name, add_course_time, add_course_price, school_list[school_id].name)
            school_list[school_id].creat_course(course)
            course_info = {"school": school_list[school_id].name,
                           "course": add_course_name,
                           "time": add_course_time,
                           "price": add_course_price,
                           }
            # file_path = "%s\%s.text" %(setting.COURSE_PATH,add_course_name)
            with open(file_path, "ab") as f:
                pickle.dump(course_info, f)
            break
# add_course()

def add_teacher():
    '''创建老师，管理员输入老师的信息，由school类进行创建'''
    for index,i in enumerate(school_list):
        print(index,i.name)
    school_id = int(input("请选择老师所在学校的序号："))
    add_teacher_name = input("请输入老师的姓名：")
    add_teacher_age = input("请输入老师的年龄：")
    add_teacher_sex = input("请输入老师的性别：")
    add_teacher_salary = int(input("请输入老师的薪资："))
    # add_teacher_course = input("请输入老师主讲课程：")
    course_tmp_list = setting.file_name(setting.COURSE_PATH)
    course_list = []
    for coures in course_tmp_list:
        suffix = re.search("\.+[a-z]{4}", coures).group()
        course_str = coures.replace(suffix, "")
        course_list.append(course_str)
    while True:
        if len(course_list):
            for index,i in enumerate(course_list):
                print(index,i)
            break
        else:
            print("学校还没有创建课程，请先创建课程！")
            add_course()
            #return
    add_teacher_course = int(input("请选择讲师所授课程的序号："))
    teacher = BasicLogic.Teacher(add_teacher_name,add_teacher_age,add_teacher_sex,school_list[school_id].name,add_teacher_salary,course_list[add_teacher_course])
    school_list[school_id].hire(teacher)
    teacher_info = {"school":school_list[school_id].name,
                   "name":add_teacher_name,
                   "age":add_teacher_age,
                   "sex":add_teacher_sex,
                    "salary":add_teacher_salary,
                    "course":course_list[add_teacher_course],
                   }
    file_path = "%s\%s.text" %(setting.TEACHERDB_PATH,add_teacher_name)
    with open(file_path,"ab") as f:
        pickle.dump(teacher_info, f)
# add_teacher()

def add_grade():
    '''创建班级，用户输入选择班级的信息进行创建'''
    for index,i in enumerate(school_list):
        print(index,i.name)
    school_id = int(input("请选择班级所在学校的序号："))
    add_grade_name = input("请输入班级名称：")
    teacher_tmp_list = setting.file_name(setting.TEACHERDB_PATH)
    teacher_list = []
    for teachers in teacher_tmp_list:
        suffix = re.search("\.+[a-z]{4}", teachers).group()
        course_str = teachers.replace(suffix, "")
        teacher_list.append(course_str)
    while True:
        if len(teacher_list):
            for index,i in enumerate(teacher_list):
                print(index,i)
            break
        else:
            print("还没有创建老师，请先创建讲师！")
            add_teacher()
    add_grade_teacher = int(input("请选择班级老师的序号："))
    course_tmp_list = setting.file_name(setting.COURSE_PATH)
    course_list = []
    for coures in course_tmp_list:
        suffix = re.search("\.+[a-z]{4}", coures).group()
        course_str = coures.replace(suffix, "")
        course_list.append(course_str)
    while True:
        if len(course_list):
            for index,i in enumerate(course_list):
                print(index,i)
            break
        else:
            print("还没有创建课程，请先创建课程！")
            add_course()
    add_grade_course = int(input("请选择班级课程的序号："))
    grade = BasicLogic.Grade(add_grade_name,teacher_list[add_grade_teacher],course_list[add_grade_course])
    school_list[school_id].creat_grade(grade)
    grade_info = {"school":school_list[school_id].name,
                   "name":add_grade_name,
                   "teacher":teacher_list[add_grade_teacher],
                   "course":course_list[add_grade_course],
                   }
    file_path = "%s\%s.text" %(setting.GRADE_PATH,add_grade_name)
    with open(file_path,"ab") as f:
        pickle.dump(grade_info, f)
# add_grade()

def show_courses():
    '''查看课程列表，反序列化课程文件'''
    file_name_res = setting.file_name(setting.COURSE_PATH)
    for i in file_name_res:
        file_path = "%s\%s" %(setting.COURSE_PATH,i)
        with open(file_path,"rb") as f:
            res = pickle.load(f)
            print("""
            -----------------info of Course:%s
            学校名称：%s
            课程名称：%s
            课程周期：%s
            课程价格：%s
            """ %( res["course"],res["school"], res["course"], res["time"], res["price"]))
# show_courses()

def show_teachers():
    '''查看老师列表，反序列化老师的数据文件'''
    file_name_res = setting.file_name(setting.TEACHERDB_PATH)
    for i in file_name_res:
        file_path = "%s\%s" %(setting.TEACHERDB_PATH,i)
        with open(file_path,"rb") as f:
            res = pickle.load(f)
            # course_str = res["course"]
            # suffix = re.search("\.+[a-z]{4}",course_str).group()
            # course_str = course_str.replace(suffix,"")
        print("""
        ---------info of Teacher:%s ---------
        学校名称：%s
        老师姓名：%s
        老师年龄：%s
        老师性别：%s
        老师所授课程：%s
        老师薪资：%s
        """ % (res["name"],res["school"],res["name"],res["age"],res["sex"],res["course"],res["salary"]))
# show_teachers()

def show_grades():
    """查看班级信息"""
    file_name_res = setting.file_name(setting.GRADE_PATH)
    for i in file_name_res:
        file_path = "%s\%s" %(setting.GRADE_PATH,i)
        with open(file_path,"rb") as f:
            res = pickle.load(f)
            # course_str = res["course"]
            # suffix = re.search("\.+[a-z]{4}",course_str).group()
            # course_str = course_str.replace(suffix,"")
            # teacher_str = res["teacher"]
            # teacher_str = teacher_str.replace(suffix,"")
        print("""
        ---------info of Grade:%s ---------
        学校名称：%s
        班级名称：%s
        班级讲师：%s
        班级课程：%s
        """ % (res["name"],res["school"],res["name"],res["teacher"],res["course"]))
# show_grades()

def logout():
    # sys.exit("欢迎下次光临")
    pass

def run():
    """学校管理接口菜单打印"""
    menu = '''
    -------Educational administration system---------
    \033[32;1m 1.  查看课程信息
    2.  查看讲师信息
    3.  查看班级信息
    4.  添加课程
    5.  添加讲师
    6.  添加班级
    7.  退出
    \033[0m'''
    menu_dic = {
        "1": show_courses,
        "2": show_teachers,
        "3": show_grades,
        "4": add_course,
        "5": add_teacher,
        "6": add_grade,
        "7":logout
    }
    menu_flag = True
    while menu_flag:
        print(menu)
        user_choice = input("请输入您要操作的ID：").strip()
        if user_choice == "7":
            menu_flag = False
            print("程序安全退出！")
        elif user_choice in menu_dic:
            menu_dic[user_choice]()
        else:
            print("\033[31;1m您输入的ID不存在，请重新输入!\033[0m")

if __name__ == "__main__":
    run()