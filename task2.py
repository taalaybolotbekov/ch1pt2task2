def stroka():
    n = int(input('vvedite kolichestvo uchenikov: '))
    k = int(input('vvedite kolichestvo apple: '))
    a=(k//n)
    b=(k % n)
    return('каждый получит по %s яблок , остаток %s'%(a,b))
print(stroka())