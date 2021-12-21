# -*- coding: utf-8 -*-

from odoo import fields,models

class ProductTemplateInherit(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    book_state = fields.Many2one('book.state', string='State', required=True, track_visibility="always")

    book_author = fields.Char(string='Author')
    book_publisher = fields.Char(string='publisher')
    book_isbn = fields.Char('ISBN')
    book_publish = fields.Date(string='Publish Day', required=True)
