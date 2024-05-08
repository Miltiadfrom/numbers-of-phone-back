import datetime

from .models import Subscriber, PhoneNumber, Payment
from .database import Base, engine, session


def start():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    objects = [
        Subscriber(type="физлицо", name="Слава", address="улица пушкина"),
        PhoneNumber(subscriber_id=1, is_active=True, number="9393992329"),
        Payment(phone_number_id=1, date=datetime.datetime.now(), amount=100)
    ]

    session.bulk_save_objects(objects)
    session.commit()

def find_users():
    result = []

    for subscriber in session.query(Subscriber).all():
        result.append(subscriber.to_json())
    return result

def find_phones_by_sub(sub):
    phones = session.query(PhoneNumber).filter(PhoneNumber.subscriber_id == sub).all()
    return [phone.to_json() for phone in phones]

def to_add_phone_by_sub(data):
    new_phone = PhoneNumber(subscriber_id=data["sub"], is_active=True, number=data["number"])

    session.add(new_phone)
    session.commit()

    return new_phone.to_json()

def to_delete_phone_by_name(number):
    phone = session.query(PhoneNumber).where(PhoneNumber.number == number).one()

    session.delete(phone)
    session.commit()

    return phone.to_json()