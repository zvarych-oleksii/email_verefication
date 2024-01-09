"""Example script to test."""
from email_verification.database import ResultDatabase
from email_verification.service import EmailVerificationService

# Assuming you have an instance of ResultDatabase
# You may need to replace ResultDatabase() with your actual database instantiation logic
db = ResultDatabase()

# Replace 'your_api_key_here' with your actual Hunter.io API key
api_key = 'your_api_key_here'

# Instantiate the EmailVerificationService
verification_service = EmailVerificationService(api_key, db)

# Example: Counting emails for a domain
domain_to_count = 'stripe.com'
count_result = verification_service.count_emails(domain_to_count)
print(f"Count result for {domain_to_count}: {count_result}")

# Example: Verify an email
email_to_verify = 'opatrick@stripe.com'
verification_result = verification_service.email_verification(email_to_verify)
print(f"Verification result for {email_to_verify}: {verification_result}")

email_to_verify = 'patrick@stripe.com'
verification_result = verification_service.email_verification(email_to_verify)
print(f"Verification result for {email_to_verify}: {verification_result}")

# Example: Get all verification results
all_results = verification_service.get_all_results()
print("All verification results:")
for result in all_results:
    print(result)

# Example: Get a specific verification result for an email
email_to_get_result_for = 'patrick@stripe.com'
specific_result = verification_service.get_result(email_to_get_result_for)
print(f"Verification result for {email_to_get_result_for}: {specific_result}")

# Example: Delete a verification result for an email
email_to_delete_result_for = 'patrick@stripe.com'
delete_result = verification_service.delete_result(email_to_delete_result_for)
print(f"Result for deletion of {email_to_delete_result_for}: {delete_result}")
