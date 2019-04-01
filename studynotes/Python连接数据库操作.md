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

## 连接oracal
* 1、下载安装cx_Oracle    https://pypi.org/project/cx-Oracle/#files
* 2、下载instantclient，配置环境变量。    https://www.oracle.com/technetwork/cn/topics/winx64soft-101515-zhs.html
* 3、 把instantclient文件夹下所有的ddl文件复制到anaconda文件夹下。（复制oci，oraocci11，oraociei11的3个DLL粘贴到你的PY目录的Libs/site-packages文件夹下面）
* 4、编写测试代码

        info = "username/password@ip:/SERVICE_NAME"
        db = cx_Oracle.connect(info)
        cursor = db.cursor()
        # 执行数据库语句
        res = cursor.execute("SELECT * FROM T_SH_JDCJBXX WHERE 1=1")
        print(res.fetchone())

### 数据库连接池连接oracal

    dsn = cx_Oracle.makedsn(db_host, db_port, db_name)
    pool = PooledDB(cx_Oracle, mincached=20, blocking=True, user=db_user, password=db_pass, dsn=dsn)
    conn = pool.connection()
    with conn.cursor() as cursor:
        sql = ""
        res = cursor.execute(sql)
        scan_result = res.fetchall()
    conn.close()

## 连接sqlite
sqlite数据库可以当做缓存来用，如果不想用redis的话，可以考虑用sqlite

    import sqlite3
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    # 查看数据库中表是否存在
    sql = "select * from sqlite_master where type = 'table' and name = 'user'"
    cur.execute(sql)
    values = cur.fetchall()
    if values:
        print(values)
    else:
        # 如果不存在，创建表
        cur.execute('create table user (id varchar(20) primary key, name varchar(20))')
        cur.execute('insert into user (id, name) values (\'1\', \'Michael\')')
    cur.close()
    conn.close()
