# def add(*args):
#     ad = []         
#     for n in args:
#         ad.append(n)
#     return sum(ad)

# print(add(3, 4, 5))

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, multiply=5)

def calculate(n, **kwargs):
    n += kwargs.get("add")
    n *= kwargs.get("multiply")
    print(n)

calculate(2, multiply=5)