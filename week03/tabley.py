import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String,DateTime,Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
# 实例一个引擎
dburl = "mysql+pymysql://root:123456@localhost/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=True, encoding="utf-8")


class Ar_table(Base):
    __tablename__ = 'archivse4'
    ar_id = Column(Integer(), primary_key=True)
    ar_name = Column(String(50), index=True)
    age = Column(Integer())
    birthday = Column(Date(), nullable=False)
    sex = Column(String(10))
    education = Column(String(50))
    create_time = Column(DateTime(), default=datetime.now)
    update_time = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return (f"{self.ar_id}, {self.ar_name}, {self.age}, {self.birthday}, "
                f"{self.sex}, {self.education}, {self.education}, "
                f"{self.create_time}, {self.update_time}")
try:
    Base.metadata.create_all(engine)
except Exception as e:
    print("create error {e}")

# 创建session
SessionClass = sessionmaker(bind=engine)
session = SessionClass()

# 增加数据
user_add1 = Ar_table(
        ar_id=110,
        ar_name="王令",
        age=2,
        birthday="1960-01-01",
        sex="man",
        education="n")

user_add2 = Ar_table(
        ar_id=111, 
        ar_name="lm",
        age=30,
        birthday="1970-01-01",
        sex="wman",
        education="e")

user_add3 = Ar_table(
        ar_id=121,
        ar_name="wl",
        age=29,
        birthday="1990-01-01",
        sex="man",
        education="m")
session.add(user_add1)
session.add(user_add2)
session.add(user_add3)
session.commit()

#查询
# for result in session.query(User_table):
#     print(result)
session.commit()

