## case in语句
```python
case expression in
    pattern1)
        ...
        ;;
    pattern2)
        ...
        ;;
    pattern3)
        ...
        ;;
    *)
        statementn
esac
```

```python
#!/bin/bash

printf "输入一个整数:"
read num

case $num in
    1)
        echo "Monday"
        ;;
    2)
        echo "Tuesday"
        ;;
    3)
        echo "Wednesday"
        ;;
    4)
        echo "Thursday"
        ;;
    5)
        echo "Friday"
        ;;
    6)
        echo "Saturday"
        ;;
    7)
        echo "Sunday"
        ;;
    *)
        echo "error"
esac

[root@iZ8vb6ughzbdqkfd58dowoZ bin]# shell_1.sh
输入一个整数:1
Monday
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# shell_1.sh
输入一个整数:2
Tuesday
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# shell_1.sh
输入一个整数:9
error
```
