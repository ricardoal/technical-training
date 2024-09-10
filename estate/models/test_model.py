from odoo import fields, models

class TestModel(models.Model):
    _name = "test.model"
    _description = "Test Model"
    _postcode = "Test Model"
    _date_availability = "Test Model"
    _expected_price = "Test Model"
    _selling_price = "Test Model"
    _bedrooms = "Test Model"
    _living_area = "Test Model"
    _facades = "Test Model"
    _garage = "Test Model"
    _garden = "Test Model"
    _garden_area = "Test Model"
    _garden_orientation = "Test Model"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()    
    date_availability = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Type',
        selection=[('North', 'North'), ('South', 'South'),('East', 'East'), ('West', 'West')]
    )

