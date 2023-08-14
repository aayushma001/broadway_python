# THe order of arguments in a funtion must be in following way :
# 1. Positional
# 2. Default
# 3. *args
# 4. ** kwargs

def addition(a, b, c, d=1, e=2, f=3, *args, ** kwargs):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(args)
    print(kwargs)


addition(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, p=11, q=12, r=14)
