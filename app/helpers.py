import datetime

from app.models import Subscriber, PhoneNumber, Payment
from app.database import Base, engine, session

from sqlalchemy import update


def start():
    Base.metadata.create_all(engine)

    objects = [
        Subscriber(type="физлицо", name="Пушка", address="улица пушкина"),
        Subscriber(type="физлицо", name="Ленский", address="улица пушкина2"),
        PhoneNumber(subscriber_id=1, is_active=True, number="9393992329"),
        Payment(phone_number_id=1, date=datetime.datetime.now(), amount=100, subscriber_id=1)
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

def find_user_by_id(sub_id):
    subscriber = session.query(Subscriber).where(Subscriber.id == sub_id).first()

    return subscriber.to_json()

def to_add_new_subscriber(data):
    new_sub = Subscriber(type=data["type"], name=data["name"], address=data["address"])

    session.add(new_sub)
    session.commit()

    return new_sub.to_json()

def to_delete_subscriber(sub_id):
    subsriber = session.query(Subscriber).where(Subscriber.id == sub_id).one()

    session.delete(subsriber)
    session.commit()

    return subsriber.to_json()

def to_change_user_by_id(sub_id, data):
    updated_sub = update(Subscriber).where(Subscriber.id == int(sub_id)).values(data)
    res = session.execute(updated_sub)
    session.commit()

    subscriber = session.query(Subscriber).where(Subscriber.id == sub_id).one()

    return subscriber.to_json()

def find_payments_by_sub(sub_id):
    payments = session.query(Payment).filter(Payment.subscriber_id == sub_id).all()
    result = []
    for payment in payments:
        data = payment.to_json()
        data["phone_number"] = payment.phone_number.number
        result.append(data)
    return result

def to_add_new_payment(data):
    new_payment = Payment(phone_number_id=data["phone_number_id"], date=datetime.datetime.now(), amount=data["amount"], subscriber_id=data["subscriber_id"])

    session.add(new_payment)
    session.commit()

    return new_payment.to_json()