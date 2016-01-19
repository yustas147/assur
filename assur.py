# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import api, models, fields
#from openerp.osv import models, fields, osv
#import time
#import datetime
#from openerp import tools
#from openerp.osv.orm import except_orm
#from openerp.tools.translate import _
#from dateutil.relativedelta import relativedelta



class assur_obj_otype(models.Model):
    _name = 'assur.obj.otype'
    _description = 'Contains top-level types of assurance objects'

    name = fields.Char('Assurance object type', required=True)
    int_name = fields.Char('Internal object type name', required=True)
    properties = fields.Many2many(comodel_name='assur.obj.prop',relation='otype_prop_rel',column1='otype_id', column2='prop_id')
    
    

class assur_obj(models.Model):
# stores info about real assurance objects: my car, his house etc.
    _name = 'assur.obj'
    _description = 'Contains different assurance objects'

    name = fields.Char('Assurance object', required=True)
    otype = fields.Many2one('assur.obj.otype','otype')
    obj_prop_vals = fields.One2many('assur.obj.prop.val','assur_obj_id', string='Assur obj property values')
    obj_props = fields.Many2many(comodel_name='assur.obj.prop',relation='assur_obj_prop_val_rel',column1='assur_obj_id',column2='assur_obj_prop_id',
                                 domain="['assur_obj_prop_val_otype', '=', 'otype' ]")
    is_auto = fields.Boolean(string="Is it automobile?")
    automodel = fields.Many2one('td.car', string='Automobile select')
    strahinfo_display = fields.Text('Strahinfo', default='Nothing to display')
    
    @api.multi
    @api.model
    def create_prop_vals(self):
        props = self.otype.properties
        prp_ids = [p.id for p in props]
        
        prop_vals = self.env['assur.obj.prop.val']
        pr_alr_set = set([p.assur_obj_prop_id.id for p in self.obj_prop_vals])
        print prp_ids
        print pr_alr_set
        unset_props = set(prp_ids) - pr_alr_set
        print unset_props
        for prpid in unset_props:
   #         print self.ids
   #         print prpid
   #         print self.otype.id
            prop_vals.create({'name':'', 'assur_obj_id':self.id, 'assur_obj_prop_id':prpid, 'assur_obj_prop_val_otype':self.otype.id})
            
            
        return True
        
    
   # engine_size_in_litres = fields.Float(string='Объем двигателя в литрах',comodel_name='assur.obj.prop.val', related )
    
#     @api.onchange('auto_engine_size_in_litres') # if these fields are changed, call method
#     def check_change(self):
#         if self.field1 < self.field2:
#         self.field3 = True


    
    @api.multi
    def calc_str(self):
        # get prop types set
        p_v_set = []
        for opv in self.obj_prop_vals:
            p_v_set.append(opv)  
        if p_v_set:
            self.strahinfo_display = unicode(p_v_set)
        return True
    
    @api.multi
    @api.model
    def calc_co(self):
        res={}
        ass_cos = self.env['assur.company'].search([])
        for assco in ass_cos:
            resco = assco.calc_obj_pvs(self)
            print unicode(resco)
            res[assco.name] = unicode(resco)
        print res
        txt = ''
        for k in res.keys():
           txt += k + ": " + res[k] + '\n' 
            
        self.strahinfo_display = txt
#        self.strahinfo_display = unicode(res)
        return res

    @api.multi
    @api.model
    def calc_coeff(self, ins_company):
#         for assco in ass_cos:
#             resco = assco.calc_obj_pvs(self)
#             print unicode(resco)
#             res[assco.name] = unicode(resco)
        return ins_company.calc_obj_pvs(self)

# class aobj_auto_light(models.Model):
#     _name = 'aobj.auto.light'
#     _inherits = {'assur.obj':'obj_id'}
#     
#     obj_id = fields.Many2one('assur.obj')
#     auto_engine_size_in_litres = fields.Float(string='Объем двигателя в литрах')
    

class assur_obj_prop(models.Model):
# stores info about possible object`s properties
    _name = 'assur.obj.prop'
    _description = 'Contains different assurance object properties'

    name = fields.Char('Assurance object`s property', required=True)
    #otype = fields.Many2one('assur.obj.otype','otype')
    otypes = fields.Many2many(comodel_name='assur.obj.otype',relation='otype_prop_rel',column2='otype_id', column1='prop_id')
    #vals = fields.



