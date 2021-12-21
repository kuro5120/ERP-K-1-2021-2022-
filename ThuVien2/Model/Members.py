from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    id_card = fields.Char(string='Studient ID', required=True)
    age = fields.Integer(string='Age', track_visibility='always')

    gender = fields.Many2one('library.gender', string='Gender', required=True, track_visibility="always")

    @api.constrains('age')
    def check_age(self):
        for rec in self:
            if rec.age <= 5:
                raise ValidationError(('The age must be greater than 5'))