
def func(*args):
    print('*args =', *args)
    print('args =', args)

    for a in args:
        print(a)


print('\ncall: func(10, 20, 30)')
func(10, 20, 30)

tuple_ = (10, 20, 30)
print('\ncall: func(tuple_)')
func(tuple_)

list_ = [10, 20, 30]
print('\ncall: func(list_)')
func(list_)

tuple_ = (10, 20, 30)
print('\ncall: func(*tuple_)')
func(*tuple_)

list_ = [10, 20, 30]
print('\ncall: func(*list_)')
func(*list_)