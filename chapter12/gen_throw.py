def gen_func():
    try:
        yield "http://projectsedu.com"
    except Exception:
        pass
    yield 2
    yield 3
    return "zhaoguom"

if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    gen.throw(Exception, "download error")
    print(next(gen))
    gen.throw(Exception, "download error")