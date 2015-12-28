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

class td_car(models.Model):
    _name = 'td.car'
    _description = 'Tecdoc car'


    name = fields.Char('Name', compute='_conc_name', store=True)

    #name = fields.Char('Car from tecdoc')
    td_car_brand_id = fields.Many2one('td.car.brand','brand')
    td_car_model_id = fields.Many2one('td.car.model', 'model')
    td_car_modif_id = fields.Many2one('td.car.modif', 'modification')
    fuel_type = fields.Char(comodel='td.car.modif', related='td_car_modif_id.fuel_type', string="Fuel type")
    engine = fields.Char(comodel='td.car.modif', related='td_car_modif_id.engine', string="Engine")
    years = fields.Char(comodel='td.car.modif', related='td_car_modif_id.years', string="Years")
    power = fields.Char(comodel='td.car.modif', related='td_car_modif_id.power', string="Power")

    @api.one
    @api.depends(
        'name',
        'td_car_brand_id',
        'td_car_model_id',
        'td_car_modif_id',
    )
    def _conc_name(self):
        self.name =  unicode(self.td_car_brand_id.name)+" "+ unicode(self.td_car_model_id.name) + " " + unicode(self.td_car_modif_id.name)

    

class td_car_brand(models.Model):
    _name = 'td.car.brand'
    _description = 'Contains tecdoc car brands'

    name = fields.Char('Brand', required=True)

class td_car_model(models.Model):
    _name = 'td.car.model'
    _description = 'Contains tecdoc car models'

    name = fields.Char('Model', required=True)

class td_car_modif(models.Model):
    _name = 'td.car.modif'
    _description = 'Contains tecdoc car modifications'

    name = fields.Char('Modification', required=False)
    fuel_type = fields.Char('Fuel type')
    engine = fields.Char('Engine')
    years = fields.Char('Years')
    cabin = fields.Char('Cabin')
    power = fields.Char('Power')

