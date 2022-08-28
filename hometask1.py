def decorator(func):
    global a
    a=0
    def wrapped(*args,**kwargs):
        global
        a += 1
        print(a)
        return func(*args,**kwargs)
    return wrapped


@decorator
def typitsa():
    print('Вы тупицы')

print(a)
typitsa()
typitsa()
typitsa()
print(a)
print(b)