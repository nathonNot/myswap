import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Double, DateTime
from sqlalchemy.orm import relationship

from . import Base, get_db, get_db_session


class User(Base):
    __tablename__ = "u_users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


class Exchange(Base):
    __tablename__ = "s_exchanges"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


class UserExchange(Base):
    __tablename__ = "u_user_exchanges"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("u_users.id"))
    exchange = Column(String)
    api_key = Column(String)
    api_secret = Column(String)
    api_passphrase = Column(String)


def get_user_exchange(user_id: int, exchange_name: str):
    db = get_db_session()

    user_exchange = db.query(UserExchange).filter(
        UserExchange.user_id == user_id).filter(UserExchange.exchange == exchange_name).first()
    db.close()
    return user_exchange


class UserFundsChange(Base):
    __tablename__ = "u_user_funds_changes"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("u_users.id"))
    exchange = Column(String, comment='交易所')
    change_num = Column(Double, comment='变化数量')
    ext = Column(String, comment='备注')
    # 结算货币
    currency = Column(String, comment='结算货币')
    create_time = Column(
        DateTime, default=datetime.datetime.now, comment='创建时间')

    def __init__(self, user_id: int, exchange: str, change_num: float, ext: str, currency: str = "usdt"):
        self.user_id = user_id
        self.exchange = exchange
        self.change_num = change_num
        self.ext = ext
        self.currency = currency

    def save(self):
        db = get_db_session()
        db.add(self)
        db.commit()
        db.close()
