import os
import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def credentials():
    """
    Reads the manually-created AutomationExercise account credentials from
    environment variables (or a local .env file — see .env.example).

    IMPORTANT: per the assessment instructions, you must manually sign up for
    a real account on https://www.automationexercise.com/ FIRST, then put
    those credentials here. This project does not create the account for you.
    """
    email = os.getenv("AE_EMAIL")
    password = os.getenv("AE_PASSWORD")
    if not email or not password:
        pytest.fail(
            "Missing AE_EMAIL / AE_PASSWORD. Copy .env.example to .env and fill in "
            "the credentials of the account you manually created on "
            "automationexercise.com."
        )
    return {"email": email, "password": password}
