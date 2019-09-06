#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/6 0006 14:31
# @Author  : y

import datetime

def time_list(li):
    t_li = list()
    today = datetime.date.today()
    weekday = today.weekday()
    for i in range(len(li[0])):
        # 获取本周、上周、下周的开奖日期日期
        for t in [-7,0,7]:
            delta = datetime.timedelta(weekday-li[0][i]+t)
            day = today - delta
            dt = datetime.datetime.strptime(str(day) + li[1], "%Y-%m-%d %H:%M")
            t_li.append(dt)
    now = datetime.datetime.now()
    t_li.append(now)
    # 冒泡排序从小到大
    n = len(t_li)
    for i in range(n):
        for j in range(0, n - i - 1):
            if t_li[j] > t_li[j + 1]:
                t_li[j], t_li[j + 1] = t_li[j + 1], t_li[j]
    index_now = t_li.index(now)
    next_time = t_li[index_now+1]
    last_time = t_li[index_now-1]
    return str(next_time), str(last_time)

print(time_list([[1,3],' 09:30']))
