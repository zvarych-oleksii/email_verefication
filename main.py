# main.py
from email_verification.service import EmailVerificationService
from email_verification.database import ResultDatabase


def main():
    # Enter your Hunter.io API key
    api_key = input("Enter your Hunter.io API key: ")

    # Initialize the EmailVerificationService
    service = EmailVerificationService(api_key, ResultDatabase())

    # Enter the email for verification
    email_to_verify = input("Enter the email for verification: ")

    # Perform verification and show results
    service.perform_verification(email_to_verify)
    service.show_all_results()


if __name__ == "__main__":
    main()
