# kafka介绍
学习来源[kafka中文教程](http://orchome.com/3)
## 一、关于生产者、消费者、中间件
假设，生产者生产鸡蛋，消费者消费鸡蛋，生产者每生产一个消费者就消费一个。如果消费者突然噎住出现故障了，生产者这时还在生产鸡蛋，那新产生的鸡蛋就丢失了。
或者说生产者生产能力强，1秒钟生产100个鸡蛋，消费者1秒钟只消费50个鸡蛋，那剩下50个鸡蛋就丢失了。为了不让鸡蛋丢失，我们放一个篮子在生产者和消费者之间，
生产者生产的鸡蛋放到篮子里，消费者从篮子中拿鸡蛋，这样，鸡蛋（数据）被临时存储起来，就不会出现丢失的情况了。这个篮子就可以看做是中间件。
## 二、两种消息模型（队列式、发布-订阅式）
消息模型可以分成两种，一种是队列式消息模型，一种是发布-订阅式消息模型。
#### 队列式消息模型
一组消费者从队列中读取数据，一条消息只由其中的一个消费者来消费。
![](https://github.com/daacheng/PythonBasic/blob/master/pic/kafkaqueue.png)
#### 发布-订阅式模型
存在多个消费者组，一条消息以广播的形式发送给所有的消费者组，每个消费者组中只会有一个消费者去消费这个消息。
![](https://github.com/daacheng/PythonBasic/blob/master/pic/kafkafabu.png)
## 二、kafka相关定义
**kafka是消息中间件中的一种，它是一个高吞吐量的分布式的“发布-订阅”系统。**
1. kafka作为一个集群运行中一台或多台服务器上。
2. kafka集群存储的消息，以Topic为类别记录。
3. 每个消息叫做record，由key, value, 时间戳组成。
### 名词解释（很重要）
![](https://github.com/daacheng/PythonBasic/blob/master/pic/kafkahanyi.png)
* **Topic: kafka把消息用Topic来分类，Topic相当于一个分类标签。**
* **Producer：向Topic中发布消息的是生产者。**
* **consumer：预定Topic中的消息并消费的是消费者。**
* **broker：kafka是分布式的，可以运行在多台服务器上，一台kafka服务器就是一个broker，一个broker可以容纳多个Topic。**
* **partition:消息分区，一个Topic可以分为多个“消息分区”，每个“消息分区”都是一个有序的队列，partition中每条消息都会分配一个有序的ID（offset）。**
* **offset：偏移，消息在消息分区中的偏移量，每个消息都有一个唯一的offset，消费者可以指定offset来消费消息。**
### 三、kafka的分区机制
#### 1、kafka的一个Topic可以有多个分区（partition），如果存在key，消息会按照key做分类，存储在不同的分区中；如果没有key，就按照轮询机制，存储在不同的分区中。
#### 2、kafka每个分区（partition）都是一个消息队列，分区中使用偏移（offset）表示每个消息的位置。
#### 3、一个Topic中的一个分区（partition）只能对应一个消费者组中的一个消费者。（每个Topic中的一个分区中的消息，可以发送给所有的消费者组，但是消费者组中只能有一个消费者消费这个消息。）**一个分区对应一个消费者，一个消费者可以对应多个分区，同一个消费者组中不可以有比分区更多的消费者，多出来的消费者会收不到消息，一直处于空等待。**
#### 4、一个分区对应一个消费者，所以消息肯定是按照顺序发送给这个消费者的，但是这这能保证Topic中这个分区内消息是顺序处理的，不能保证跨分区的消息先后处理，如果想要顺序处理Topic中所有的数据，那就是只提供一个分区。
#### 5、kafka通过leader和follower的方式，将分区的数据复制到不同是服务器中，进行同步。**kafka往分区中写入数据时，只会往leader分区中写入数据，然后再复制给followers**。
![](https://github.com/daacheng/PythonBasic/blob/master/pic/kafkaleader.png)
