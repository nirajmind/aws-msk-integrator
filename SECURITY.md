# Security Guidelines

## Never store AWS credentials in the repository

- Do not commit `.env` files
- Do not commit AWS Access Keys or Secret Keys
- Do not commit `~/.aws/credentials`

## Use secure authentication

- Prefer AWS SSO or IAM roles
- Use `aws configure` for local development
- Use environment variables only for non-secret config

## GitHub Safety

- Enable 2FA
- Rotate credentials regularly
- Use GitHub secret scanning alerts
