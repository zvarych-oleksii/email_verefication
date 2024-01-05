"""Verify email using hunter."""
from typing import Dict, Union

import requests

HUNTER_API_KEY = '96d95ec2ea53efab6eaa859ebfa0d0a25f028a24'


def verify_email(email: str) -> Dict[str, Union[str, bool]]:
    """Verify email using hunter."""
    url = f'https://api.hunter.io/v2/email-verifier?email={email}&api_key={HUNTER_API_KEY}'
    response = requests.get(url)
    response_data = response.json()

    if response.status_code == 200:
        return {'email': email, 'verification_result': response_data['data']['result']}
    return {'email': email, 'verification_result': f'Error: {response_data['errors'][0]['details']}'}
