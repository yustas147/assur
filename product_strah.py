# -*- coding: utf-8 -*-
'''
Created on 19 ���. 2016 �.

@author: yustas
'''
from openerp.osv import fields, osv
from openerp.tools.translate import _

class product_product(osv.osv):
    '''
    classdocs
    '''
    _inherit = 'product.product'
    _columns = {
                'product_otype': fields.many2many('assur.obj.otype','product_otype_rel'),
                'is_it_strah': fields.boolean(string='Eto strahovka?'),
                }