# Stark Bank Invoice & Webhook API

This Flask API integrates with the Stark Bank API to create invoices and handle webhook callbacks for payments. When an invoice is paid, the app receives a webhook, processes the payment, and transfers the net amount (after fees) to a specified account.

## Features

- **Invoice Creation**: Issues random invoices at regular intervals.
- **Webhook Callback**: Receives webhook notifications when invoices are paid.
- **Transfer**: Processes the invoice payment and transfers the received amount (minus fees) to a specified bank account.

## Project Structure

The application follows a clean architecture approach with the following layers:

- **Controllers**: Handle HTTP requests and responses.
- **Use Cases**: Contain the business logic of the application.
- **Services**: Interact with external APIs (like Stark Bank).
- **Gateways**: Provide access to external services.

### Folder Structure

```plaintext
stark_bank_api/
│
├── app.py                   # Main application file
├── config.py                # Configuration settings
├── controllers/             # Controllers for handling requests
│   ├── __init__.py
│   ├── invoice_controller.py
│   └── webhook_controller.py
├── usecases/                # Use cases for business logic
│   ├── __init__.py
│   ├── create_invoice.py
│   └── handle_webhook.py
├── services/                # Services for interacting with APIs
│   ├── __init__.py
│   ├── invoice_service.py
│   └── transfer_service.py
└── gateways/                # Gateways for external services
    ├── __init__.py
    └── starkbank_gateway.py
```

## Requirements

- Python 3.8 or higher
- Flask
- Stark Bank Python SDK

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-repository/stark_bank_api.git
   cd stark_bank_api
   ```

2. **Create a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables**:

   Create a `.env` file or export the following environment variables in your shell:

   ```bash
   export STARKBANK_PROJECT="your-stark-bank-project-id"
   export STARKBANK_ENVIRONMENT="sandbox"  # Use "production" for production
   export STARKBANK_API_KEY="your-stark-bank-api-key"
   ```

5. **Run the Flask app**:

   ```bash
   python app.py
   ```

## API Endpoints

### 1. Create Invoice

- **URL**: `/invoices/`
- **Method**: `POST`
- **Description**: This endpoint creates a random invoice using the Stark Bank API.

#### Response Example:

```json
{
  "id": "unique-invoice-id",
  "amount": 5000,
  "due": "2024-10-23T10:00:00Z"
}
```

### 2. Webhook for Invoice Payment

- **URL**: `/webhook/invoice`
- **Method**: `POST`
- **Description**: This endpoint handles webhook callbacks from Stark Bank. When an invoice is paid, it processes the payment and makes a transfer to the specified account.

#### Request Example (Webhook Payload):

```json
{
  "event": {
    "log": {
      "id": "unique-log-id",
      "created": "2024-10-23T10:00:00Z",
      "type": "credited",
      "invoice": {
        "id": "unique-invoice-id",
        "amount": 5000,
        "status": "paid",
        "fee": 50,
        "created": "2024-10-22T10:00:00Z",
        "due": "2024-10-23T10:00:00Z",
        "tax_id": "123.456.789-10",
        "recipient": {
          "name": "John Doe",
          "tax_id": "123.456.789-10"
        }
      }
    }
  }
}
```

#### Response Example:

```json
{
  "status": "success",
  "transfer_id": "unique-transfer-id"
}
```

## Error Handling

- **400 Bad Request**: For invalid or missing data in the request.
- **500 Internal Server Error**: For unexpected server errors or failed Stark Bank API calls.

### Global Error Handling Example:

```json
{
  "error": "Detailed error message",
  "message": "An unexpected error occurred."
}
```

## How the System Works

1. **Invoice Creation**: The `InvoiceController` handles requests for creating invoices. It calls the `CreateInvoiceUseCase`, which interacts with `InvoiceService` to generate invoices using the Stark Bank API.
2. **Webhook Handling**: When a webhook callback is received (indicating that an invoice has been paid), the `WebhookController` extracts the invoice data and passes it to the `HandleWebhookUseCase`. This use case then uses `TransferService` to process the payment and initiate a transfer to a predefined bank account.

## Running Tests

To run tests, you can use any Python testing framework such as `unittest` or `pytest`. Here is an example command to run tests with `pytest`:

```bash
pytest tests/
```

## Deployment

This application can be deployed on any platform that supports Python and Flask (e.g., Heroku, AWS, or Google Cloud). Ensure that the environment variables are set for the deployment environment.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.