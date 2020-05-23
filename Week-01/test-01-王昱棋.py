i = 1
user = '123'
password = '345'
while i < 4:
    a = input("请输入用户名：")
    b = input("请输入密码：")

    if user == a and password == b:
        print("登陆成功")
        break
    else:
        print("用户名或密码错误，若连续三次错误则自动锁死账号")
        i = i + 1
        if i == 4:
            print("因三次输入用户名或密码错误，账号已锁死")
