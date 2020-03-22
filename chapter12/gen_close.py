def gen_func():
    yield "http://projectsedu.com"
    yield 2
    yield 3
    return "zhaoguom"

if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    gen.close()
    next(gen)