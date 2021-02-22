## 1.vim文本编辑器
1. 命令模式：控制光标移动，可对文本进行复制、粘贴、查找、删除等工作。
2. 输入模式：正常的文本录入。
3. 末行模式：保存或退出文档，以及设置编辑环境。

**每次在运行编辑器的时候，默认进入命令模式，此时需要先切换到输入模式后(通过a、i、o等键)，才能进行文档编写工作，而每次编写完文档后，需要先返回命令模式(通过Esc键)，然后再进入末行模式(通过:键)，执行文档的保存或退出操作。**
### 1.1.命令模式中常用的命令

命令 | 作用
---|---
dd | 删除（剪切）光标所在整行
5dd | 删除（剪切）从光标处开始的5行
yy | 复制光标所在整行
5yy | 复制从光标处开始的5行
n | 显示搜索命令定位到的下一个字符串
N | 显示搜索命令定位到的上一个字符串
u | 撤销上一步的操作
p | 将之前删除（dd）或复制（yy）过的数据粘贴到光标后面

### 1.2.末行模式中命令
**末行模式主要用于保存、退出文件，以及设置vim编辑器的工作环境，还可以让用户执行外部的linux命令或跳转到所编写文档的特定行数。通过冒号:键进入末行模式。**

命令 | 作用
---|---
:w | 保存
:q | 退出
:q! | 强制退出（放弃对文档的修改内容）
:wq! | 强制保存退出
:set nu | 显示行号
:set nonu | 不显示行号
:命令 | 执行该命令
:整数 | 跳转到该行
:s/one/two | 将当前光标所在行的第一个one替换成two
:s/one/two/g | 将当前光标所在行的所有one替换成two
:%s/one/two/g | 将全文中的所有one替换成two
?字符串 | 在文本中从下至上搜索该字符串
/字符串 | 在文本中从上至下搜索该字符串
:w filename | 将编辑的数据存储为另一个文件，另存为新文件
:r filename | 将另一个文件中的数据读入到当前文件。

## 2.vim的暂存盘
vim 会在与被编辑的文件的目录下创建一个名为.filename.swp 的文件。
我们对文件做的动作会被记录到这个文件中！如果你的系统因为某些原因断线了，
导致编辑的文件还没有储存，这个时候 .filename.swp 就能够发挥救援的功能了。

```python
E325: ATTENTION
Found a swap file by the name ".man_db.conf.swp"
          owned by: root   dated: Mon Feb 22 10:21:09 2021
         file name: ~root/vitest/man_db.conf
          modified: no
         user name: root   host name: iZ8vb6ughzbdqkfd58dowoZ
        process ID: 3252 (still running)
While opening file "man_db.conf"
             dated: Mon Feb 22 10:16:30 2021

(1) Another program may be editing the same file.  If this is the case,
    be careful not to end up with two different instances of the same
    file when making changes.  Quit, or continue with caution.
(2) An edit session for this file crashed.
    If this is the case, use ":recover" or "vim -r man_db.conf"
    to recover the changes (see ":help recovery").
    If you did this already, delete the swap file ".man_db.conf.swp"
    to avoid this message.

Swap file ".man_db.conf.swp" already exists!
[O]pen Read-Only, (E)dit anyway, (R)ecover, (Q)uit, (A)bort:
```

* O:以只读的方式打开文件，不进行编辑
* E：不载入暂存盘(.swp)的内容，直接进行编辑
* R：载入暂存盘的内容，在之前未保存的基础上继续编辑
* D：删掉暂存盘文件，如果不确定暂存盘是什么时候的可以不载入，直接删除
* Q：退出
