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
    department_id = fields.Many2one(string="Departamento", related="equipment_id.department_id")

    # c

    acting_user_ids = fields.Many2many('res.users', string="Ejecutantes",
                                       domain="[('id', 'in', team_member_ids)]")

    team_member_ids = fields.Many2many('res.users', string="Miembros del Equipo",
                                       compute="_compute_team_member_ids")

    @api.depends('maintenance_team_id')
    def _compute_team_member_ids(self):
        for record in self:
            if record.maintenance_team_id:
                record.team_member_ids = record.maintenance_team_id.member_ids.ids
            else:
                record.team_member_ids = False

    # d
    # user_id = fields.Many2one('res.users', string="Usuario informante")
    #
    # # e
    priority = fields.Selection([('0', 'Very Low'), ('1', 'Low'), ('2', 'Normal'), ('3', 'High')],
                                string='Priority')

    # f
    maintenance_priority = fields.Selection([
        ('1', '1- Máquina parada / producción detenida'),
        ('2', '2- Máquina funcionando / necesidad de reparación'),
        ('3', '3- No afecta a la producción'),
        ('4', '4- Otro / detallar en notas')
    ], string="Prioridad")
