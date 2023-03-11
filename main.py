##############################################################
# LEARN PYTHON DAY-1,2023-03-06
# Salute to Hank Gan
# FROM:
# 1.https://github.com/ganyunhan
# 2.https://www.liaoxuefeng.com/wiki/1016959663602400
# 3.https://www.amghank.cn/
# 4.https://aijishu.com/a/1060000000306827
############################################################
import math
import types


# print('hello world!')
# print(sum(range(1,101)))

# from random import randint, sample
#
# # 初始化备选红色球,列表推导式写法
# red_balls = [x for x in range(1, 34)]
# # 选出六个红色球
# selected_balls = sample(red_balls, 6)
# # 对红色球进行排序
# selected_balls.sort()
# # 添加一个蓝色球
# selected_balls.append(randint(1, 16))
# # 输出选中的随机号码
# for index, ball in enumerate(selected_balls):
#     print('%02d' % ball, end=' ')
#     if index == len(selected_balls) - 2:
#         print('|', end=' ')
# print()

# # 首字母大写title(),全大写upper(),全小写lower()
# # 可以用+ 拼接字符串
# # 可以用strip去除空格，rstrip、lstrip是剔除右边、左边的空格
# name='  li haoxian  '
# print(name.title(),name.upper(),name.lower())
# print(name.strip())
# print(name.rstrip())
# print(name.lstrip())

##############################################################
# LEARN PYTHON DAY-2,2023-03-07
# Salute to Hank Gan & LIAO Xuefeng
# FROM:
# 1.https://www.liaoxuefeng.com/wiki/1016959663602400/1017032074151456
############################################################
# # input()可以让用户输入字符串
# name=input('输入姓名：')
# print('hello,', name)

# # 除法2种
# print('10/3=', 10/3, '\n')
# print('10//3=', 10//3)
#
# print(ord('中'))
# print(chr(20013))

# # 编码解码
# x='ABC'.encode('ascii')
# print(x)
# y=b'ABC'.decode('ascii')
# print(y)

# # 字符串长度
# length=len('ABC')
# print(length)

# # 关于格式化字符串:
# # 一种是用%s,%d这种;
# # 一种是用format();
# print('他叫{0}，目前得分为{1:.2f}'.format('大伟',27.8))
# # 一种是用f-string
# name='大卫'
# c=100
# print(f'他叫{name}，目前得分为{c:.2f}')

##############################################################
# LEARN PYTHON DAY-3,2023-03-08
# Salute to Hank Gan & LIAO Xuefeng
# FROM:
# 1.https://www.liaoxuefeng.com/wiki/1016959663602400/1017032074151456
############################################################

# # list类似数组
# other = ['canyon','commencal','santa cruz']
# bicycles = ['giant','trek','specialized',other,'cannondale']
# print(bicycles[0])
# print('I can not afford a ' + bicycles[3][2].title() + ' ' + 'mountain bike.')
# print(bicycles[-2][-1])
# # list加元素:
# # 1.加在末尾用append()
# other.append('car')
# print(other)
# # 2.加在其他位置用insert()
# other.insert(1, 'boot')
# print(other)
#
# # list删元素：
# # 1.知索引删除，用del语句
# del other[0]
# print(other)
# # 2.知内容删除，用remove()
# other.remove('car')
# print(other)
# # 3.删除栈顶元素(末尾那个)
# other.pop()
# print(other)
#
# # list对元素进行排序，用sort()
# other = ['uz','canyon','commencal','santa cruz']
# other.sort(reverse=False) #顺序
# print(other)

# # 元组tuple,和list非常类似，但是tuple一旦初始化就不能修改
# classmates = ('Michael', 'Bob', 'Tracy')

# if-elif-else语句
# for-in 语句
# while语句

##############################################################
# LEARN PYTHON DAY-4,2023-03-09
# Salute to Hank Gan & LIAO Xuefeng
# FROM:
# 1.https://www.liaoxuefeng.com/wiki/1016959663602400/1017032074151456
############################################################

# # 字典dict，键-值对（key-value）
# d = {'Mike': 95, 'Bob': 75, 'Tank': 85}
# d['Mike']=100
# print(d['Mike'])
# # 判断key是否存在
# print('Mike' in d)
# # 删除键-值对，用pop()
# d.pop('Mike')
# print('Mike' in d)

# # 集合set,只有key,且key不重复（重复会被过滤）
# s=set([1,2,3,3,4])
# print(s)
# s.add(1024)
# print(s)
# s.remove(1024)
# print(s)
# # set可以做交集&和并集|

