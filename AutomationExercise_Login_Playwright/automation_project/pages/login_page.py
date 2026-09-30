"""
Page Object for AutomationExercise (https://www.automationexercise.com/).

Selectors are based on the site's own data-qa attributes, which the site's
developers added specifically to support automation practice (this is a
well-documented, stable public test site used across many QA courses).
"""

from playwright.sync_api import Page, expect

BASE_URL = "https://www.automationexercise.com"


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        # Nav
        self.signup_login_link = page.get_by_text("Signup / Login")

        # Login form (right-hand panel on the /login page)
        self.login_email_input = page.locator('input[data-qa="login-email"]')
        self.login_password_input = page.locator('input[data-qa="login-password"]')
        self.login_button = page.locator('button[data-qa="login-button"]')

        # Post-login indicator in the nav bar
        self.logged_in_indicator = page.get_by_text("Logged in as", exact=False)

        # Error message shown on invalid credentials
        self.login_error_message = page.locator("p", has_text="Your email or password is incorrect!")

    def open(self):
        """Navigate directly to the home page, then click through to Login —
        mirrors how a real user would arrive at the login form."""
        self.page.goto(BASE_URL)
        self.signup_login_link.click()
        expect(self.page).to_have_url(f"{BASE_URL}/login")

    def login(self, email: str, password: str):
        self.login_email_input.fill(email)
        self.login_password_input.fill(password)
        self.login_button.click()

    def assert_logged_in(self):
        expect(self.logged_in_indicator).to_be_visible(timeout=10000)

    def assert_login_failed(self):
        expect(self.login_error_message).to_be_visible(timeout=10000)
