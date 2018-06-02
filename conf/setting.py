#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# Author:bear

import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

DATA_PATH = "%s\data" %BASE_DIR

STUDENTDB_PATH = "%s\students" %DATA_PATH
TEACHERDB_PATH = "%s\\teachers" %DATA_PATH
COURSE_PATH = "%s\courses" %DATA_PATH
GRADE_PATH = "%s\grades" %DATA_PATH



def file_name(file_dir):
    '''获取文件名的方法，在查看课程，老师，学生，班级的时候调用'''
    file_list = []
    for root,dirs,files in os.walk(file_dir):
        for i in files:
            file_list.append(i)
    return file_list
# res = file_name(COURSE_PATH)
# print(res)
