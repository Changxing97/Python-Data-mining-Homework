# 如果账号密码是个excel的话,(主要是我也不知道还能用什么装orz)
import xlrd

data = xlrd.open_workbook('usernameandpassword.xls')  # 瞎起名了嘻嘻
table = data.sheets()[0]
nrows = table.nrows
for i in range(nrows):
    if i == 0:
        continue
    for i in range(2):
        if i < 2:
            username = input('用户名为: ')
            password = input('密码为: ')
            if password == username[data]:
                print('登陆成功')
            else:
                print('用户名或密码错误，若连续3次错误则自动锁死账号')
                i += 1
        else:
            username = input('用户名为: ')
            password = input('密码为: ')
            if password == username[a]:
                print('登陆成功')
            else:
                print('因连续3次输入用户名或密码错误，账号已锁死')
