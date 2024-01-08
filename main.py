"""Main module."""
from email_verification.client import EmailVerificationClient
from email_verification.database import ResultDatabase
from email_verification.service import EmailVerificationService


def main():
    # Replace 'your_api_key' with your actual Hunter API key
    api_key = '96d95ec2ea53efab6eaa859ebfa0d0a25f028a24'

    # Initialize the EmailVerificationClient and EmailVerificationService
    result_database = ResultDatabase()
    service = EmailVerificationService(api_key, result_database)

    # Example email for verification
    email_to_verify = 'invalid_email'
    result_verification = service.perform_verification(email_to_verify)



if __name__ == '__main__':
    main()
