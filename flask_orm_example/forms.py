# -*- coding: utf-8 -*-

from wtforms_alchemy import ModelForm

from models import Product

__author__ = 'sergeevev'


class ProductForm(ModelForm):
    class Meta:
        model = Product
        only = ['price', 'name']