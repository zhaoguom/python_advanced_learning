def fib(n):
    if n<=2:
        return 1
    return fib(n-2) + fib(n-1)


def fib2(index):
    re_list = []
    n, a, b, = 0, 0, 1

    while n<index:
        re_list.append(b)
        a,b = b, a+b
        n+=1
    return re_list

def fib3(index):
    n,a,b = 0, 0, 1

    while n<index:
        yield b
        a, b = b, a+b
        n+=1

if __name__ == "__main__":
    for x in fib3(100):
        print(x, end=" ")

