from src.util.database import MysqldbHelper as Helper

class User:
    def __init__(self):
        self.helper=Helper()
    def insert_user(self,username,password,full_name,age,gender):
        sql='insert into user(username,password,full_name,age,gender) values (%s,%s,%s,%s,%s)'
        return self.helper.executeInsert(sql,(username,password,full_name,age,gender))

    def update_user_role_id(self,user_id,role_id):
        sql='update user set role_id=%s where id=%s'
        self.helper.executeUpDe(sql,(user_id,role_id))

    def update_user_password(self,username,password):
        sql='update user set password=%s where username=%s'
        self.helper.executeUpDe(sql,(password,username))

    def is_exist_user(self,username):
        sql='select username from user where username=%s'
        result= self.helper.executeSelect(sql,(username),'one')
        return result

    def is_exist_user_password(self,username,password):
        sql='select id,username,full_name,gender,role_id from user where username=%s and password=%s'
        return self.helper.executeSelect(sql,(username,password),'one',rtype='dict')



if __name__ == '__main__':
    user=User()
    #user.update_user_role_id(1,1)
    #print(user.is_exist_user('admins'))
    print(user.is_exist_user_password('admin','admin'))