import threading

class FooBar():
    def __init__(self, n):
        self.n = n
        self.event_foo = threading.Event()
        self.event_bar = threading.Event()
        self.event_yeah = threading.Event()
        self.event_foo.set()

    def foo(self):
        for _ in range(self.n):
            self.event_foo.wait() # 等待執行續被呼叫
            print("foo", end='')
            self.event_foo.clear() # 執行續為初始狀態
            self.event_bar.set() # 呼叫下一個event

    def bar(self):
        for _ in range(self.n):
            self.event_bar.wait()
            print("bar", end='')
            self.event_bar.clear()
            self.event_yeah.set()

    def yeah(self):
        for _ in range(self.n):
            self.event_yeah.wait()
            print("yeah")
            self.event_yeah.clear()
            self.event_foo.set()

# n = input()
# try:
#     n = int(n)
# except:
#     print("Incorrect input, defaulted to 3.")
#     n = 3
n = 3
foobar = FooBar(n)
threads = [threading.Thread(target=foobar.foo),
           threading.Thread(target=foobar.bar),
           threading.Thread(target=foobar.yeah),]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()