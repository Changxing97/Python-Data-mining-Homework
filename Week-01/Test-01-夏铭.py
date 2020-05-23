name="abc"
password="123"

for i in range(3):
    name_input=input('请输入你的账号：')
    password_input=input('请输入你的密码：')
    if name==name_input and password==password_input:
        print('登陆成功')
        break
    else:
        print('用户名或密码错误，若连续3次错误则自动锁死账号')
        if i==2:
            print('因连续3次输入用户名或密码错误，账户已锁死')


