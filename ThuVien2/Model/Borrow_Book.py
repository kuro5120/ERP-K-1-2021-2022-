# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class BorrowBook(models.Model):
    _name = 'library.borrow'
    _inherit = ['mail.thread.cc',
                'mail.activity.mixin']
    _description = 'Borrow book'
    _rec_name = 'name'
    _order = "id desc"

    name = fields.Char(string='Borrow ID', required=True, copy=False, readonly=True,
                       index=True, default=lambda self:_('New'))

    member_id = fields.Many2one('res.partner', string='Member', required=True)
    member_age = fields.Integer('Age', related='member_id.age')
    member_address = fields.Char('Address', related='member_id.street')
    member_phone = fields.Char('Phone', related='member_id.phone')
    student_id = fields.Char('Studient ID', related='member_id.id_card')

    librarian_id = fields.Many2one('hr.employee', string='librarian', required=True)
    librarian_phone = fields.Char('Phone', related='librarian_id.work_phone')
    librarian_email = fields.Char('Email', related='librarian_id.work_email')

    borrow_date = fields.Date(string='Borrow Date', required=True)
    return_date = fields.Date(string='Return Date', required=True)

    borrow_state = fields.Selection([('draft', 'Draft'),
                                     ('borrowing', 'Borrowing'),
                                     ('return', 'Return')
                                     ], default='draft', sting='State', readomly=True)

    borrow_line = fields.One2many('library.borrow.line', 'borrow_id', string='borrow line')

    librarian_notes = fields.Text(string="Librarian Notes")

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('library.borrow.sequence') or _('New')
        result = super(BorrowBook, self).create(vals)
        return result

    def borrow_confirm(self):
        for rec in self:
            rec.borrow_state = 'borrowing'

    def borrow_done(self):
        for rec in self:
            rec.borrow_state = 'return'

class BorrowLine(models.Model):
    _name = 'library.borrow.line'
    _description = 'Borrow line'

    book_id = fields.Many2one('product.template', string='Books', required=True)
    book_author = fields.Char('Author', related='book_id.book_author')
    book_publisher = fields.Char('Publisher', related='book_id.book_publisher')
    book_isbn = fields.Char('ISBN', related='book_id.book_isbn')

    borrow_id = fields.Many2one('library.borrow', string='Borrow ID')

    return_date = fields.Date(string='Return Date')

    borrow_state = fields.Selection([('borrowing', 'Borrowing'),
                                     ('return', 'Return')
                                     ], default='borrowing', sting='State', readomly=True)

    def borrow_return(self):
        for rec in self:
            rec.borrow_state = 'return'
