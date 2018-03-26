# -*- coding: utf-8 -*-
import re
from odoo import api, fields, models

class BaseProfile(models.Model):
    _name = "goopay.ewallet.profile.base"
    _description = u'Thông tin hồ sơ khách hàng'

    name = fields.Char(string="Mã",required=True)
    profile_id = fields.Char(string="Định danh", required=True, index=True)

    full_name = fields.Char(string = 'Tên khách hàng')
    email = fields.Char(string="Email",index=True)
    mobile = fields.Char(string="Số di động",index=True )
    passphrase = fields.Char(string ='Passphrase')
    
    profile_type = fields.Selection([
        ('C', 'Cá nhân'),
        ('B', 'Doanh nghiệp'),
        ('P', 'Đối tác'),
        ('I', 'Nội bộ')
        ], default='C',  string='Loại', copy=False, index=True, store=True,
        )
    
    status = fields.Selection([
        ('M', 'Mới'),
        ('A', 'Hoạt động'),
        ('I', 'Không hoạt động'),
        ('L', 'Bị khóa')
        ], default='M',  string='Trạng thái', copy=False, index=True, store=True,
        )