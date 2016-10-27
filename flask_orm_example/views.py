# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request

from forms import ProductForm
from models import Product, Order
from app import db

__author__ = 'sergeevev'

base_views = Blueprint('base_views', __name__, template_folder='templates')
product_views = Blueprint('product_views', __name__, url_prefix='/product')
order_views = Blueprint('order_views', __name__, url_prefix='/order')


@base_views.route('/')
def index():
    return render_template('index.html')

@product_views.route('/create', methods=['GET', 'POST'])
def new_product():
    # product = Product(name=name, price=price)
    # db.session.add(product)
    # db.session.commit()
    #
    # return ('Added {}'.format(product.id))

    if request.method == 'POST':
        form = ProductForm(request.form)
        if form.validate():
            product = Product()
            form.populate_obj(product)

            db.session.add(product)
            db.session.commit()
            print('Saved', product.name, product.price)
        else:
            print('Invalid')
    else:
        form = ProductForm()

        return render_template('product.html', form=form)

@order_views.route('/create', methods=['GET', 'POST'])
def new_order():
    # product = Product.query.filter_by(id=product_id).first()
    # if product:
    #     order = Order(person_name=person_name, product=product)
    #     db.session.add(order)
    #     db.session.commit()
    #     return 'Exists {}, created {}'.format(product.name, order.id)
    #
    # return 'Product does not exist'
    return 'Order created'



