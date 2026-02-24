from odoo import models, fields

class LibraryBook(models.Model):
    _name = "library.book"
    _description = "Libro de Biblioteca"

    code = fields.Char(string="Código", required=True, copy=False)
    name = fields.Char(string="Título", required=True)
    description = fields.Text(string="Descripción")
    author_id = fields.Many2one(string="Autor", comodel_name="res.partner")
    active = fields.Boolean(string="Activo", default= True)
    isbn = fields.Char(string="ISBN")
    state = fields.Selection(string="Estado", selection=[("disponible", "Disponible"), ("prestado", "Prestado"), ("perdido", "Perdido")], default="disponible")