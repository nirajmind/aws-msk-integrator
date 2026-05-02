from aws_msk_iam_sasl_signer.MSKAuthTokenProvider import generate_auth_token

token = generate_auth_token('ap-south-1')
print("IAM token generated:", token)
