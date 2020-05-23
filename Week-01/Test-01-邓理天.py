'''
让用户输入用户名和密码，如果输入正确，则显示“登陆成功”；
若用户名或密码输入错误，则显示“用户名或密码错误，若连续3次错误则自动锁死账号”；
若用户名或密码输入错误次数达到3次，则显示“因连续3次输入用户名或密码错误，账号已锁死”。
'''


def judge(n, p):  # 定义判断账号密码是否正确的函数
    username = 'yonghuming'
    password = 'mima123456'
    if n == username:
        if p == password:
            return True
        else:
            return False
    else:
        return False


a = input('请输入您的用户名：')
b = input('请输入您的密码：')  # 用户键入用户名和密码
i = 0
flag = judge(a, b)  # 调用判断函数
while flag == False and i < 2:  # 循环结构
    print('用户名或密码错误，若连续3次错误则自动锁死账号')
    i += 1
    a = input('请重新输入您的用户名：')
    b = input('请重新输入您的密码：')
    flag = judge(a, b)

if flag == True:  # 分支结构
    print('登陆成功')
else:
    print('因连续3次输入用户名或密码错误，账号已锁死')
