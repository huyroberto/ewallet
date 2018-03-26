# -*- coding: utf-8 -*-
import re
from odoo import api, fields, models

class Transaction(models.Model):
    _name = "goopay.ewallet.transaction.base"
    _description = u'Thông tin giao dịch'

    name = fields.Char(string = 'Mã giao dịch', readonly = True)
    note = fields.Text(string = 'Ghi chú')

    product = fields.Many2one('goopay.ewallet.service.product', string = 'Sản phẩm', require=True)
    profile = fields.Many2one('goopay.ewallet.profile.base','Khách hàng')

    product_amount = fields.Float(string = 'Số tiền')

    discount_rate = fields.Float(string = 'Mức chiết khấu', default = 0)
    discount_amount = fields.Float(string = 'Chiết khấu')

    fee_amount = fields.Float(string = 'Phí giao dịch', default = 0)
    total_amount = fields.Float(string = 'Tổng tiền', compute='_get_total_amount',store=True)

    @api.multi
    @api.depends('product_amount','discount_amount', 'fee_amount')
    def _get_total_amount(self):
        self.total_amount = product_amount - discount_amount + fee_amount


