'''
1. 子生成器产生的值，都是直接传给调用方的，调用方通过.send()发送的值都是直接传递给子生成器的，如果发送的是None,会调用子生成器的__next__()方法，
如果不是None, 会调用子生成器的.send()方法
2. 子生成器退出的时候，最后的return expr，会触发一个StopIteration(expr)异常；
3. yield from 表达式的值，是子生成器终止时，传递给StopIteration异常的第一个参数；
4. 如果调用的时候出现StopIteration异常，委托生成器会恢复运行，同时其他的异常会向上抛出；
5. 传入委托生成器的异常里，除了GeneratorExit之外，其他的所有异常全部传递给子生成器的throw()方法，如果调用.throw()的时候出现了StopIteration异常，
那么就恢复委托生成器的运行，
'''

final_result = {}

def sales_sum(pro_name):
    total = 0
    nums = []
    while True:
        x = yield
        print(pro_name+"销量：", x)
        if not x:
            break
        total += x
        nums.append(x)
    return total, nums

def middle(key):
    while True:
        final_result[key] = yield from sales_sum(key)
        print(key+"销量统计完成！")

def main():
    data_sets = {
        "面膜":[1200, 1500, 3000],
        "手机":[28, 55, 98, 108],
        "大衣":[280, 560, 778, 70],
    }
    for key, data_set in data_sets.items():
        print("start key: ", key)
        m = middle(key)
        m.send(None)
        for value in data_set:
            m.send(value)
        m.send(None)
    print("final_result: ", final_result)

if __name__ == "__main__":
    main()