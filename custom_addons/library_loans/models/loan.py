from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Registro de Prestámos'
    
    
    # Relacion con modulo de creacion de libros
    book_id = fields.Many2one(
        
        comodel_name='library.book',
        string='Libro',
        required=True,
        domain=[('state','=','disponible')]
        )
    
    partner_id= fields.Many2one('res.partner', string='Socio', required=True)
    date_start = fields.Date(string='Fecha Inicio', default=fields.Date.today)
    return_date = fields.Date(string='Fecha Devolución')

    state = fields.Selection([
        ('draft', 'Borrador'),
        ('ongoing', 'En curso'),
        ('returned', 'Devuelto')
    ], string='Estado del prestamo', default='draft')
    
    def action_confirm_loan(self):
        for record in self:
            if record.book_id.state != 'disponible':
                raise ValidationError("El libro no está disponible para préstamo.")
            
            # Cambiamos el estado en el módulo de tu compañero
            record.book_id.state = 'prestado'
            record.state = 'ongoing'

    def action_return_book(self):
        for record in self:
            # Al devolverlo, lo ponemos disponible otra vez
            record.book_id.state = 'disponible'
            record.state = 'returned'
            record.date_return = fields.Date.today()