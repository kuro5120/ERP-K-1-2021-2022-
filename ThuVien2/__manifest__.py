# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Thu Vien 2',
    'version': '1.0',
    'summary': 'Module for managing the library',
    'sequence': '10',
    'description': """""",
    'category': 'extral tool',
    'depends': ['sale', 'product', 'hr', 'base', 'mail'],
    'data': [
        'Views\Member_view.xml',
        'Views\Book_view.xml',
        'Views\Librarian_view.xml',
        'Views\Borrow_view.xml',
        'Views\Configuration_view.xml',
        'Views\Menu_item.xml',
        'Data\Sequence.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}