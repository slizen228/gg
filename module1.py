class vremia(BaseException):
    pass
def decorator(n):
    def wrapper(a,b,c):
        print(n(a,b,c))
        s=(b*c)+((((a-b)/c)*c*c)/2)
        print(s)
    return wrapper

@decorator
def urawn(a,b,c):
    v=(a-b)/c
    return v
try:
    a=int(input('Введите конечную скорость'))
    b=int(input('Введите начальную скорость'))
    c=int(input('Введите время'))
    if c==0:
        raise vremia()
    urawn(a,b,c)
except ValueError:
    print('Eto doljni bit chisla')
except vremia:
    print("vremia ne doljno bit ravno nulu")
finally:
    print('Programma zavershena')


