from src.dao.user_dao import User
from src.util import params_verify,md5



class UserService:
    def __init__(self):
        self.user=User()

    def login(self,username,password):
        try:
            is_exist_user=self.user.is_exist_user(username)
            if is_exist_user is None:
                '''表示没有查询出结果'''
                result={'code': 202, 'data': {'msg': '找不到此用户名'}}
            else:
                '''表示查询出了结果，判断密码是否错误'''
                password=md5.md5(password)
                is_exist_user_password=self.user.is_exist_user_password(username,password)
                if is_exist_user_password is None:
                    '''表示密码错误'''
                    result={'code':202,'data':{'msg':'密码错误'}}
                else:
                    result={'code': 200, 'data': {'msg': 'OK','user_info':is_exist_user_password}}
        except Exception as e:
            result={'code': 201, 'data': {'Exception': str(e)}}
        finally:
            self.user.helper.close()
        return result

    def regist(self,username,password,full_name,age,gender):
        try:
            for i in (username,password,full_name,age,gender):
                if params_verify.verify(i) is False:
                    raise Exception('%s不能为空或参数不合法' % i)
            else:
                # 如果没有查询出结果，返回None
                is_exist_user=self.user.is_exist_user(username)
                if is_exist_user is None:
                    password=md5.md5(password)
                    user_id=self.user.insert_user(username,password,full_name,age,gender)
                    result = {'code': 201, 'data': {'user_id': user_id}}
                    print("恭喜您注册成功")
                else:
                    raise Exception("用户名重复了")
        except Exception as e:
                print(e)
                # 代表出异常了
                result={'code':201,'data':{'Exception':str(e)}}
        finally:
            self.user.helper.close()
        return result

    def modify_password(self,username,old_password,new_password):
        try:
            '''先验证旧密码是否正确'''
            old_password=md5.md5(old_password)
            is_exist_user_password=self.user.is_exist_user_password(username,old_password)
            if is_exist_user_password is not None:
                '''表示密码正确,开始更新密码'''
                new_password=md5.md5(new_password)
                self.user.update_user_password(username,new_password)
                result={'code': 200, 'data': {'msg': 'OK'}}

            else:
                '''老密码错误'''
                result={'code': 202, 'data': {'mag': '老密码错误'}}
        except Exception as e:
            result={'code': 201, 'data': {'Exception': str ( e )}}
        finally:
            self.user.helper.close ()
        return result

if __name__ == '__main__':
    u=UserService()
    # g=u.regist("admin","admin","超级管理员",30,'1')
    # print("ggg:",g)
    # r=u.login('admin','admin')
    # print(r)
    s=u.modify_password('admin','123456','admin')
    print(s)
