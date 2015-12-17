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

from openerp.osv import fields, osv
#import time
#import datetime
from openerp import tools
from openerp.osv.orm import except_orm
#from openerp.tools.translate import _
#from dateutil.relativedelta import relativedelta

class assur_obj(osv.Model):
    _name = 'assur.obj'
    _description = 'Contains different assurance objects'

    _columns = {
        'name':fields.char('Assurance object', required=True),
    }

class assur_obj_prop(osv.Model):
    _name = 'assur.obj.prop'
    _description = 'Contains different assurance object properties'

    _columns = {
        'name':fields.char('Assurance object`s property', required=True),
    }

class assur_obj_prop_value(osv.Model):
    _name = 'assur.obj.prop.value'
    _description = 'Contains real values of assurance object`s properties'

    _columns = {
        'name':fields.char('Assurance object`s property', required=True),
        'assur_obj_id':fields.many2one('assur.obj', 'Assurance object'),
        'assur_obj_prop_id':fields.many2one('assur.obj.prop', 'Assurance object property'),
    }
