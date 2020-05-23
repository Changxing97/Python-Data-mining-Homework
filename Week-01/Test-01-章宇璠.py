if __name__ == "__main__":
    init_usrname = input('Please enter initial username:')
    init_password = input('Please enter initial password:')
    flag0 = 0
    flag1 = 0
    print('>>>设置成功<<<')
    while True:
        usr = input('enter username:')
        password = input('enter password:')
        if usr == init_usrname and password == init_password:
            print('登陆成功!')
            flag1 = 1
            break
        else:
            flag0 += 1
        if flag0 <= 2:
            print('用户名或密码错误，若连续3次错误则自动锁死账号')
        if flag1 == 1:
            break
        if flag0 > 2:
            print('因连续3次输入用户名或密码错误，账号已锁死')
            break
