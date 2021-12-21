from odoo import models, fields, api, _

class MemberGender(models.Model):
    _name = 'library.gender'
    _rec_name = 'gender'

    gender = fields.Char('Gender', required=True)

class BookState(models.Model):
    _name = 'book.state'
    _rec_name = 'state'

    state = fields.Char('State', required=True)




