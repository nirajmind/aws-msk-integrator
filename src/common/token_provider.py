from aws_msk_iam_sasl_signer.MSKAuthTokenProvider import generate_auth_token
import os

region = os.getenv("AWS_REGION", "ap-south-1")

class TokenProvider:
    def token(self):
        return generate_auth_token(region=region)
