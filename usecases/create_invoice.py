from services.invoice_service import InvoiceService
import random

class CreateInvoiceUseCase:
    def __init__(self):
        self.invoice_service = InvoiceService()

    def execute(self):
        try:
            for _ in range(random.randint(8, 12)):
                name = f"Customer {_}"
                tax_id = "36749369847"
                invoice = self.invoice_service.create_invoice(name, tax_id)
                return invoice
        except Exception as e:
            raise ValueError("Error while creating invoice: " + str(e))
