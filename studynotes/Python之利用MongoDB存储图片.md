# Python之利用MongoDB存储图片
## 存入图片到MongoDB数据库

    from pymongo import MongoClient
    from gridfs import *
    import os
    #连接mongodb
    client=MongoClient('localhost',27017)
    #取得对应的数据库
    db=client.pictures
    #取得对应的集合
    collection = db.test
    #图片路径
    img_path = r'C:\Users\daacheng\Desktop\timg.jpg'

    # 数据库其他字段信息
    img_info = {
        'content_type': 'jpg',
        'filename': 'timg.jpg',
        'filepath': img_path
    }

    with open(img_path, 'rb') as f:
        #创建写入流
        fs = GridFS(db, collection="test")
        data = f.read()
        #将数据写入，文件类型和名称通过前面的分割得到
        img_id=fs.put(data, **img_info)
        print(img_id)

## 从MongoDB中下载图片

    from gridfs import *
    from pymongo import MongoClient
    from bson.objectid import ObjectId
    # 连接数据库
    client = MongoClient('localhost', 27017)
    db = client['pictures']
    fs = GridFS(db, collection='test')
    # 通过id查找图片
    image_id = '5c2c720381b1bc41ec02eb89'
    result = fs.find_one({'_id': ObjectId(image_id)})
    data = result.read()
    with open('a.jpg', 'wb') as f:
        f.write(data)
