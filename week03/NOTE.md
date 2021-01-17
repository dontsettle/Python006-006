学习笔记
1，在windos下安装MYSQL5.7,增加配置文件，my.ini，并改字符集
#basedir=C:\Users\Administrator\mysql-5.7.32-winx64
#datadir=C:\Users\Administrator\mysql-5.7.32-winx64\data
#lower_case_table_names = 2
[client]
default_character_set=utf8mb4
[mysql]
default_character_set=utf8mb4
[database]
default_character_set=utf8mb4
[mysqld]
character-set-server = utf8mb4
max_allowed_packet= 64M

验证字符集的 SQL 语句
mysql> show variables like '%character%';
+--------------------------+--------------------------------------------------+
| Variable_name            | Value                                            |
+--------------------------+--------------------------------------------------+
| character_set_client     | utf8mb4                                          |
| character_set_connection | utf8mb4                                          |
| character_set_database   | utf8mb4                                          |
| character_set_filesystem | binary                                           |
| character_set_results    | utf8mb4                                          |
| character_set_server     | utf8mb4                                          |
| character_set_system     | utf8                                             |
| character_sets_dir       | C:\Users\Administrator\mysql-5.7\share\charsets\ |
+--------------------------+--------------------------------------------------+
8 rows in set, 1 warning (0.01 sec)

2. 使用 sqlalchemy ORM 方式创建如下表，使用 PyMySQL 对该表写入 3 条测试数据，并读取:
用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间
将 ORM、插入、查询语句作为作业内容提交
from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, Table, Float, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime,Date
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Archivse_table(Base):
    __tablename__ = 'archivse5'
    archiv_id = Column(Integer(), primary_key=True)
    archiv_name = Column(String(50), index=True)
    archiv_age = Column(Integer())
    archiv_birthday = Column(Date(), nullable=False)
    archiv_gender = Column(String(50) )
    archiv_degree = Column(String(50))
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)


    def __repr__(self):
        return "Archivse_table(archiv_id='{self.archiv_id}', " \
            "archiv_name='{self.archiv_name}',"\
            "archiv_age={self.archiv_age} , "\
            "archiv_birthday={self.archiv_birthday},"\
            "archiv_gender={self.archiv_gender} ,"\
            "archiv_degree={self.archiv_degree}"\
            ")" .format(self=self)
        # return (f"{self.archiv_id}, {self.archiv_name}, {self.archiv_age}, {self.archiv_birthday}, "
        #         f"{self.archiv_gender}, {self.archiv_degree}, "
        #         f"{self.create_on}, {self.update_on}")


# 实例一个引擎
dburl = "mysql+pymysql://root:123456@localhost/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=True, encoding="utf-8")
Base.metadata.create_all(engine)

# 创建session
SessionClass = sessionmaker(bind=engine)   
session = SessionClass()

# 增加数据
archiv_demo = Archivse_table(archiv_id= 14 ,archiv_name='王琼英',archiv_birthday = "1960-1-1",
                        archiv_age=50 ,archiv_gender='女', archiv_degree='小学')
archiv_demo2 = Archivse_table(archiv_id= 15 ,archiv_name='李荣英',archiv_birthday = "1970-2-1",
                        archiv_age=50 ,archiv_gender='女', archiv_degree='文盲' )
archiv_demo3 = Archivse_table(archiv_id= 16 ,archiv_name='王令',archiv_birthday = "1990-3-1",
                        archiv_age=30 ,archiv_gender='男', archiv_degree='高中' )

# 增加多条数据
# session.add(archiv_demo)
# session.add(archiv_demo2)
# session.add(archiv_demo3)
#session.flush()
session.commit()
# 查询数据
see=session.query(Archivse_table).all()
for see in session.query(Archivse_table):
    print(see)
# seee=session.query(Archivse_table).first()
# print(seee)
see1=session.query(Archivse_table.archiv_name).first()
print(see1)
session.commit()

3. 为以下 sql 语句标注执行顺序：
SELECT DISTINCT player_id, player_name, count(*) as num #5 通过SELECT提取我们指定的字段
FROM player JOIN team ON player.team_id = team.team_id #1 先运行player JOIN team，然后通过ON进行筛选
WHERE height > 1.80          #2 通过WHERE去判断一下，哪一个更符合我们的条件
GROUP BY player.team_id      #3 进行分组
HAVING num > 2               #4 对分组产生的分组表进行过滤
ORDER BY num DESC            #6 把提取字段进行相应的排序
LIMIT 2                      #7 限制排序后的数据显示行数

4. 以下两张基于 id 列，分别使用 INNER JOIN、LEFT JOIN、 RIGHT JOIN 的结果是
INNER JOIN 
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
INNER JOIN Table2
ON Table1.id = Table2.id;
结果：根据Table1和Table2共同的id 并取出id 对应的name.
LEFT JOIN
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
LEFT JOIN Table2
ON Table1.id = Table2.id;
结果：根据Table1和Table2共同的id 取出id对应的name外还取出Table1表所有的id和name.
LEFT JOIN
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
LEFT JOIN Table2
ON Table1.id = Table2.id
WHERE Table2.id NULL;
结果：根据Table1和Table2共同的id 取出Table1表id不对应的name，其它值都显示为空.
 RIGHT JOIN
LEFT JOIN
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
RIGHT JOIN Table2
ON Table1.id = Table2.id;
结果：根据Table1和Table2共同的id 取出id对应的name外还取出Table2表所有的id和name.
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
RIGHT JOIN Table2
ON Table1.id = Table2.id
WHERE Table1.id NULL;
结果：根据Table1和Table2共同的id 取出Table2表id不对应的name，其它值都显示为空.
5. 使用 MySQL 官方文档，学习通过 sql 语句为上题中的 id 和 name 增加索引，并验证。根据执行时间，增加索引以后是否查询速度会增加？请论述原因，并思考什么样的场景下增加索引才有效
-- 查询官方文档，了解索引
-- 增加索引：
ALTER TABLE userinfo ADD INDEX (user_id, user_name);
-- 增加索引后的查询：
SELECT * FROM userinfo;
-- 时间：0.127s, 0.135s,0.136s,0.151s,0.154s,0.125s,0.129s,0.136s.0.26s

-- 删除索引：
ALTER TABLE userinfo DROP INDEX user_id;
ALTER TABLE userinfo DROP INDEX user_name;
-- 删除索引后查询：
SELECT * FROM userinfo;
-- 时间：0.171s, 0.403s, 0.144s, 0.151s, 0.159s, 0.157s, 0.137s

-- 反复尝试多次发现没有明显变化。
-- 可能需要当数据量大的时候，同时，索引作为WHERE语句条件的时候才能提升速度。
-- 索引的本质也是一张表，增加索引会降低数据改变的时间。
