from flask import Flask, jsonify
from controllers.invoice_controller import InvoiceController
from controllers.webhook_controller import WebhookController
from apscheduler.schedulers.background import BackgroundScheduler
import random

app = Flask(__name__)

# Initialize controllers
invoice_controller = InvoiceController()
webhook_controller = WebhookController()

# Function to create invoices
def scheduled_invoice_creation():
    for _ in range(random.randint(8, 12)):  # Create a random number of invoices between 8 and 12
        # Here you should implement the logic to create an invoice
        invoice_controller.create_invoice()
        print("Invoice created")  # Log the invoice creation

# Initialize and start the scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(scheduled_invoice_creation, 'interval', hours=3)  # Schedule every 3 hours
scheduler.start()

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

# Graceful shutdown
def start_scheduler():
    print("Scheduler started.")

@app.route('/shutdown', methods=['POST'])
def shutdown():
    scheduler.shutdown()
    return jsonify({"message": "Scheduler shut down."}), 200

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()  # Ensure the scheduler is shut down