class assur_obj_prop_val(models.Model):
# stores info about oject`s values
    _name = 'assur.obj.prop.val'
    _description = 'Contains real values of assurance object`s properties'

    name = fields.Char('OPValue', required=True)
    assur_obj_id = fields.Many2one('assur.obj', string='Assurance object')
    assur_obj_prop_id = fields.Many2one('assur.obj.prop', string='Assurance object property')
    assur_obj_prop_val_otype = fields.Many2one('assur.obj.otype', related='assur_obj_id.otype', string='Assur obj type')

# class contract_type(models.model):
#     _name = 'contr.type'
#     _description = 'Info specific to contract types'
    
    #name = fields.Char('Contract type')
class assur_company(models.Model):
    _name = 'assur.company'
    _description = 'Assur companies info: assur. prop. coefficients'

# take object data, assur.prop.otype.company.assur_cpoargs_data, assur_cpoargs_func and
# calculate coefficient

    name = fields.Char('Assurance company name:', required=True)
    assur_prop_otype_company_ids = fields.One2many('assur.prop.otype.company','assur_company_id', string='Company`s properties')
    
    @api.multi    
    @api.model
    def calc_prop_for_value(self, obj_id):
        # берем объект страховки из объекта страховой компании и обсчитываем его коэффициенты
#        env = api.Environment()
        obj_model = self.env['assur.obj']
        obj_rec = obj_model.browse(obj_id)
        otype_id = obj_rec.otype.id    
        #print "Object type id is: "+unicode(obj_rec.otype.id)
        #print "Object type name is: "+unicode(obj_rec.otype.name)
        res=1
#        res=[]
#        for opval in obj_rec.obj_prop_vals:
        pocsenv = self.env['assur.prop.otype.company']
        this_co_id = self.id
        aspi = [opv.assur_obj_prop_id.id for opv in obj_rec.obj_prop_vals]
        pocs = pocsenv.search([('assur_company_id','=',this_co_id),('assur_otype_id','=',obj_rec.otype.id),('assur_prop_id','in', aspi)])
        for opval in obj_rec.obj_prop_vals:
            for poc in pocs:
                if poc.assur_otype_id == opval.assur_obj_prop_val_otype and poc.assur_prop_id == opval.assur_obj_prop_id:
                    resi = poc.calc_coeff(opval.name)[0]
                    res *= resi
        return res

    @api.multi    
    @api.model
    def access_obj_pvs(self):
#        env = api.Environment()
        objpool = self.env['assur.obj']
        for objrec in objpool.search([]):
            self.calc_prop_for_value(objrec.id)
        return True

    @api.multi
    @api.model
    def calc_obj_pvs(self, assobj):
        return self.calc_prop_for_value(assobj.id)

class assur_prop_otype_company(models.Model):
# info about assur company`s data and methods to produce coefficients
    _name = 'assur.prop.otype.company'
    _description = 'Stores info about prop/type coeff. calculation'
    
    name = fields.Char(compute='_get_conc_name', store=True)
    assur_company_id = fields.Many2one('assur.company', string='Assur company')
    assur_prop_id = fields.Many2one('assur.obj.prop', string='Assur property')
    assur_otype_id = fields.Many2one('assur.obj.otype', string='Assur otype')
    assur_cpoargs_data = fields.Text()
    assur_cpoargs_func = fields.Text(default='def calcu(val):\n    return 1')
    
    @api.one
    def calc_coeff(self, val):
#        def calc():
#            return True
        exec(self.assur_cpoargs_func)
        return float(calcu(val))
#        return calcu(val)

    @api.one
    @api.depends(
        'name',
        'assur_company_id',
        'assur_otype_id',
        'assur_prop_id',
    )
    def _get_conc_name(self):
        self.name =  unicode(self.assur_otype_id.name)+": "+ unicode(self.assur_prop_id.name) + ": " + unicode(self.assur_company_id.name)

class assur_calc(models.Model):
    _name = 'assur.calc'
    _description = 'Calculates object`s insuranse price'
    
    assur_obj_id = fields.Many2one('assur.obj')
    assur_company_id = fields.Many2one('assur.company')
    assur_calc_txt = fields.Text("Results:", default='assur_calc_txt')
    _defaults = { 'assur_calc_txt': 'nothing'}

    @api.multi
    def calc_coeff(self):
        print unicode(self.assur_calc_txt)
        self.write({'assur_calc_txt':self.assur_calc_txt+'_(-_-)'}) 
        print 'print from calc_coeff: '+unicode(self.assur_calc_txt)
        return True


