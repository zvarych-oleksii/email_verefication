# main.py
from email_verification.service import EmailVerificationService
from email_verification.database import ResultDatabase


def main():
    api_key = input("Enter your Hunter.io API key: ")

    service = EmailVerificationService(api_key, ResultDatabase())

    email_to_verify = input("Enter the email for verification: ")

    service.perform_verification(email_to_verify)
    service.show_all_results()


if __name__ == "__main__":
    main()
