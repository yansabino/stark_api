import random
from datetime import datetime, timedelta
from dotenv import load_dotenv
from os import environ
import starkbank
load_dotenv('.env')
class InvoiceService:
    def __init__(self):
        self.user = starkbank.Project(
            environment=environ["ENVIRONMENT"],  # "production" for live
            id=environ["PROJECT_ID"],
            private_key=environ["PRIVATE_KEY"]
        )

    def create_invoice(self, name, tax_id):
        amount = random.randint(1000, 10000)  # Random amount
        try:
            invoice = starkbank.invoice.create([
                {
                    "amount": amount,
                    "name": name,
                    "tax_id": tax_id
                }
            ], self.user)
            print(invoice)
            return invoice
        except Exception as e:
            raise RuntimeError("Stark Bank API error: " + str(e))
