from sqlalchemy import Column, ForeignKey, UniqueConstraint, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
import mysql.connector
import configparser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session

EntityBase = declarative_base()


class DBSessionFactory:
    config = configparser.ConfigParser()
    config.read('./dao/config.ini', encoding='utf-8')
    DB_HOST = config['MySQL']['HOST']
    DB_USER = config['MySQL']['USER']
    DB_PASSWORD = config['MySQL']['PASSWORD']
    DB_NAME = 'mieruka'
    DB_PORT = config['MySQL']['PORT']
    DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    
    @classmethod
    def get_session(cls):
        engine = create_engine(cls.DB_URL, echo = False, pool_pre_ping = True)
        return scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=engine)
        )
        
    @classmethod
    def create_datebase(cls):
        try:
            conn = mysql.connector.connect(host = cls.DB_HOST, user = cls.DB_USER, password = cls.DB_PASSWORD)

            #カーソルを取得
            cursor = conn.cursor()
            #executeは引数をSQL文として実行する。
            cursor.execute('CREATE DATABASE '+ cls.DB_NAME)
            #すでにあるときにエラー
               
        except mysql.connector.errors.DatabaseError :
            print('すでにデータベースが存在しています')

        finally:#どっちにしろ、add(Create)の作業に進む
            database = cls.DB_NAME
            engine = create_engine('mysql+pymysql://'+cls.DB_USER+':'+cls.DB_PASSWORD+'@'+cls.DB_HOST+'/' + database,echo=False)
            db_session = scoped_session(
                sessionmaker(
                    autocommit = False,
                    autoflush = False,
                    bind = engine
                )
        )
            EntityBase.metadata.create_all(bind=engine)
        
        
class DaoBase:
    def __init__(self, session):
        self.session = session
        EntityBase.query = session.query_property()
        



"""
try:
    conn = mysql.connector.connect(host = HOST, user = USER, password = PASSWORD)

#カーソルを取得
    cursor = conn.cursor()
#executeは引数をSQL文として実行する。
    cursor.execute('CREATE DATABASE '+ TRIAL_NAME)
#すでにあるときにエラー   
except mysql.connector.errors.DatabaseError :
    print('すでにデータベースが存在しています')

finally:#どっちにしろ、add(Create)の作業に進む
    database = TRIAL_NAME
    engine = create_engine('mysql+pymysql://'+USER+':'+PASSWORD+'@'+HOST+'/' + database,echo=False)
    db_session = scoped_session(
        sessionmaker(
            autocommit = False,
            autoflush = False,
            bind = engine
        )
    )

    Base = declarative_base()
    Base.query = db_session.query_property()

    class Customer(Base):
        __tablename__ = 'customer'
        customer_id = Column(Integer, primary_key = True, index = True)
        customer_name = Column(String(100), unique = True,  nullable=False)
        address = Column(String(100), unique = False, nullable=False)
        latitude = Column(String(12), unique = False, nullable=False)
        longitude = Column(String(12), unique = False, nullable=False)

    class Predictive_val_today(Base):
        __tablename__ = 'predictive_val_today'
        predictive_val_today_id = Column(Integer, primary_key = True, nullable = False, index = True)
        today = Column(DateTime, nullable = False)
        koma_1 = Column(Float, nullable = False)
        koma_2 = Column(Float, nullable = False)
        koma_3 = Column(Float, nullable = False)
        koma_4 = Column(Float, nullable = False)
        koma_5 = Column(Float, nullable = False)
        koma_6 = Column(Float, nullable = False)
        koma_7 = Column(Float, nullable = False)
        koma_8 = Column(Float, nullable = False)
        koma_9 = Column(Float, nullable = False)
        koma_10 = Column(Float, nullable = False)
        koma_11 = Column(Float, nullable = False)
        koma_12 = Column(Float, nullable = False)
        koma_13 = Column(Float, nullable = False)
        koma_14 = Column(Float, nullable = False)
        koma_15 = Column(Float, nullable = False)
        koma_16 = Column(Float, nullable = False)
        
"""