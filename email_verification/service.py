"""Main module."""
from client import verify_email
from database import result_database


def perform_verification(email: str) -> None:
    """Verify an email."""
    result_of_verify = verify_email(email)
    result_database.create_result(result_of_verify['email'], result_of_verify['verification_result'])
    print(f'Verification result for {email}: {result_of_verify["verification_result"]}')


def show_all_results() -> None:
    """Show all results in the database."""
    results = result_database.get_results()
    print('All results in the database:')
    for result in results:
        print(result)


if __name__ == '__main__':
    email_to_verify = input('Enter the email to verify: ')
    perform_verification(email_to_verify)
    show_all_results()
