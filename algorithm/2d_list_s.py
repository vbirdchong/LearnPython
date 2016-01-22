#!/usr/bin/env python
# coding=utf-8

'''
定义一个20*5的二维数组，用来存储某班级20位学员的5门课的成绩；这5门课按存储顺序依次为：core C++，coreJava，Servlet，JSP和EJB。

（1）循环给二维数组的每一个元素赋0~100之间的随机整数。

（2）按照列表的方式输出这些学员的每门课程的成绩。

（3）要求编写程序求每个学员的总分，将其保留在另外一个一维数组中。

（4）要求编写程序求所有学员的某门课程的平均分。
'''


import random


def get_score(course_list, score_list, student_num):

    # 每个学员的成绩
    everyone_score = [ [score_list[course][student] for course in range(len(course_list))] for student in range(student_num)]

    # 每个学员的总分
    everyone_total_score = [sum(everyone_score[i]) for i in range(len(everyone_score))]

    # 每个课程的平均分
    ever_score_avg = [sum(score_list[i])/len(score_list[i]) for i in range(len(score_list))]

    return everyone_score, everyone_total_score, ever_score_avg


course_list = ['c++', 'Java', 'servlet', 'JSP', 'EJB']
student_num = 20

score_list = [[ random.randint(0, 100) for x in range(student_num) ] for j in range(len(course_list))]


print "==========>The course list as below:"
for i in range(len(course_list)):
        print course_list[i], score_list[i]


print "==========>Everyone's course score as below:"
ever_score, ever_total_score, ever_score_avg = get_score(course_list, score_list, student_num)
for i in range(len(ever_score)):
    print ever_score[i]

print "==========>Everyone's total score as below:"
print ever_total_score


print "==========>Each course avg:"
for i in range(len(course_list)):
    print "{} average score is:{}".format(course_list[i], ever_score_avg[i])
