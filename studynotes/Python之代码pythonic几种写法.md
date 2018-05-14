## 两个变量值替换

    a,b= 5,6
    print(a)      #5
    print(b)      #6
    a,b=b,a
    print(a)      #6
    print(b)      #5

## 链式比较

    a=5
    b=4
    2<b<a<7   #True

## 真值测试
**True：任意非空字符串；任意非零数字；任意非空容器     False：空字符串''；数字0；空的容器[]{}()Set();None**

    dic =  {'a':1}
    name = 'bob'
    lis =  [1,2,3]
    if dic and name and lis:
        print(123)
## 字符串反转

    s = 'abcde'
    s[::-1]   #'edcba'

## 列表生成式

    [x*x for x in range(9) if x%3==0]     #[0, 9, 36]

## 字典默认值

    dic = {}
    dic['a']=dic.get('a',0)
    dic

## for……else……

    for i in range(5):
        print(i)
    else:
        print('over')

## 三元符代替

    a=3
    b=2 if a>4  else  0
    b  #0

## Enumerate

    for i, e in enumerate(['a','b','c']):
        print(i,e)      #0 a
                        #1 b
                        #2 c

## zip创建键值对

    #使用zip创建键值对
    key = ['a','b','c']
    val = [1,2,3]
    dict(zip(key,val))      # {'a': 1, 'b': 2, 'c': 3}


