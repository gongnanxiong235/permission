from src.dao.permission_dao import Permission

class PermissionService:
    def __init__(self):
        self.permission_service=Permission()
    def get_all_permission(self,role_id):
        response=''
        try:
            result=self.permission_service.get_permission(role_id)
            '''表示没有任何权限'''
            if result is None:
                response={'code': 202, 'data': {'msg': '没有任何可执行的权限，请联系管理员'}}
            else:
                '''获取到了权限'''
                print(result)
                pass
        except Exception as e:
            response={'code': 201, 'data': {'Exception': str ( e )}}
        finally:
            self.permission_service.helper.close()
        return response