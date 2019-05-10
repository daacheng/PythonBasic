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
* hget key filed : 获取哈希表key中，字段名为filed的值。
* hlen key ： 获取哈希表中filed的数量。（相当于查看Python字典中有多少个键值对）
* hkeys key : 获取哈希表中所有filed的名称。（相当于查看Python字典中所有的键的名称）
* hvals key : 获取哈希表中所有的value。（相当于查看Python字典中所有的值）
* hexists key filed : 判断哈希表中是否存在指定的字段。（相当于查看Python字典中是否存在指定的键）
* hdel key filed : 删除哈希表中指定字段。
* hmset key filed1 value1 filed2 value2 : 一次设置哈希表中多个键值对。
* hmget key filed1 filed2 : 获取哈希表中多个字段的值。
## List（有序，可以重复）
* llen key : 查看列表中元素个数。
* lpush key value : 从头部往列表中添加一个元素。
* lpop key : 从列表头部取出一个元素。
* lrange key start end : 获取列表中指定范围内的元素。
* lset key index value : 通过所有设置列表中指定元素的值。
## Set（无序，不重复）
* sadd key member : 往集合中添加一个元素。
* scard key : 查看集合中元素个数。
* sismember key member : 判断元素是否存在集合中。
* srandmember key  ： 随机从集合中取出一个元素。
* srem key member ：移除集合中的元素。
## Sorted Set(有序集合)
* zadd key score member : 向有序集合中添加一个成员，指定分数（优先级）
* zcard key : 获取有序集合的元素个数。
* zcount key min max : 获取指定分数区间内元素个数。
* zrangebyscore key min max : 返回指定分数区间中的所有成员。
* zscore key member : 返回指定元素的分数（优先级）。

[Python操作redis](https://www.cnblogs.com/cnkai/p/7642787.html)
