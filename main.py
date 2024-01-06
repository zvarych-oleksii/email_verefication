"""Main module."""
from email_verification.client import EmailVerificationClient
from email_verification.database import ResultDatabase
from email_verification.service import EmailVerificationService

def main():
    # Replace 'your_api_key' with your actual Hunter API key
    api_key = 'your_api_key'

    # Initialize the EmailVerificationClient and EmailVerificationService
    client = EmailVerificationClient(api_key)
    result_database = ResultDatabase()
    service = EmailVerificationService(api_key, result_database)

    # Example email for verification
    email_to_verify = 'example@example.com'

    # Perform email verification
    email, verification_result = service.perform_verification(email_to_verify)

    # Display verification result
    print(f"Verification result for {email}: {verification_result}")

    # Get all verification results
    all_results = service.get_all_results()

    # Display all verification results
    print("All verification results:")
    for result in all_results:
        print(result)


if __name__ == '__main__':
    main()
