def verify(params):
    if params is None or str(params).strip()=="":
        return False
    return True

if __name__ == '__main__':
    print(verify("     "))