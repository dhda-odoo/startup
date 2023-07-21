from odoo import fields,models,Command
import logging


_logger=logging.getLogger(__name__)

class startup_account(models.Model):
    _inherit="startup.fundraising"
    _name="startup.fundraising"
    
    def action_set_sold(self):
        _logger.info("sold method overriden")
        self.env['account.move'].create(
            {
                'move_type':'out_invoice',
                'partner_id':self.buyer_id.id,
                'invoice_date':fields.Date.context_today(self),
                'invoice_line_ids':[
                    Command.create({
                        'name':self.company_name,
                        'price_unit':self.selling_price,
                        'quantity':1,
                        'tax_ids':[1]
                    }),
                    
                    Command.create({
                        'name':self.company_name,
                        'price_unit':100,
                        'quantity':1,
                        'tax_ids':[1]
                    })
                ]
        
        }
        )
        return super().action_set_sold()
    
    