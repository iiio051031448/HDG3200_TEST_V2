import time
import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, MetaData, Table
from sqlalchemy.orm import sessionmaker

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(funcName)s - %(lineno)d - %(message)s "
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)

Base = declarative_base()


class TLog(Base):
    __tablename__ = 'logs'

    mac = Column(String, primary_key=True)
    operator = Column(String)
    start_time = Column(String)
    end_time = Column(String)
    test_id = Column(String)
    is_repeat = Column(Boolean)
    result = Column(String)
    failed_info = Column(String)
    note = Column(String)

    def __repr__(self):
        return "<User(mac='%s', operator='%s', start_time='%s')>" % (
            self.mac, self.operator, self.start_time)


class SqlSession:
    def __init__(self, sql_db_file):
        self.engin = create_engine(sql_db_file)
        self.metadata = MetaData(self.engin)

        self.logs_table = Table('logs', self.metadata,
                           Column("mac", String(50), primary_key=True),
                           Column("operator", String(50)),
                           Column("start_time", String(32)),
                           Column("end_time", String(32)),
                           Column("test_id", String(32)),
                           Column("is_repeat", Boolean),
                           Column("result", String(32)),
                           Column("failed_info", String(1024)),
                           Column("note", String(1024)))
        self.metadata.create_all()

        self.Session = sessionmaker(bind=self.engin)
        self.session = self.Session()

    def find_item(self, mac):
        log = self.session.query(TLog).filter(TLog.mac == mac).first()
        return log

    def updata_operator(self, t_log, operator):
        t_log.operator = operator
        self.session.commit()

    def update_log(self, t_log, operator, start_time, end_time, test_id, is_repeat, result, failed_info, note=""):
        t_log.operator = operator
        t_log.start_time = start_time
        t_log.end_time = end_time
        t_log.test_id = test_id
        t_log.is_repeat = is_repeat
        t_log.result = result
        t_log .failed_info = failed_info
        t_log .note = note
        self.session.commit()

    def add_log(self, mac, operator, start_time, end_time, test_id, is_repeat, result, failed_info, note=""):
        t_log = self.find_item(mac)
        if not t_log:
            print("NOT FIND ITME : [%s]" % mac)
            t_log = TLog(mac=mac, operator=operator, start_time=start_time,
                         end_time=end_time, test_id=test_id, is_repeat=is_repeat,
                         result=result, failed_info=failed_info, note=note)
            self.session.add(t_log)
            self.session.commit()
        else:
            print("FINDED ITME : [%s]" % mac)
            self.update_log(t_log, operator, start_time, end_time, test_id, is_repeat, result, failed_info, note)
        return t_log


if __name__ == "__main__":
    sql_ses = SqlSession("sqlite:///log.db")

    t_log_new = sql_ses.add_log(mac='11:22:33:44:58:6F', operator="ed", start_time=time.strftime("%Y-%m-%d %H:%M:%S"),
                      end_time=time.strftime("%Y-%m-%d %H:%M:%S"), test_id="HDG201804060001", is_repeat=False,
                      result="成功", failed_info="ALL SUCCESS", note="")

    t_log = sql_ses.find_item("11:22:33:44:58:6F")
    print(t_log)
    if t_log:
        sql_ses.updata_operator(t_log, "刘德华5")


# session.add(ed_user)
# session.commit()
'''
u = session.query(User).filter(User.mac == '11:22:33:44:55:66').first()
print(u)
u.operator = "xman"
session.commit()
'''


