USER_LIST = {"zhanghao1": "123", "zhanghao2": "789"}#白名单

username = input("请输入账号：")

num = 0

if username in USER_LIST:
	while num < 3:
		password = input("请输入密码：")
		if USER_LIST.get(username) == password:
			print("登陆成功！")
		else:
			print("密码有误（如果连续三次输入错误则自动锁死账号）")
			num += 1
	else:
		print("连续三次输入错误，账号已锁死！")
else:
	print("用户名不存在！")