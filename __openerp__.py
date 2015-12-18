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
{
    'name' : 'Assurance',
    'version' : '0.1',
    'author' : 'Simbioz',
    'sequence': 110,
    'category': 'Managing ass, ass-calculator, etc. ',
    'website' : 'https://simbioz.com.ua/fleet',
    'summary' : 'Assurance, calculator, management',
    'description' : """
Assurance management
==================================
With this module, we help you managing all your assurances

Main Features
-------------
* Add ass objects 
""",
    'depends' : [
        'base',
        'crm',
        'sale'
    ],
    'data' : [
        'ass_view.xml',
      #  'ass_obj',
    ],

    'demo': [],
    #'demo': ['fleet_demo.xml'],

    'installable' : True,
    'application' : False,
}
