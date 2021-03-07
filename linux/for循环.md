## for循环
```python
for(( 初始化语句; 判断条件; 自增或自减 ))
do
    ...
done
```

```python
#!/bin/bash

sum=0
for ((i=0;i<=100;i++))
do
    ((sum+=i))
done

echo $sum
```


## python风格的for循环
```python
items=("item1" "item2" "item3")
for s in ${items[*]}
do
    echo "$s"
done

[root@iZ8vb6ughzbdqkfd58dowoZ bin]# shell_1.sh 
item1
item2
item3
```
