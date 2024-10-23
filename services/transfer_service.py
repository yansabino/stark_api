import starkbank

class TransferService:
    def __init__(self):
        self.user = starkbank.Project(
            environment="sandbox",  # "production" for live
            id="6017754540802048",
            private_key="-----BEGIN EC PARAMETERS-----BgUrgQQACg==-----END EC PARAMETERS----------BEGIN EC PRIVATE KEY-----MHQCAQEEIFCLYpln978L1Cx0ehA8pxs64fXXpuTjC6ttmVnKOgejoAcGBSuBBAAKoUQDQgAE2tctMCoVjShEJCsbpp2UX5ULha355f6ZcwMQ2/Y2LGFuJplcQMnSiAiW0nmsqJR9mXTscGfxn06mG/4EBcStKw==-----END EC PRIVATE KEY-----"
        )

    def process_webhook(self, data):
        try:
            amount_received = data['amount']
            fee = data['fee']
            net_amount = amount_received - fee
            
            transfer_response = starkbank.Transfer.create([
                {
                    "amount": net_amount,
                    "bank_code": "20018183",
                    "branch": "0001",
                    "account": "6341320293482496",
                    "name": "Stark Bank S.A.",
                    "tax_id": "20.018.183/0001-80",
                    "account_type": "payment"
                }
            ], self.user)
            return {
                "status": "success",
                "transfer_id": transfer_response.id
            }
        except Exception as e:
            raise RuntimeError("Stark Bank API error: " + str(e))
        except KeyError as e:
            raise ValueError(f"Missing required key in data: {str(e)}")
