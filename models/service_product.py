# -*- coding: utf-8 -*-
import re
from odoo import api, fields, models

class Service(models.Model):
    _name = "goopay.ewallet.service.base"
    _description = u'Thông tin dịch vụ'

    name = fields.Char(string = "Tên dịch vụ")
    description = fields.Char(string = 'Mô tả')

    products = fields.One2many('goopay.ewallet.service.product','service', string = 'Các sản phẩm')

class ServiceProduct(models.Model):
    _name = "goopay.ewallet.service.product"
    _description = u'Thông tin sản phẩm'
    
    name = fields.Char(string = "Mã sản phẩm")
    description = fields.Char(string = 'Tên sản phẩm')

    # CÁC LIÊN KẾT TỚI ĐỐI TƯỢNG KHÁC
    service = fields.Many2one('goopay.ewallet.service.base',string='Dịch vụ', required=True)
    provider = fields.Many2one('goopay.ewallet.service.provider',string='Nhà cung cấp', required=True)
    parent = fields.Many2one('goopay.ewallet.service.product',string ='Sản phẩm chính')

    sub_products = fields.One2many('goopay.ewallet.service.product','parent',string ='Sản phẩm con')

class ServiceProvider(models.Model):
    _name = "goopay.ewallet.service.provider"
    _description = u'Thông tin nhà cung cấp dịch vụ'

    name = fields.Char(string = "Mã")
    description = fields.Char(string = 'Tên nhà cung cấp')

    products = fields.One2many('goopay.ewallet.service.product','provider', string = 'Các sản phẩm')