def swap1(a,b):
    a=a^b
    b=a^b
    a=a^b
    print(f"after swapping, a={a} and b={b} ")
def swap2(a,b):
    a=(a&b)+(a|b)
    b=a+(~b)+1
    a=a+(~b)+1
    print(f"after swapping, a={a} and b={b} ")

swap1(17,29)
swap2(18,4)