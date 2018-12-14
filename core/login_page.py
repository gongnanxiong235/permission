from src.service.user_service import UserService
class LoginPage:
    def __init__(self):
        self.user_service=UserService()
    def login_page(self):
        for i in range(3):
            intent=input("请选择登录or注册-->1:登录 2:注册")
            if intent.isdigit() and intent in ('1','2'):
                intent=int(intent)
                if intent==1:
                    '''调登录方法'''
                    for j in range(3):
                        result=self.enter_login()
                        '''表示登录成功'''
                        if result['code']==200:
                            '''跳转到下一个页面，把基本信息带入'''
                            break
                        elif result['code']==202:
                            print(result['data']['msg'],'请重新输入')
                        else:
                            print("服务器异常:",result['data']['Exception'])
                            break
                            return


                    pass
                if intent==2:
                    pass
            else:
                if i==2:
                    print("错误次数太多了，明天再来")
                    return
                else:print("输入错误，请重新输入")
    def enter_login(self):
        username=input("username:")
        password=input("password")
        return self.user_service.login (username,password)


if __name__ == '__main__':
    LoginPage().login_page()


