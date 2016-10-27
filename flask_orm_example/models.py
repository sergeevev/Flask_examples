# -*- coding: utf-8 -*-

from datetime import datetime

from app import db

__author__ = 'sobolevn'


class Product(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(50))
    price = db.Column('price', db.Float)

    date_created = db.Column(
        'date_created', db.DateTime, default=datetime.now
    )

    def __init__(self, name=None, price=None):
        self.name = name
        self.price = price


class Order(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    person_name = db.Column('person_name', db.String(50))

    product_id = db.Column(db.ForeignKey('product.id'))
    product = db.relationship(
        'Product', backref=db.backref('orders', lazy='dynamic')
    )

    date_created = db.Column(
        'date_created', db.DateTime, default=datetime.now
    )
    is_active = db.Column('is_active', db.Boolean, default=True)

    def __init__(self, person_name=None, product=None):
        self.person_name = person_name
        self.product = product
