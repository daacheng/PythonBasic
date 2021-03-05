# Shell字符串
## 1.字符串表示
* 单引号包围，任何字符串都会原样输出，在其中使用变量无效
* 双引号包围，会解析其中的变量值之后再输出
* 获取字符串长度：${#var}

```python
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# var=123asd
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo $var
123asd
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# var='mail $MAIL'
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo $var
mail $MAIL
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# var="mail $MAIL"
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo $var
mail /var/spool/mail/root
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo ${#var}
25
```

## 2.字符串截取
* 从字符串左边开始计算：${string: start :length}，start:起始位置从0开始，length截取的长度
* 从字符串右边开始计算：${string: 0-start :length}
* ${string#*chars}： 从 string 字符串第一次出现 *chars 的位置开始，截取 *chars 后面的所有字符(从前往后匹配)
* ${string##*chars}: 从 string 字符串最后一次出现 *chars 的位置开始，截取 *chars 后面的所有字符(从前往后匹配)
* ${string%*chars}: 从 string 字符串第一次出现 *chars 的位置开始，截取 *chars 前面的所有字符(从后往前匹配)
* ${string%%*chars}: 从 string 字符串最后一次出现 *chars 的位置开始，截取 *chars 前面的所有字符(从后往前匹配)

```python
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# var=www.baidu.com
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo ${var:4:5}
baidu
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo ${var:4}
baidu.com
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo ${var:0-3:3}
com
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo ${var#*bai}
du.com
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo ${var#*.}
baidu.com
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo ${var##*.}
com
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo ${var%bai*}
www.
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo ${var%.com*}
www.baidu
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo ${var%.*}
www.baidu
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo ${var%%.*}
www
```
