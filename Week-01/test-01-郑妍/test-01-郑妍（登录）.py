a={"dsglij":"sd56er","s5168":"1564e489","56aq849":"sa56e84e"}
i=1
while True:
    user=input("username:")
    pswd=input("password:")
    if user in a:
        if i<3:
            if pswd==a[user]:
                print("登陆成功")
                break
            else:
                print("用户名或密码错误，若连续3次错误则自动锁死账号")
                i=i+1
        else:
            if pswd==a[user]:
                print("登陆成功")
                break
            else:
                print("因连续3次输入用户名或密码错误，账号已锁死")
                break
    else:
        print("用户名不存在")
        i = i + 1
