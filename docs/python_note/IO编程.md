# IO编程

> 读取文件的方式有两种
>
> * 同步编程：等待读取完再去做后面的事。
> * 异步编程：不等待，先做后边的事。

## 文件读写

```python
try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close() # 一定要关闭，不然占用太多内存了，系统内存有限，必须关闭
# 两者等价
with open('/path/to/file', 'r') as f:
    print(f.read())
# 会自动执行close()方法

# 读取二进制文件
f = open('/Users/michael/test.jpg', 'rb')
f.read()
# 读取GBK编码文件
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
# 遇到错误编码选择忽略
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
# 写文件啊
f = open('/Users/michael/test.txt', 'w')
f.write('Hello, world!')
f.close()
# 等价于
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')
```

## StringIO和BytesIO

> 在内存中读写

```python
# StringIO
from io import StringIO
f = StringIO()
f.write('hello')
print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodbye!') # 可以直接初始化
while True:
     s = f.readline()
     if s == '':
         break
     print(s.strip())
# BytesIO
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8')) # 将重恩按utf-8进行二进制编码转成Bytes格式
print(f.getvalue())
# 同样可以直接初始化
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()
```

## 操作文件和目录

```python
# 查看当前目录的绝对路径
os.path.abspath('.')
# 合并两个目录
os.path.join('/Users/michael', 'testdir')
# 创建一个目录
os.mkdir('/Users/michael/testdir')
# 删除一个目录
os.rmdir('/Users/michael/testdir')
# 从最后一个目录拆分一个目录
os.path.split('/Users/michael/testdir/file.txt')
# 拆分出文件的拓展名
os.path.splitext('/path/to/file.txt')

# 重命名文件
os.rename('test.txt', 'test.py')
# 删除文件
os.remove('test.py')
# 列出当前目录下的所有目录
[x for x in os.listdir('.') if os.path.isdir(x)]
['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Applications', 'Desktop', ...]
#累出所有.py文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']#列表表达式
['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']
```

## 序列化

```python
# 序列化
import pickle
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)# 将文件序列化成一个bytes
f = open('dump.txt', 'wb')
pickle.dump(d, f) # 将变量序列化成一个文件
f.close()

# 反序列化
f = open('dump.txt', 'rb')
d = pickle.load(f)#反序列化
f.close()
d
{'age': 20, 'score': 88, 'name': 'Bob'}

```