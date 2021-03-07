# if语句

### if
```python
if condition
then
    ....
fi
```

```python
# 示例
#!/bin/bash

a=3
if (($a>2))
then
    echo "a大于2"
fi

[root@iZ8vb6ughzbdqkfd58dowoZ bin]# shell_1.sh
a大于2
```


### if else
```python
if  condition
then
   ....
else
   ....
fi
```

```python
#!/bin/bash

read -p "请输入a的值: " a
if (($a>=10))
then
    echo "a大于等于10"
else
    echo "a小于10"
fi

[root@iZ8vb6ughzbdqkfd58dowoZ bin]# shell_1.sh
请输入a的值: 5
a小于10
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# shell_1.sh
请输入a的值: 12
a大于等于10
```

### if elif else
```python
if  condition1
then
   ...
elif condition2
then
    ...
elif condition3
then
    ...
else
   ...
fi
```

```python
#!/bin/bash

read -p "请输入a的值: " a
if (($a>=10))
then
    echo "a>=10"
elif (($a>=5))
then
    echo "5<=a<10"
else
    echo "a<5"
fi

[root@iZ8vb6ughzbdqkfd58dowoZ bin]# shell_1.sh
请输入a的值: 3
a<5
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# shell_1.sh
请输入a的值: 5
5<=a<10
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# shell_1.sh
请输入a的值: 12
a>=10
```
