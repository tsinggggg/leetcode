import keyword
keyword.kwlist
# ['False',
#  'None',
#  'True',
#  'and',
#  'as',
#  'assert',
#  'break',
#  'class',
#  'continue',
#  'def',
#  'del',
#  'elif',
#  'else',
#  'except',
#  'finally',
#  'for',
#  'from',
#  'global',
#  'if',
#  'import',
#  'in',
#  'is',
#  'lambda',
#  'nonlocal',
#  'not',
#  'or',
#  'pass',
#  'raise',
#  'return',
#  'try',
#  'while',
#  'with',
#  'yield']

#在 [], {}, 或 () 中的多行语句，不需要使用反斜杠。

content = input("input sth")
print(content)


print('123') # 默认换行
print('123', end = "") # 不换行

#%module
#** power
#// interger division

#So there are many types of objects which can be used with a for loop. These are called iterable objects.
#The built-in function iter takes an iterable object and returns an iterator.
# >>> x = iter([1, 2, 3])
# >>> x
# <listiterator object at 0x1004ca850>
# >>> x.next()
# 1
# >>> x.next()
# 2
# >>> x.next()
# 3
# >>> x.next()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

#Iterators are implemented as classes. 
# class yrange:
#     def __init__(self, n):
#         self.i = 0
#         self.n = n

#     def __iter__(self):
#         return self

#     def next(self):
#         if self.i < self.n:
#             i = self.i
#             self.i += 1
#             return i
#         else:
#             raise StopIteration()

# The __iter__ method is what makes an object iterable. 
# Behind the scenes, the iter function calls __iter__ method on the given object.
# The return value of __iter__ is an iterator. 
# It should have a next method and raise StopIteration when there are no more elements.
# In the above case, both the iterable and iterator are the same object. It need not be the case always.

# 元组、列表、字典和字符串对象是可迭代的，但不是迭代器，不过我们可以通过 iter() 函数获得一个迭代器对象；
# Python 的 for 循环实质上是先通过内置函数 iter() 获得一个迭代器，然后再不断调用 next() 函数实现的；
# 自定义迭代器需要实现对象的 __iter()__ 和 next() 方法（注意：Python3 要实现 __next__() 方法），其中，__iter()__ 方法返回迭代器对象本身，next() 方法返回容器的下一个元素，在没有后续元素时抛出 StopIteration 异常。


#在 Python 中，使用了 yield 的函数被称为生成器（generator）。

def f():
	print('1')
	yield 1
	print('2')
	yield 2
	print('3')
	yield 3

# 	带有 yield 的函数执行过程比较特别：

# 调用该函数的时候不会立即执行代码，而是返回了一个生成器对象；
# 当使用 next() (在 for 循环中会自动调用 next()) 作用于返回的生成器对象时，函数开始执行，在遇到 yield 的时候会『暂停』，并返回当前的迭代值；
# 当再次使用 next() 的时候，函数会从原来『暂停』的地方继续执行，直到遇到 yield 语句，如果没有 yield 语句，则抛出异常；


# >>> def generator_function():
# ...     value1 = yield 0
# ...     print 'value1 is ', value1
# ...     value2 = yield 1
# ...     print 'value2 is ', value2
# ...     value3 = yield 2
# ...     print 'value3 is ', value3
# ...
# >>> g = generator_function()
# >>> g.next()   # 调用 next() 方法开始执行，返回 0
# 0
# >>> g.send(2)
# value1 is  2
# 1
# >>> g.send(3)
# value2 is  3
# 2
# >>> g.send(4)
# value3 is  4
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

def generator_function():
	try:
		yield 'Normal'
	except ValueError:
		yield 'Error'
	finally:
		print('Finally')


def print_info(arg1, *vartuple):

	print('arg1'+str(arg1))
	for x in vartuple:
		print(x)
print_info(10)
print_info(70, 60, 50)	


# 变量作用域

# L （Local） 局部作用域
# E （Enclosing） 闭包函数外的函数中
# G （Global） 全局作用域
# B （Built-in） 内建作用域

# 以 L –> E –> G –> B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。
# Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问。
# 定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
# 局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。
# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字。	

num = 1
def fun1():
	global num  # 需要使用 global 关键字声明
	print(num) 
	num = 123
	print(num)
fun1()

def outer():
	num = 10
	def inner():
		nonlocal num   # nonlocal关键字声明
		num = 100
		print(num)
	inner()
	print(num)
outer()

# A namespace is a mapping from names to objects.

def scope_test():
	def do_local():
		spam = "local spam"

	def do_nonlocal():
		nonlocal spam
		spam = "nonlocal spam"

	def do_global():
		global spam
		spam = "global spam"

	spam = "test spam"
	do_local()
	print("After local assignment:", spam)
	do_nonlocal()
	print("After nonlocal assignment:", spam)
	do_global()
	print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

# After local assignment: test spam
# After nonlocal assignment: nonlocal spam
# After global assignment: nonlocal spam
# In global scope: global spam

# # When a class definition is entered, a new namespace is created, and used as the local scope — thus, all assignments to local variables go into this new namespace.
# The original local scope (the one in effect just before the class definition was entered) is reinstated, and the class object is bound here to the class name given in the class definition header 

class MyClass:
	"""A simple example class"""
	def __init__(self):
		self.__data=1
		self._data=1

	i = 12345
	temp_list=[]

	def f(self):
		print(self.__data)

# x.f() is exactly equivalent to MyClass.f(x).         

class Dog:

	tricks = []             # mistaken use of a class variable

	def __init__(self, name):
		self.name = name

	def add_trick(self, trick):
		self.tricks.append(trick)

# >>> d = Dog('Fido')
# >>> e = Dog('Buddy')
# >>> d.add_trick('roll over')
# >>> e.add_trick('play dead')
# >>> d.tricks                # unexpectedly shared by all dogs
# ['roll over', 'play dead']

# Data attributes override method attributes with the same name; to avoid accidental name conflicts, which may cause hard-to-find bugs in large programs, it is wise to use some kind of convention that minimizes the chance of conflicts. Possible conventions include capitalizing method names, prefixing data attribute names with a small unique string (perhaps just an underscore), or using verbs for methods and nouns for data attributes.

