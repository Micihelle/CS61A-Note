from urllib.request import urlopen

shakespeare = urlopen('http://composingprograms.com/shakespeare.txt')
'''
将变量shakespeare与=号后面的表达式的值关联起来
该表达式运用urlopen函数于一个URL,该URL包含了shakespeare 37部戏剧的完整文本，全部在一个.txt文件中。
print(shakespeare)
'''
words = set(shakespeare.read().decode().split())
'''
指令链 read, decode,split
我们从开放URL地址中read读取数据，然后将数据解码decode成文本，最后split将文本分割成为单词。所有的这些单词被储存在set集合里面
'''

reversal = {w for w in words if len(w) == 6 and w[::-1] in words}
print(reversal)

'''
- 主要作用：遍历words里面 能够在进行倒序以后会出现在shakespeare文章中 并且长度等于6的单词
- 关于切片操作
b = a[i:j]  
表示复制a[i]到a[j-1]，以生成新的list对象
b = a[i:j:s]
表示：i,j与上面的一样，但s表示步进，缺省为1.
所以 a[i:j:1] 相当于 a[i:j]
当s<0时，i缺省时，默认为-1. j缺省时，默认为-len(a)-1
所以a[::-1]相当于 a[-1:-len(a)-1:-1]，也就是从最后一个元素到第一个元素复制一遍，即倒序。
w[::-1]相当于对w列表中的所有元素进行倒序
'''
