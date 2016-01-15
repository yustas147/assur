# -*- coding: utf-8 -*-
'''
Created on 14 ���. 2016 �.

@author: yustas
'''
from openerp.osv import fields, osv

class sale_order(osv.osv):
    _inherit = 'sale.order'
   
   
    def set_price_unit(self, cr, uid, ids, context = False): 
        curr_sale_ord = self.browse(cr, uid, ids)[0]
        strobj = curr_sale_ord.str_obj
        for ol in curr_sale_ord.order_line:
            strahovajka = ol.product_id.seller_ids[0].name.insur_id
            koeff = strobj.calc_coeff(strahovajka)
            newprice = koeff*ol.product_id.list_price
            ol.write({'price_unit':newprice})
        return True
            
    
    def get_coeffs(self, cr, uid, ids, context = False):
        curr_sale_ord = self.browse(cr, uid, ids)[0]
        strobjpool = self.pool.get('assur.obj')
        obj_inst = strobjpool.browse(cr, uid, [curr_sale_ord.str_obj.id])[0]
        #ass_info = obj_inst.calc_co()
        curr_sale_ord.write({'note':obj_inst.calc_co()})
#        curr_sale_ord.write({'note':ass_info})
        return True

    _columns = {
                'is_strah':fields.boolean(string='Is it strahovka?'),
                'str_obj':fields.many2one('assur.obj', string="Object strahovaniya"),
                }
