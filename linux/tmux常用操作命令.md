## tmux 命令
#### 会话 session
* tmux：直接创建一个默认的会话session
* tmux ls: 查看所有的会话，快捷键：ctrl+b s
* tmux new -s session_name: 指定会话名称创建会话
* tmux detach: 离开会话，快捷键：ctrl+b d
* tmux a -t session_name: 进入会话
* tmux kill-session -t session_name: 杀掉会话，快捷键：ctrl+d
* tmux rename-session -t old_name new_name: 重命名session

#### 窗口 windows
* tmux new-window -n window_name: 新建一个窗口
* **ctrl+b w: 查看所有窗口**
* tmux select-window -t window_name: 切换窗口
* tmux kill-window -t window_name: 关闭窗口，快捷键：ctrl+b & 关闭当前窗口

#### 窗格 pane
* tmux split-window: 上下切割，快捷键：ctrl+b % 
* tmux split-window -h: 左右切割，快捷键：ctrl+b "
* ctrl+b 方向键：切换窗格
* ctrl+b x: 关闭窗格


