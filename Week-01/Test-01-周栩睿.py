name = str(input("输入你的姓名："))
key = str(input("输入你的密码："))
count = 0
while count < 2:
    if name == "周栩睿" and key == "011029":
        print("登陆成功")
        break
    count += 1
    print("用户名或密码错误，若连续3次错误则自动锁死账号")
    name = str(input("输入你的姓名："))
    key = str(input("输入你的密码："))

if count >= 2:
    print("因连续3次输入用户名或密码错误，账号已锁死")
