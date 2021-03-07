## while语句
```python
while condition
do
    ...
done
```

```python
#!/bin/bash

read -p "请输入m:" m
read -p "请输入n:" n

sum=0
while ((m <= n))
do
   ((sum+=m))
   ((m++))
done

echo "sum:$sum"

[root@iZ8vb6ughzbdqkfd58dowoZ bin]# shell_1.sh
请输入m:0
请输入n:9
sum:45
```
