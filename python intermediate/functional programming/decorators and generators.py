# 定义装饰器函数
def my_decorator(func):
    def wrapper():
        print('函数执行前')
        func()
        print('函数执行后')
    return wrapper

# 给函数应用装饰器
@my_decorator
def say_hello():
  print('你好，装饰器！')

# 调用添加装饰器后的函数
say_hello()

# 普通函数（一次性生成所有数据）
def get_numbers_normal(n):
    result = []
    for i in range(n):
        result.append(i * 2)
    return result

# 生成器函数（节省内存）
def get_numbers_generator(n):
    for i in range(n):
        yield i * 2          # yield 代替 return


# 使用
for num in get_numbers_generator(1000000):   # 即使生成100万个数也不会占用太多内存
    print(num)
    if num > 20:
        break