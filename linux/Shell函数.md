## Shell函数
```python
function func {
    statements
    [return value]
}

# 调用 Shell 函数时可以给它传递参数，也可以不传递。如果不传递参数，直接给出函数名字
func
# 如果传递参数，那么多个参数之间以空格分隔
name param1 param2 param3
```

```python
#!/bin/bash

function getsum(){
    local sum=0
    for var in $*
    do
        ((sum+=var))
    done
    return $sum
}

getsum 1 2 3
echo $?

```
