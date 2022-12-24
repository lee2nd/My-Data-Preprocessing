import itertools

my_list = [1,2,3,4]
for pair in itertools.product(my_list, repeat=2):
    func(*pair) # func 為自己定義的參數

# Output
# 1 2
# 1 3
# 1 4
# 2 1
# 2 2
# 2 3
# 2 4
# 3 1
# 3 2
# 3 3
# 3 4
# 4 1
# 4 2
# 4 3
# 4 4
