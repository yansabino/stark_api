from flask import jsonify
from usecases.create_invoice import CreateInvoiceUseCase

class InvoiceController:
    def __init__(self):
        self.create_invoice_use_case = CreateInvoiceUseCase()

    def create_invoice(self):
        try:
            invoice_data = self.create_invoice_use_case.execute()
            return {"message": "success"}, 201
        except ValueError as ve:
            return jsonify({"error": str(ve)}), 400
        except Exception as e:
            return jsonify({"error": str(e), "message": "Failed to create invoice."}), 500
