# AutomationExercise Login — Playwright + Python + pytest

Automates the login scenario for https://www.automationexercise.com/ using the
Page Object Model.

## ⚠️ Before you run this

Per the assessment instructions, **you must manually create a real account** on
automationexercise.com first (Signup / Login → New User Signup). This project
deliberately does not automate account creation — it only automates *logging
in* with credentials you already have.

## Project structure

```
automation_project/
├── pages/
│   └── login_page.py      # Page Object: locators + actions for the Login page
├── tests/
│   └── test_login.py      # The login scenario + one bonus negative case
├── conftest.py             # Reads credentials from .env
├── requirements.txt
├── pytest.ini
└── .env.example
```

## Setup

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
playwright install               # downloads the browser binaries

cp .env.example .env
# then edit .env and fill in the email/password of the account you created manually
```

## Run

```bash
pytest tests/test_login.py --headed    # watch it run in a real browser window
pytest tests/test_login.py             # headless
```

## What it does

1. Launches automationexercise.com
2. Clicks "Signup / Login" to reach the Login page
3. Fills in the email and password from your `.env` file
4. Submits the form
5. Asserts that "Logged in as [name]" appears in the nav bar, confirming success

A second test (`test_login_fails_with_incorrect_password`) is included as a
small bonus — it isn't required by the brief, but proves the suite can also
detect a *failed* login, not just assert blindly that login "worked."

## A note on how this was built

Selectors (`data-qa="login-email"`, `data-qa="login-password"`,
`data-qa="login-button"`) are based on the site's own documented/known
structure — this is a long-standing, stable public practice site and these
`data-qa` attributes were added by its maintainers specifically to support
automation. That said, **this code was written without being executed against
the live site** (this environment's network access doesn't reach
automationexercise.com), so treat it as a strong, ready-to-run starting point
rather than something guaranteed bug-free — run it yourself and adjust
selectors if the site's markup has since changed.
