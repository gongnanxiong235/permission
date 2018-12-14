from src.util.database import MysqldbHelper as Helper

class Permission:
    def __init__(self):
        self.helper=Helper()

    def get_permission(self,role_id):
        sql='select caption,fun,module from permission where id in (select permission_id from role_permission where role_id=%s)'
        return self.helper.executeSelect(sql,(role_id),type='all',rtype='dict')


if __name__ == '__main__':
    p=Permission()
    result=p.get_permission(1)
    print(result)