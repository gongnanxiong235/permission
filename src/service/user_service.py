from src.dao.user_dao import User
from src.util import params_verify
class UserService:
    def __init__(self):
        self.user=User()

    def login(self):
        pass

    def regist(self,username,password,full_name,age,gender):
        result=""
        try:
            for i in (username,password,full_name,age,gender):
                if params_verify.verify(i) is False:
                    raise Exception('%s不能为空或参数不合法' % i)
            else:
                #如果没有查询出结果，返回None
                is_exist_user=self.user.is_exist_user(username)
                if is_exist_user is None:
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

    def modify_password(self):
        pass


if __name__ == '__main__':
    u=UserService()
    g=u.regist("","123456","ppp",30,'1')
    print("ggg:",g)
