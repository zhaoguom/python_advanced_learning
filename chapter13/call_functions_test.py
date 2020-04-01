import asyncio

def callback(sleep_time):
    print("sleep {} seconds success".format(sleep_time))

def stop_loop(loop):
    loop.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.call_soon(callback, 2)
    loop.call_later(2, callback, 2)
    loop.call_later(1, callback, 1)
    loop.call_later(3, callback, 3)
    # loop.call_soon(stop_loop, loop)
    loop.run_forever()