from services.transfer_service import TransferService

class HandleWebhookUseCase:
    def __init__(self):
        self.transfer_service = TransferService()

    def execute(self, data):
        try:
            return self.transfer_service.process_webhook(data)
        except KeyError as e:
            raise ValueError(f"Missing required data in webhook: {str(e)}")
        except Exception as e:
            raise RuntimeError("Error while handling webhook: " + str(e))
