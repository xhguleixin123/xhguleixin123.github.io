[toc]



# python基础

## 数据类型和变量

### 数据类型

#### 浮点数

#### 字符串

* 为了简化换行\n操作，常使用：

```python
print('''line1
... line2
... line3''')
```

#### 布尔值

#### 空值

#### 变量

> 变量都是地址指向

#### 常量

* // 地板除：两个整数的除法仍然是整数。



 ## 字符串与编码

### 字符编码

* ASCII 最早由美国人发明，只有127个字符，有大小写英文字母、数字和一些符号（一个字节）。

* GB23112是中国的编码方式（两个字节）

* Unicode是为了解决多国的语言编码标准而诞生的，一般是两个字节。

* UTF-8是因为英语不需要占两个字节，为了解决这个问题，所以在出现这种编码方式。

  >记事本在读取时采用Unicode，保存时准换成UTF-8

  > 浏览器页面输出采用的就是UTF-8编码

![编码图1](images\编码图1.png)

![编码图2](images\编码图2.png)



### 字节串和字符串

#### bytes

> bytes是以字节为单位的，可以叫字节串。

```python
# 创建一个空的bytes
b1 = bytes()
# 创建一个空的bytes值
b2 = b''
# 通过b前缀指定hello是bytes类型的值
b3 = b'hello'
print(b3)
print(b3[0])
print(b3[2:4])
# 调用bytes方法将字符串转成bytes对象
b4 = bytes('我爱Python编程',encoding='utf-8')
print(b4)
# 利用字符串的encode()方法编码成bytes，默认使用utf-8字符集
b5 = "学习Python很有趣".encode('utf-8')
print(b5)
```

输出：

```
b'hello'
104
b'll'
b'\xe6\x88\x91\xe7\x88\xb1Python\xe7\xbc\x96\xe7\xa8\x8b'
b'\xe5\xad\xa6\xe4\xb9\xa0Python\xe5\xbe\x88\xe6\x9c\x89\xe8\xb6\xa3'
```

104是h的Unicode编码，\x是十六进制，\xe6是两个16进制，一个16进制是4位bit，两个16进制是一个字节（8bit）

* 可以使用字符串自带的encode()方法来讲字符串转换成字节串。

#### 字符串

* encode() 方法，按照指定方式**编码**，第一个参数是编码方式，第二个参数是发生错误所采用的方法。
* decode()方法，按照指定方式**解码**，第一个参数是解码方式，第二个参数是发生错误所采用的方法。
* ord("A")方法，返回字符的整数值。
* chr()方法，返回编码对应的字符。
* len()方法，返回字符串长度。

#### 占位符

%实现占位

```python
'Hello, %s' % 'world'
'Hi, %s, you have $%d' % ('Michael', 1000000)
```

Format实现站位

```python
'Hello, {0},成绩提升了{1:.f}%'.format('小明'，17.125)
```



## 使用list和uple

### list(列表)

* len(<list>)获取列表元素个数

```python
classmates = ['Michael','Bob','Tracy']
len(classmates)
# 空列表的长度是0
L = []
len(L)
```

* 获取每一位置的元素

```python
# 获取第一位的元素
classmates[0]
# 获取第二位的元素
classmates[1]
# 获取最后一位的元素
classmates[-1]
# 获取倒数第二位的元素
classmates[-2]
```

* append()在列表末尾添加一个元素

```python
classmates.append('Adsm')
```

* pop()删除列表元素

```python
# 删除list末尾的元素
classmates.pop()
# 删除指定位置的元素
classmates.pop(i)
```

* 替换指定位置的元素

```python
classmates[1] = 'Sarah'
```

* 列表中的元素类型可以不同

```python
L = ['Apple',123,True]
```

* 列表中套列表（多维数组）

```python
s = ['python','java',['asp','php'],'scheme']

# 输出多维列表,第3个元素（是一个列表）的第2个元素
s[2][1]
```

* insert()在指定位置上插入元素

```python
# 在序号为1的索引上插入一个元素
classmates.insert(1,'Jack')
```

### tuple

> tuple一旦内容确定就无法改变，没有**append()**和**insert()**方法，其他方法和list一样。

* 空的tuple

```python
t = ()
```

* 定义只有一个元素的的tuple

```python
# 括号会被认为是小括号，所以t只是1。
t = (1)
# 需要在1后面添加一个，来表示是tuple。
t = (1,)
```

* 改变tuple的内容

```python
t = ('a','b',['A','B'])
# 因为t当中第三个元素是list，所以可以改变list的指向
t[2][0] = 'X'
t[2][1] = 'Y'
```

###  条件判断

* if语句简写

```python
# 只要x是非空字符，非零数，非空list就为True,否则为Flase
if x:
    print('True')
```



* if-else语句

```python
age = 3
if age >= 18:
    print('your age is ' , age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')
```

* if-elif (elif是else if 的缩写)，**只要满足一个**就自动忽略后面的判断。

```python
age = 3
if age >=18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
```

### 循环

#### range()

```python
# 从0到9
range(10)
# 从1到10
range(1,11)
# 从0到30，步长为5
range(0,31,5)
# 从0到-9，步长为-1
range(0,-10,-1)
```

#### for-in 循环

```python
# 遍历list
names = ['Michael'.'Bob','Tracy']
for name in names:
    print(nmae)
    

# 循环n次    
for i in range(n+1):
    print(i+1)
```

#### break

> 结束整个循环

#### continue

> 提早结束当前循环

### 使用dict和set

#### dict

> dict的键的顺序与添加的顺序无关
>
> dict的键唯一

```python
# list
names = ['Michael','Bob','Tracy']
scores = [95,75,85]

# dict 
d = ['Michael':95,'Bob':75,'Tracy':85]

# 通过键（key）来访问值（Value）
d['Michael']

# 添加和修改键值的方法
d['Michael'] = 66 # 修改键值
d['Jack'] = 88 # 添加键值

# 判断键是否存在
'Thomas' in d
d.get('Thomas') # 存在返回True，否则返回False
d.get('Thomas',-1) # 存在返回True，不存在返回指定的-1

# 删除键值的方法
d.pop('Bob')
```

#### set

> set存放不重复的不可变对象！！！

```python
# 通过list来作为输入集合(会过滤重复项)
s = set([1,2,3])

# 通过add方法来添加元素(同样会过滤重复项)
s.add(4)

# 集合的交、并集操作
s1 = set([1,2,3])
s2 = set([2,3,4])
s1 & s2 #交集
s1 | s2 #并集
```



#### 不可变对象

```python
# liset内部的方法会改变list自身
a = ['c','b','a']
a.sort()

# 字符串自身的方法，不改变字符串本身，只返回一个返回值
a = 'abc'
b = a.replace('a','A') #a仍然不变，只是返回通过replace方法返回了一个值给b
```

