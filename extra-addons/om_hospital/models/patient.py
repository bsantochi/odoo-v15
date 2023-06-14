# -*- coding: utf-8 -*-
from odoo import api, fields, models
from datetime import date


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = "mail.thread", 'mail.activity.mixin'
    _description = "Hospital Patient"

    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date(string='Date of Birth')
    ref = fields.Char(string='Reference', default="AA-")
    age = fields.Integer(string="Age", compute='_compute_age', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True)
    active = fields.Boolean(string="Active", default=True)

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
                if today.month < rec.date_of_birth.month:
                    rec.age -= 1
                elif today.month == rec.date_of_birth.month and today.day < rec.date_of_birth.day:
                    rec.age -= 1
            else:
                rec.age = 0
