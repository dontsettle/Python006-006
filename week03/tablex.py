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


