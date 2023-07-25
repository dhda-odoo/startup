from odoo import fields,models,api

class startup_fundraising(models.Model):
    _inherit=["startup.fundraising",'mail.activity']
    # _name="startup.fundraising"



    @api.model
    def create(self,vals):
        company_name = vals.get('company_name')
        self.env['project.project'].sudo().create({

            
            'name':company_name

        })
        return super().create(vals)
    
    
    def action_close_dialog(self):
        
        self.env['project.task'].create({
            'project_id':1,
            'name':"odooo",
            'stage_id':1
        })
        return super().action_close_dialog()

