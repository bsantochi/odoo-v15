# -*- coding: utf-8 -*-

from odoo import api, fields, models


class CustomMaintenanceRequest(models.Model):
    _inherit = "maintenance.request"

    partner_id = fields.Many2one(
        string="Usuario Portal Solicitante", comodel_name="res.partner", readonly=True
    )

    department_id = fields.Char(string="Departamento")
    """ equipment_id = fields.Many2one(
        string="Equipamiento", comodel_name="maintenance.equipment.category"
    ) """

    """ @api.onchange(equipment_id) """

    def onchange_equipment_id(self):
        self.department_id = self.equipment_id.department_id
