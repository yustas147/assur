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

from openerp import models, fields, api
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
    
    

class assur_obj(models.Model):
# stores info about real assurance objects: my car, his house etc.
    _name = 'assur.obj'
    _description = 'Contains different assurance objects'

    name = fields.Char('Assurance object', required=True)
    otype = fields.Many2one('assur.obj.otype','otype')
    obj_prop_vals = fields.One2many('assur.obj.prop.val','assur_obj_id', string='Assur obj property values')
    obj_props = fields.Many2many(comodel_name='assur.obj.prop',relation='assur_obj_prop_val',column1='assur_obj_id',column2='assur_obj_prop_id')
    is_auto = fields.Boolean(string="Is it automobile?")
    automodel = fields.Many2one('td.car', string='Automobile select')

class assur_obj_prop(models.Model):
# stores info about possible object`s properties
    _name = 'assur.obj.prop'
    _description = 'Contains different assurance object properties'

    name = fields.Char('Assurance object`s property', required=True)
    otype = fields.Many2one('assur.obj.otype','otype')
    #vals = fields.



class assur_obj_prop_val(models.Model):
# stores info about oject`s values
    _name = 'assur.obj.prop.val'
    _description = 'Contains real values of assurance object`s properties'

    name = fields.Char('Assurance object`s property Values', required=True)
    assur_obj_id = fields.Many2one('assur.obj', string='Assurance object')
    assur_obj_prop_id = fields.Many2one('assur.obj.prop', string='Assurance object property')
    assur_obj_prop_val_otype = fields.Many2one('assur.obj.otype', related='assur_obj_id.otype', string='Assur obj type')

class assur_company(models.Model):
    _name = 'assur.company'
    _description = 'Assur companies info: assur. prop. coefficients'

    def get_coeffs(self, assur_obj_id):
# take object data, assur.prop.otype.company.assur_cpoargs_data, assur_cpoargs_func and
# calculate coefficient
        return True

    name = fields.Char('Assurance company name:', required=True)
    assur_prop_otype_company_ids = fields.One2many('assur.prop.otype.company','assur_company_id', string='Company`s properties')
    

class assur_prop_otype_company(models.Model):
# info about assur company`s data and methods to produce coefficients
    _name = 'assur.prop.otype.company'
    _description = 'Stores info about prop/type coeff. calculation'
    
    name = fields.Char(compute='_get_conc_name', store=True)
    assur_company_id = fields.Many2one('assur.company', string='Assur company')
    assur_prop_id = fields.Many2one('assur.obj.prop', string='Assur property')
    assur_otype_id = fields.Many2one('assur.obj.otype', string='Assur otype')
    assur_cpoargs_data = fields.Text()
    assur_cpoargs_func = fields.Text()

    @api.one
    @api.depends(
        'name',
        'assur_company_id',
        'assur_otype_id',
        'assur_prop_id',
    )
    def _get_conc_name(self):
        self.name =  unicode(self.assur_otype_id.name)+": "+ unicode(self.assur_prop_id.name) + ": " + unicode(self.assur_company_id.name)