# 函数定义：def语句
# def my_abs(x):
#     if x >= 0:
#         return x
#     elif x>-1024:
#         return -x
#     else:
#         pass
#
#
# print(my_abs(-1024), math.cos(math.pi))

# # 默认参数
# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s


# # 关键字参数
# def enroll(name, gender, age=6, city='Beijing', **k):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)
#     print('other:', k)
#
#
# print(power(5))
# enroll('Andy', 'P', city='ZHE', home='sky', play='genshin')


# # 限定关键字参数
# def person(name, age, *, city, job):
#     print(name, age, city, job)
#
#
# person('LI',21,city='WUHAN',job='student')

# # 切片slice
# L=[1,2,5,6,8]
# print(L)
# print(L[0:3])

##############################################################
# LEARN PYTHON DAY-5,2023-03-10
# Salute to Hank Gan & LIAO Xuefeng
# FROM:
# 1.https://www.liaoxuefeng.com/wiki/1016959663602400/1017032074151456
# 2.关于yield:https://blog.csdn.net/mieleizhi0522/article/details/82142856
############################################################

# # map()和reduce()函数
# def f(x):
#     return x * x
#
#
# m = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(list(m))
#
# # reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# def add(x, y):
#     return x + y
#
#
# from functools import reduce
# r = reduce(add, [1, 3, 5, 7, 9])
# print(r)

# # filter()把传入的函数依次作用于每个元素，
# # 然后根据返回值是True还是False决定保留还是丢弃该元素
# def is_odd(n):
#     return n % 2 == 1
#
# l=list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# print(l)

# yield的函数才是真正的迭代器。类似于return。
# next(foo())开始执行foo代码块，遇到yield返回
# 下次再next(foo()),从上个yield开始执行

# # 如果理解了上面的内容，那么就可以做素数生成了
# def odd_from3():
#     n=1
#     while True:
#         n += 2
#         yield n
#
#
# def select(n):
#     return lambda x: x % n > 0
#
#
# def primes():
#     yield 2
#     init_n = odd_from3()
#     while True:
#         n = next(init_n)
#         yield n
#         init_n = filter(select(n),init_n)
#
#
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break
        
##############################################################
# LEARN PYTHON DAY-6,2023-03-11
# Salute to Hank Gan & LIAO Xuefeng
# FROM:
# 1.https://www.liaoxuefeng.com/wiki/1016959663602400/1017032074151456
# 2.
# ############################################################

# # sorted()函数对list进行排序
# # sorted()可以接收一个key函数来实现自定义的排序
# s = sorted([36, 5, -12, 9, -21], key=abs)
# print(s)

# # 闭包，函数定义嵌套
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
#
#
# f = lazy_sum(1, 3, 5, 7, 9)
# print(f)
# print(f())

# # 匿名函数lambda
# m=map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(list(m))

# # functools.partial用于创建一个偏函数
# import functools
# int2 = functools.partial(int, base=2)
# print(int2('1000000'))

# 包与模块
# 每一个包目录下面都会有一个__init__.py的文件，
# 这个文件是必须存在的，否则，Python就把这个目录当成普通目录，
# 而不是一个包

# # 类与封装
# class Student(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print('%s: %s' % (self.name, self.score))
#
#
# stu1 = Student('LI', 1024)
# stu1.print_score()
# # 实例的变量名以__开头，就变成了一个私有变量（private）
# print(stu1.score)
# # 但是如果外部代码要获取name怎么办？可以给Student类增加get_name

# # 继承与多态
# class Animal(object):
#     def run(self):
#         print('Animal is running...')
#
#
# class Dog(Animal):
#     def run(self):
#         print('Dog is running...')
#     def eat(self):
#         print('Eating meat...')
#
#
# dog = Dog()
# dog.run()
# dog.eat()
# # 判断一个变量是否是某个类型可以用isinstance()判断
# print(isinstance(dog,Dog))
# print(isinstance(dog,Animal))
#
# # 判断对象类型，使用type()函数
# print(type(dog))
# print(type(123))
# # 判断一个对象是否是函数
# def fn():
#     pass
#
#
# print(type(fn)==types.FunctionType)
# print(type(abs)==types.BuiltinFunctionType)
# print(type(lambda x:x*x)==types.LambdaType)
# print(type((x for x in range(10)))==types.GeneratorType)
#
# # 获得一个对象的所有属性和方法，使用dir()函数
# d=dir('ABC')
# print(d)


# # 使用__slots__限制class实例能添加的属性
# # __slots__定义的属性仅对当前类实例起作用，对继承的子类不起作用
# class Student(object):
#     __slots__ = ('name', 'age')
#     pass
#
#
# s=Student()
# s.name = 'LI'
# s.age = 21



