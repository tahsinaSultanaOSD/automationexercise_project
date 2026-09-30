"""
Scenario under test (per assessment instructions):
1. Launch the website
2. Navigate to the Login page
3. Enter the registered email address and password
4. Submit the login form
5. Verify that the login was successful

Run with:
    pytest tests/test_login.py --headed     # to watch it run
    pytest tests/test_login.py              # headless (CI-friendly)
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage


def test_successful_login_with_valid_credentials(page, credentials):
    login_page = LoginPage(page)

    # 1 & 2: Launch the site and navigate to the Login page
    login_page.open()

    # 3 & 4: Enter credentials and submit
    login_page.login(credentials["email"], credentials["password"])

    # 5: Verify login was successful
    login_page.assert_logged_in()


def test_login_fails_with_incorrect_password(page, credentials):
    """Bonus negative case — not required by the brief, but a one-line addition
    that meaningfully strengthens the suite: proves the login form actually
    validates credentials rather than always succeeding."""
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(credentials["email"], "definitely-the-wrong-password")
    login_page.assert_login_failed()
