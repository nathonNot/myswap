from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from . import Base


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
    exchange_id = Column(Integer, ForeignKey("s_exchanges.id"))
    api_key = Column(String)
    api_secret = Column(String)
    api_passphrase = Column(String)