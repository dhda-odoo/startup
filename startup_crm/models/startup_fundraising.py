from odoo import fields,models,api

class startup_fundraising(models.Model):
    _inherit="startup.fundraising.offers"
    

    @api.model
    def create(self,vals):
        price = vals.get('price')
        partner=vals.get('partner_id')
        deadline= vals.get('deadline_date')
        self.env['crm.lead'].sudo().create({
            'stage_id':1,
            'name':"quotation for stake",
            'expected_revenue':price,
            'partner_id':partner,
            'date_deadline':deadline


        })
        return super().create(vals)    
