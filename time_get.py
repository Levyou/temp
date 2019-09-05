import datetime

def time_list(li):
    t_li = list()
    today = datetime.date.today()        # 获取当前日期, 因为要求时分秒为0, 所以不要求时间
    weekday = today.weekday()
    for i in range(len(li[0])):
        delta = datetime.timedelta(weekday-li[0][i])    # 当前日期距离周一的时间差
        day = today - delta    # 获取这周一日期
        dt = datetime.datetime.strptime(str(day) + li[1], "%Y-%m-%d %H:%M")
        t_li.append(dt)
    return t_li
today = datetime.datetime.now()  
print(time_list([[1,3,5],' 09:30']))
if today<datetime.datetime(2019, 9, 5, 20, 30):
    print(today)
