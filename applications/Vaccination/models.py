from datetime import datetime

from applications import db


class VaccinationModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String)
    iso_code = db.Column(db.String)
    date = db.Column(db.DATE)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    @classmethod
    def insert_row(cls, country, iso_code, date):
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        date_obj = date_obj.date()

        instance = cls(country=country, iso_code=iso_code, date=date_obj)
        db.session.add(instance)
        db.session.commit()

        return instance

class User(db.Model):
    id= db.Column(db.Integer, primary_key=True)

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)