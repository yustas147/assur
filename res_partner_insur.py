# -*- coding: utf-8 -*-
'''
Created on 15 ���. 2016 �.

@author: yustas
'''

from openerp.osv import fields, osv

class res_partner(osv.osv):
    _inherit = 'res.partner'
    
    _columns = {
                'isit_strah':fields.boolean(string='Is it insurance co?'),
                'insur_id':fields.many2one('assur.company', string='Insurance company')
                }
