#shopmail
goods = {'iphone':1000,'mac book':2000,'bike':500}
goodsname=list(goods.keys())
shoppingcart={'iphone':0,'mac book':0,'bike':0}
def shopping(usern,useracc):
    global shoppingcart
    print('{}登录成功'.format(usern))
    account2=int(useracc)
    ss = input('按任意键请继续购物，随时输入Q退出')
    while ss != 'Q':
        ss = input('商品有iphone，单价1000，mac book ，单价2000，bike ，单价500，\n请直接输入商品名购买，如果输入Q退出\n')
        if ss in goodsname:
            if account2 >= goods[ss]:
                shoppingcart[ss]+=1
                account2-=goods[ss]
                print(F'购买{ss}成功!余额还有{account2}')
                continue
            else:
                print('余额不足')
                print('已购',end='')
                for key,v in shoppingcart.items():
                    print('{}{}个,'.format(key,v),end='')
                print('余额有{}。'.format(account2))
        elif ss !="Q":
            print('输入错误')

    else:
        print('已购',end='')
        for key,v in shoppingcart.items():
            print('{}{}个,'.format(key,v),end='')
        print('余额有{}。'.format(account2))
with open('user.txt','r+') as f1 ,open('b.txt','r+') as f2:
    users=f1.readlines()
    a=[]
    for w  in users:
        a.append(w.split()[0])
    name1 =input('请输入名字>:')
    while  name1 in f2.readlines():
        name1 =input(' 名字禁止登录，请输入名字>:')
    password1=input('请输入密码>:')
    if  name1 in a:
        for i in range(len(users)):
            user = users[i].split()
            if name1 == user[0]:
                log=1
                while user[1]!=password1:
                    if log==3 :
                        print('错误太多，禁止登录')
                        if user[0] not in f2.readlines():
                            f2.seek(0,2)
                            f2.write('{}\n'.format(user[0]))
                        break
                    log+=1
                    password1=input('密码错误，请输入密码>:')
                else:
                    shopping(user[0],user[2])

    else:
        print('请先注册')
        name1 =input('请输入名字>:')
        while not name1 or name1  in a or name1  in f2.readlines():
            print('名字为空,名字已存在或禁止登录')
            name1 =input('请输入名字>:')
        password1=input('请输入密码>:')
        password2=input('请再次输入密码>:')
        while password1 != password2:
            print('两次输入的密码不一致')
            password1=input('请输入密码>:')
            password2=input('请再次输入密码>:')
        account1=int(input('请输入余额>:'))
        f1.write('{} {} {}\n'.format(name1,password1,account1))
        print('注册成功')
        shopping(name1,account1)
