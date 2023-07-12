import pymysql
from common.logger import write_log
from config.ProjectConfig import VBConfig
def execute_db(sql):
    """"
    连接接口项目mysql数据库，并执行sql语句
    :param sql: sql语句
    :return:
    """
    try:
        # 打开数据库连接
        db_config = {

            "host": "127.0.0.1",

            "port": 3306,

            "user": "root",

            "password": "123456",

            "db": "vueblog3"

        }
        db = pymysql.connect(**db_config)
        # 新建游标
        cursor = db.cursor()
        # 执行sql
        cursor.execute(sql)
        # 获取执行结果
        res = cursor.fetchall()
        # 关闭游标
        cursor.close()
        # 提交连接
        db.commit()
        # 关闭连接
        db.close()
        return res
    except pymysql.OperationalError as e:
        write_log.error("数据库连接，执行失败".format(e))

# def init_db_category():
#     """
#     初始化数据库，删掉表中的数据
#     """
#     execute_db("delete from category;")
#
# def insert_category():
#     execute_db("INSERT INTO category(cateName,date) VALUES ('myabc2',NOW());")
#     execute_db("select")
#
# if __name__ == '__main__':
#     init_db_category()
#     insert_category()