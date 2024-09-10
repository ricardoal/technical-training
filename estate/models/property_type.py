from odoo import fields, models

class PropertyType(models.Model):
    _name = "property.type.model"

    name = fields.Char(required=True)
