def isPower(a):
    while a > 0:
        print(a)
        if a == 1:
            return True
        if a % 2 != 0:
            return False
        a = a // 2
    return False


print(isPower(-1))
