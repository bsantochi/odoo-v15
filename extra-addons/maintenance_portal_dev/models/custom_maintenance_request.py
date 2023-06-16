# -*- coding: utf-8 -*-

from odoo import api, fields, models


class CustomMaintenanceRequest(models.Model):
    _inherit = "maintenance.request"

    # a
    partner_id = fields.Many2one('res.partner', string="Usuario Portal Solicitante",
                                 readonly=True)
    # b
    equipment_id = fields.Many2one(
        string="Equipamiento", comodel_name="maintenance.equipment"
    )

    equipment_department_id = fields.Many2one(
        string="EquiDep", related="equipment_id"
    )

    def search_deparment(self):
        department = self.env["hr.department"]
        all_department = department.search([])
        print("search()", all_department, all_department.name)

    department_id = fields.Many2one(string="Departamento", related="equipment_id")

    # @api.onchange(equipment_id)
    # def onchange_equipment_id(self):
    #     self.department_id = self.equipment_id.department_id

    # c
    acting_user_ids = fields.Many2many('res.users', string="Ejecutantes")
                                       #, domain={[('maintenance_team_id', '=', 'True')]})

    # d
    user_id = fields.Many2one('res.users', string="Usuario informante")

    # e
    priority = fields.Selection([('0', 'Very Low'), ('1', 'Low'), ('2', 'Normal'), ('3', 'High')], string='Priority')

