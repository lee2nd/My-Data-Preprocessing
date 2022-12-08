def f(x):
    return {
        'a': 1,
        'b': 2
    }.get(x, 9)    # 9 will be returned default if x is not found

f('a')
# 1
f('b')
# 2
f('c')
# 9
f('fuck')
# 9
