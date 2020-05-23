user = "LuZhen"
passwd = 123456
a = 1
while a <= 3:
    username = str(input("please input your username:"))
    password = float(input("please input your password:"))
    if username == user and password == passwd:
        print("登陆成功")
        a = a + 1
        break
    else:
        print("用户名或密码错误，若连续三次错误则锁死账号")
        a = a + 1
else:
    print("因连续三次输入用户名或密码错误，账号已锁死")
