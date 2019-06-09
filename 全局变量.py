a = 100
def test():
    '''这是一个test方法的说明'''
    print(a)
    print(a+10)
    x = a+10
    print("----test------")
    return x

def test1():
    print("-----test1-----")
    print(test())
# test()
# test1()

def test1(a,b,func):
    result = func(a,b)
    print(result)
#lambda 是匿名函数的关键字。
test1(11,22,lambda x,y:x+y)