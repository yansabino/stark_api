from flask import Flask, jsonify
from config import Config
from controllers.invoice_controller import InvoiceController
from controllers.webhook_controller import WebhookController

app = Flask(__name__)
app.config.from_object(Config)

# Initialize controllers
invoice_controller = InvoiceController()
webhook_controller = WebhookController()

# Register routes
@app.route('/invoices/', methods=['POST'])
def create_invoice():
    return invoice_controller.create_invoice()

@app.route('/webhook/invoice', methods=['POST'])
def invoice_webhook():
    return webhook_controller.invoice_webhook()

# Global error handler
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle all exceptions globally."""
    response = {
        "error": str(e),
        "message": "An unexpected error occurred."
    }
    if hasattr(e, 'code'):
        return jsonify(response), e.code
    return jsonify(response), 500

if __name__ == '__main__':
    app.run(debug=True)
