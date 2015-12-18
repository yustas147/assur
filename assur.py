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

from openerp import models, fields
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
    _name = 'assur.obj'
    _description = 'Contains different assurance objects'

    name = fields.Char('Assurance object', required=True)
    otype = fields.Many2one('assur.obj.otype','otype')
    obj_prop_vals = fields.One2many('assur.obj.prop.val','assur_obj_id', string='Assur obj property values')
    obj_props = fields.Many2many(comodel_name='assur.obj.prop',relation='assur_obj_prop_val',column1='assur_obj_id',column2='assur_obj_prop_id')

class assur_obj_prop(models.Model):
    _name = 'assur.obj.prop'
    _description = 'Contains different assurance object properties'

    name = fields.Char('Assurance object`s property', required=True)
    #vals = fields.

class assur_obj_prop_val(models.Model):
    _name = 'assur.obj.prop.val'
    _description = 'Contains real values of assurance object`s properties'

    name = fields.Char('Assurance object`s property Values', required=True)
    assur_obj_id = fields.Many2one('assur.obj', 'Assurance object')
    assur_obj_prop_id = fields.Many2one('assur.obj.prop', 'Assurance object property')
    assur_obj_prop_val_otype = fields.Many2one('assur.obj.otype', related='assur_obj_id.otype')
