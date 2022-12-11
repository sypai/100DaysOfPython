# Working with *args
def add(*args):
    sum = 0
    # args will be a tuple (arguments with order)
    for n in args:
        sum += n
    print(sum)

add(1, 2, 3, 4, 5, 6)
add(1)

# Working with **kwargs (keyword arguments)
def calculate(num, **kwargs):
    # kwargs will be a dictionary (arguments with name(keyword))
    num += kwargs.get('add')
    num *= kwargs.get('multiply')
    
    print(num)

calculate(2, add=20, multiply=5)