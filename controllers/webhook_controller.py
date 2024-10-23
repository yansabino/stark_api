from flask import request, jsonify
from usecases.handle_webhook import HandleWebhookUseCase

class WebhookController:
    def __init__(self):
        self.handle_webhook_use_case = HandleWebhookUseCase()

    def invoice_webhook(self):
        data = request.json
        if not data:
            return jsonify({"error": "Invalid data format."}), 400

        try:
            # Extract necessary fields from webhook payload
            event_data = data.get('event', {}).get('log', {}).get('invoice', {})
            if not event_data:
                return jsonify({"error": "Missing invoice data in webhook payload."}), 400
            
            # Pass the extracted data to the use case
            response = self.handle_webhook_use_case.execute(event_data)
            return jsonify(response), 200
        except KeyError as ke:
            return jsonify({"error": f"Missing key: {str(ke)}"}), 400
        except Exception as e:
            return jsonify({"error": str(e), "message": "Failed to process webhook."}), 500
