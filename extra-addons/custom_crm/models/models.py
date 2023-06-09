# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Visit(models.Model):
    _name = "custom_crm.visit"
    _description = "Visit"

    name = fields.Char(string="Descripción")
    #    customer = fields.Char(string='Cliente') antes del campo relacionado
    customer = fields.Many2one(string="Cliente", comodel_name="res.partner")
    date = fields.Datetime(string="Fecha")
    type = fields.Selection(
        [("P", "Presencial"), ("W", "WhatsApp"), ("T", "Telefónico")],
        string="Tipo",
        required=True,
    )
    done = fields.Boolean(strng="Realizada", readonly=True)
    image = fields.Binary(string="Imagen")

    def toggle_state(self):
        self.done = not self.done
