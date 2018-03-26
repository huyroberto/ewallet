# -*- coding: utf-8 -*-
{
    'name': 'Payment Gateway',
    'version': '2.0',
    'category': 'Accounting',
    'sequence': 95,
    'summary': 'Payment Gateway - Administration System',
    'description': 'GooPay - Payment Gateway',
    'author':'Hapi Solutions',
    'website': 'http://erp.hapi.solutions',
    'depends': ['base','hr'],
    'data': [
        #'security/ir.model.access.csv',
        'views/profiles.xml',
        'views/settings.xml',
        'views/menus.xml'
        #'views/quotation_workflow.xml',
        #'views/payment_workflow.xml'
    ],
    #’demo': ['data/hr_expense_demo.xml'],
    'installable': True,
    'application': True,
}
