from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Subscriber(Base):
    __tablename__ = 'subscribers'

    id = Column(Integer, primary_key=True)
    type = Column(String)
    name = Column(String)
    address = Column(String)

    phone_numbers = relationship("PhoneNumber", back_populates="subscriber")
    payments = relationship("Payment", back_populates="subscriber")

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class PhoneNumber(Base):
    __tablename__ = 'phone_numbers'

    id = Column(Integer, primary_key=True)
    number = Column(String)
    subscriber_id = Column(Integer, ForeignKey('subscribers.id'))
    is_active = Column(Boolean)

    subscriber = relationship("Subscriber", back_populates="phone_numbers")
    payments = relationship("Payment", back_populates="phone_number")

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    phone_number_id = Column(String, ForeignKey('phone_numbers.id'))
    date = Column(Date)
    amount = Column(Integer)

    phone_number = relationship("PhoneNumber", back_populates="payments")
    subscriber_id = Column(Integer, ForeignKey('subscribers.id'))
    subscriber = relationship("Subscriber", back_populates="payments")

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

