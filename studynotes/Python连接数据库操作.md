# Python连接数据库操作
## 连接mysql
### 方式一

    # 创建数据库连接
    conn = pymysql.connect(host="0.0.0.0", user="root", password="123456", db="dbname", port=3306, charset='utf8')
    # 创建游标
    cur = conn.cursor()
    # 执行sql
    sql = 'select * from table_name where 1 = 1'
    cur.execute(sql)
    res = cur.fetchone()
    print(res)
    # 关闭游标和数据库的连接
    cur.close()
    conn.close()

### 方式二

    db_config = {
            'host': '0.0.0.0',
            'port': 3306,
            'user': 'root',
            'password': '123456',
            'db': 'dbname',
            'charset': 'utf8'
        }
    with pymysql.connect(**db_config) as cur:
        sql = 'select * from table_name'
        cur.execute(sql)
        print(cur.fetchall())

### 方式三(数据库连接池)
* creator：使用链接数据库的模块
* maxconnections：连接池允许的最大连接数，0和None表示没有限制
* mincached：初始化时，连接池至少创建的空闲的连接，0表示不创建
* maxcached：连接池空闲的最多连接数，0和None表示没有限制
* maxshared：连接池中最多共享的连接数量，0和None表示全部共享，ps:其实并没有什么用，因为pymsql和MySQLDB等模块中的threadsafety都为1，所有值无论设置多少，_maxcahed永远为0，所以永远是所有链接共享
* blocking：链接池中如果没有可用共享连接后，是否阻塞等待，True表示等待，False表示不等待然后报错
* setsession：开始会话前执行的命令列表
* ping：ping Mysql 服务端，检查服务是否可用

      mysql_pool = PooledDB(
              creator=pymysql,  
              maxconnections=500,  
              mincached=0,  
              maxcached=20,  
              maxshared=0, 
              blocking=True,  
              setsession=[],  
              ping=1,  
              host='0.0.0.0',
              port=3306,
              user='root',
              password='123456',
              database='dbname',
              charset='utf8')

      conn = mysql_pool.connection()
      with conn.cursor() as cur:
          sql = 'select * from table_name'
          cur.execute(sql)
          data = cur.fetchall()
          print(data)
      conn.close()
