#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# Author:bear

import pickle,os,sys,re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import BasicLogic
from conf import setting
from core import school_func

def stu_registration():
    """学生注册"""
    print("欢迎来到学生注册系统！")
    for index,i in enumerate(school_func.school_list):
        print(index,i.name)
    school_id = int(input("请选择您要注册学校的序号："))
    school_func.show_grades()
    file_name_res = setting.file_name(setting.GRADE_PATH)
    tmp_grades = []
    for i in file_name_res:
        course_str = i
        suffix = re.search("\.+[a-z]{4}", course_str).group()
        course_str = course_str.replace(suffix, "")
        tmp_grades.append(course_str)
    for index,i in enumerate(tmp_grades):
        print(index,i)
    choose_grade = int(input("请输入您的班级序号："))
    stu_tmp_list = setting.file_name(setting.STUDENTDB_PATH)
    while True:
        stu_name = input("请输入您的姓名：")
        stu_file_name = setting.file_name(setting.STUDENTDB_PATH)
        tmp_stu = []
        for i in stu_file_name:
            stu_str = i
            suffix_stu = re.search("\.+[a-z]{4}", stu_str).group()
            course_str = stu_str.replace(suffix_stu, "")
            tmp_stu.append(course_str)
        if stu_name in tmp_stu:
            print("您输入的学生姓名已经存在，如果重名请联系管理员")
            break
        else:
            stu_age = input("请输入您的年龄：")
            stu_sex = input("请输入您的性别：")
            tmp_stu_id = setting.file_name(setting.STUDENTDB_PATH)
            stu_num = len(tmp_stu_id)
            stu_id = 1001 + stu_num
            pay_status = 0
            student = BasicLogic.Students(stu_name,stu_age,stu_sex,school_func.school_list[school_id].name,stu_id,tmp_grades[choose_grade],pay_status)
            school_func.school_list[school_id].enroll(student)
            stu_info = {
                "school": school_func.school_list[school_id].name,
                "name": stu_name,
                "age": stu_age,
                "sex": stu_sex,
                "id": stu_id,
                "grade": tmp_grades[choose_grade],
                "pay_status":pay_status,
            }
            file_path = "%s\%s.text" %(setting.STUDENTDB_PATH,stu_name)
            with open(file_path,"ab") as f:
                pickle.dump(stu_info, f)
# stu_registration()

def show_stu():
    """查看学生信息"""
    file_name_res = setting.file_name(setting.STUDENTDB_PATH)
    for i in file_name_res:
        file_path = "%s\%s" %(setting.STUDENTDB_PATH,i)
        with open(file_path,"rb") as f:
            res = pickle.load(f)
        print("""
        ---------info of Student:%s ---------
        学生姓名：%s
        学生性别：%s
        学生年龄：%s
        所属学校：%s
        学生ID：%s
        所属班级：%s
        缴费状态：%s
        """ % (res["name"],res["name"],res["sex"],res["age"],res["school"],res["id"],res["grade"],res["pay_status"]))
# show_stu()

def pay_tuition():
    """学生缴费，修改支付状态"""
    while True:
        stu_name = input("请输入您的姓名：")
        stu_file_name = setting.file_name(setting.STUDENTDB_PATH)
        tmp_stu = []
        for i in stu_file_name:
            stu_str = i
            suffix_stu = re.search("\.+[a-z]{4}", stu_str).group()
            course_str = stu_str.replace(suffix_stu, "")
            tmp_stu.append(course_str)
        if stu_name in tmp_stu:
            stu_db_path = "%s\%s.text" %(setting.STUDENTDB_PATH,stu_name)
            with open(stu_db_path, "rb") as f_stu:
                res = pickle.load(f_stu)
            pay_status = res["pay_status"]
            stu_grade = res["grade"]
            grade_db_path = "%s\%s.text" %(setting.GRADE_PATH,stu_grade)
            with open(grade_db_path, "rb") as f_grade:
                res_grade = pickle.load(f_grade)
            grade_course = res_grade["course"]
            if pay_status == 0:
                print("您当前的缴费状态：未缴费")
                course_db_path = "%s\%s.text" % (setting.COURSE_PATH,grade_course)
                with open(course_db_path, "rb") as f_course:
                    course_res = pickle.load(f_course)
                course_price = course_res["price"]
                i = 0
                while i < 3:
                    print("您所需要缴费的金额为：%s" %course_price)
                    stu_pay = int(input("请输入您要缴费的金额："))
                    if stu_pay == course_price:
                        print("缴费成功！")
                        res["pay_status"] = 1
                        with open(stu_db_path, "wb") as f_in:
                            pickle.dump(res, f_in)
                        with open(stu_db_path, "rb") as f_out:
                            show_stu = pickle.load(f_out)
                            print("""
                                    ---------info of Student:%s ---------
                                    学生姓名：%s
                                    学生性别：%s
                                    学生年龄：%s
                                    所属学校：%s
                                    学生ID：%s
                                    所属班级：%s
                                    缴费状态：%s
                                    """ % (
                                show_stu["name"], show_stu["name"], show_stu["sex"], show_stu["age"], show_stu["school"], show_stu["id"], show_stu["grade"],show_stu["pay_status"]))
                            # show_stu()
                        break
                    else:
                        print("您输入的金额不正确！重新输入")
                        i+= 1
                break
            if pay_status == 1:
                print("您当前的缴费状态：已缴费")
                break
        else:
            exit("您尚未注册，请先办理学员注册手续！")
# pay_tuition()

def logout():
    # sys.exit("欢迎下次光临")
    pass

def run():
    """学校管理接口菜单打印"""
    menu = '''
    -------Student registration centre ---------
    \033[32;1m 1.  学生注册
    2.  学生报名缴费
    3.  退出
    \033[0m'''
    menu_dic = {
        "1": stu_registration,
        "2": pay_tuition,
        "3":logout
    }
    menu_flag = True
    while menu_flag:
        print(menu)
        user_choice = input("请输入您要操作的ID：").strip()
        if user_choice == "3":
            menu_flag = False
            print("程序安全退出！")
        elif user_choice in menu_dic:
            menu_dic[user_choice]()
        else:
            print("\033[31;1m您输入的ID不存在，请重新输入!\033[0m")

if __name__ == "__main__":
    run()