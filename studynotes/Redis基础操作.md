# Redis基础操作
## key
* keys * : 查看所有的key
* del key ： 删除指定的key
* exists key: 查看key是否存在
* expire key: 给key设置过期时间，秒

## 字符串
* set key value : 设置指定key的值
* get key : 获取指定key的值
* strlen key : 返回key所存储的字符串的长度。
* getset key value : 将给定key的值设置为value，并返回老的value。
* setex key 秒数 value : 将key的值设置为value，并设置key的过期时间。
* append key value : 如果key已经存在，并且value是字符串，新的value会追加到原来的value后面。
## Hash
* hset key filed value : 将哈希表key中字段名为filed的值设置为value（相当于创建一个python字典，字典的名称为key，field是字典中的key，value是字典中的值）
