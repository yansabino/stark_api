```markdown
# Invoice App

This Flask application integrates with Stark Bank's API to create invoices and handle webhook callbacks. The application is designed to create a random number of invoices (between 8 to 12) every 3 hours for 24 hours. Upon receiving a webhook callback for an invoice credit, it processes the payment and initiates a transfer to a specified bank account.

## Deployed Application

You can access the deployed application at: [Invoice App](https://coherent-broker-439504-h3.uc.r.appspot.com)

## Features

- **Create Invoices**: Issues a specified number of invoices every 3 hours.
- **Webhook Integration**: Listens for webhook callbacks from Stark Bank for invoice credits.
- **Transfer Processing**: Sends the received amount (minus fees) to a specified bank account upon receiving payment confirmation.

## Project Structure

The application follows a clean architecture approach with the following layers:

- **Controllers**: Handle HTTP requests and responses.
- **Use Cases**: Contain the business logic of the application.
- **Services**: Interact with external APIs (like Stark Bank).

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

```

## Requirements

- Python 3.7 or higher
- Flask
- APScheduler
- Stark Bank SDK
- Gunicorn

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
   cd YOUR_REPO
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables (if applicable).

## Running the Application Locally

To run the application locally, execute:

```bash
python app.py
```

The app will run on `http://127.0.0.1:5000`.

## API Endpoints

### Create Invoice

- **Endpoint**: `POST /invoices/`
- **Description**: Creates a new invoice.

### Webhook for Invoice Credit

- **Endpoint**: `POST /webhook/invoice`
- **Description**: Receives a webhook callback for invoice credit.

## Testing

To run the unit tests, execute:

```bash
pytest tests
```

Ensure all dependencies are installed and the application is configured properly before running tests.

## Deployment

This application is deployed on Google App Engine. To redeploy, use the following command:

```bash
gcloud app deploy
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Notes

- Make sure to replace `YOUR_USERNAME` and `YOUR_REPO` with your actual GitHub username and repository name if you include the clone command.
- Update the README further based on any specific configurations or additional features you might have implemented.

Feel free to adjust any sections or add additional information as needed!