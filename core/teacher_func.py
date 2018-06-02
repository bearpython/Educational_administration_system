#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# Author:bear

import sys,os,json,pickle,re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import BasicLogic
from conf import setting
from core import school_func,student_func


def logout():
    # sys.exit("欢迎下次光临")
    pass

def run():
    """学校管理接口菜单打印"""
    menu = '''
    -------The lecturer system ---------
    \033[32;1m 1.  查看课程信息
    2.  查看班级信息
    3.  查看班级学员列表
    4.  退出
    \033[0m'''
    menu_dic = {
        "1": school_func.show_courses,
        "2": school_func.show_grades,
        "3": student_func.show_stu,
        "4":logout
    }
    menu_flag = True
    while menu_flag:
        print(menu)
        user_choice = input("请输入您要操作的ID：").strip()
        if user_choice == "4":
            menu_flag = False
            print("程序安全退出！")
        elif user_choice in menu_dic:
            menu_dic[user_choice]()
        else:
            print("\033[31;1m您输入的ID不存在，请重新输入!\033[0m")

if __name__ == "__main__":
    run()