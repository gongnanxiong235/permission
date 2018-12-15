from src.service.user_service import UserService
from src.service.permission_service import Permission
import importlib
class LoginPage:
    def __init__(self):
        self.user_service=UserService()
        self.permission_service=Permission()
    def login_page(self):
        for i in range(3):
            intent=input("请选择登录or注册-->1:登录 2:注册")
            if intent.isdigit() and intent in ('1','2'):
                intent=int(intent)
                if intent==1:
                    '''调登录方法'''
                    for j in range(3):
                        if j==2:
                            '''tag决定数据库连接什么时候关闭'''
                            tag=1
                        else:
                            tag=0
                        result=self.enter_login(tag)
                        '''表示登录成功'''
                        if result['code']==200:
                            '''跳转到下一个页面，把基本信息带入'''
                            self.home_page(result['data']['user_info'])
                            return
                        elif result['code']==202:
                            if j == 2:
                                print ( "错误次数太多了，明天再来" )
                                return
                            else:print(result['data']['msg'],'请重新输入')
                        else:
                            print("服务器异常:",result['data']['Exception'])
                            return

                    pass
                if intent==2:
                    pass
            else:
                if i==2:
                    print("错误次数太多了，明天再来")
                    return
                else:print("输入错误，请重新输入")
    def enter_login(self,tag):
        username=input("username:")
        password=input("password")
        return self.user_service.login (username,password,tag)

    def home_page(self,args):
        print('欢迎你%s，告诉我您要做什么' % args['full_name'])
        '''获取所有权限'''
        role_dict=self.permission_service.get_permission(args['role_id'])
        print(role_dict)
        number_list=[]
        for i,v in enumerate(role_dict,1):
            print(i,v['caption'])
            number_list.append(str(i))
        for i in range(3):
            number=input("请输入编号:")
            '''表示输入非法'''
            if number.isdigit() is False or number  not in number_list:
                if i==2:
                    print('输入错误次数太多了')
                    return
                else:print ( '输入非法，请重新输入' )
            else:
                '''动态找到需要调用的方法,这里如果方法路径不是当前路径可以用importlib动态导入模块'''
                fun_name=role_dict[int(number)-1]['fun']
                '''反射的方式调用方法'''
                getattr(self,fun_name)(args)
    def modify_password_page(self,args):
        old_password=input('请输入老密码:')
        new_password=input("请输入新密码:")
        response=self.user_service.modify_password(args['username'],old_password,new_password)
        print(response)




if __name__ == '__main__':
    LoginPage().login_page()


