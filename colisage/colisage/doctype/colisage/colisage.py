# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Colisage(Document):
    def validate(self):
        self.calculate_total_amount()

    def calculate_total_amount(self):
        total_amount = sum(item.price * item.quantity for item in self.items)
        self.total_amount = total_amount

    def on_submit(self):
        # Logique lors de la soumission, si nécessaire
        pass

    def on_cancel(self):
        # Logique lors de l'annulation, si nécessaire
        pass
