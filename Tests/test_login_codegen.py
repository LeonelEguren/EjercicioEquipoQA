import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("file:///C:/Users/Personal/Desktop/ejercicioQA-login/ejercicioQA-login.html")
    page.get_by_role("button", name="Show password Hide password").click()
    page.get_by_role("button", name="Show password Hide password").click()
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("pas")
    page.get_by_role("button", name="Show password Hide password").click()
    page.get_by_role("button", name="Show password Hide password").click()
    page.get_by_role("button", name="Show password Hide password").click()
    page.get_by_role("button", name="Show password Hide password").click()
    page.get_by_role("link", name="Forgot password?").click()
    page.get_by_role("link", name="Sign up").click()
    page.get_by_role("button", name="Continue with Google").click()
    page.get_by_role("button", name="Continue with Google").click()
    page.get_by_role("textbox", name="Email address").click()
    page.get_by_role("heading", name="Welcome").click()
    page.get_by_text("Log in to Mercap to continue").click()
    page.get_by_text("Email address", exact=True).click()
