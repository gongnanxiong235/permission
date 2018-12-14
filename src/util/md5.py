import hashlib


def md5(arg):
    new_arg='gongnanxiong'+arg+"xiaozunzun"
    m = hashlib.md5()
    m.update(bytes(new_arg, encoding='utf8'))
    m_new=m.hexdigest ()
    m.update ( bytes ( m_new, encoding='utf8' ) )
    return m.hexdigest()

if __name__ == '__main__':
    print(md5('123456'))