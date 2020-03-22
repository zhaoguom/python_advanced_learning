def gen_func():
    #1. 可以产出值
    #2. 可以接收值
    html = yield "http://projectsedu.com"
    print(html)
    yield 2
    yield 3
    return "zhaoguom"

#1. throw, close

#1. 生成器不仅可以产出值，还可以接收值

if __name__ == "__main__":
    gen = gen_func()
    url = next(gen)
    print(url)
    html = "zhaoguom"
    print(gen.send(html)) # send方法可以传递值进入生成器内部，同时还可以重启生成器执行到下一个yield位置
    
