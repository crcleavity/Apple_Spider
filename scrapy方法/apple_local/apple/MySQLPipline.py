from pymysql import connect


class MySQLPipeline(object):
    def __init__(self):
        self.connect = connect(
            host='39.100.77.143',
            port=3306,
            db='scrapy',
            user='root',
            passwd='mysql',
            charset='utf8',
            use_unicode=True)
        # 连接数据库
        self.cursor = self.connect.cursor()
        # 使用cursor()方法获取操作游标

    def process_item(self, item, spider):
        self.cursor.execute(
            """insert into apple(shop_name, address, contact, href)
            value (%s, %s, %s, %s)""",
            (item['shop_name'],
             item['address'],
             item['contact'],
             item['href'],

             ))
        # 执行sql语句，item里面定义的字段和表字段一一对应
        self.connect.commit()
        # 提交
        return item
    # 返回item

    def close_spider(self, spider):
        self.cursor.close()
        # 关闭游标
        self.connect.close()
        # 关闭数据库连接