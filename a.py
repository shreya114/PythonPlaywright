import re
from playwright.sync_api import sync_playwright 

# def test_has_title(page: Page):
#     page.goto("https://playwright.dev/")

#     expect(page).to_have_title(re.compile("Playwright"))

# def test_get_started_link(page: Page):
#     page.goto("https://playwright.dev/")


#     page.get_by_role("link", name="Get started").click()

#     expect(page.get_by_role("heading", name="Installation")).to_be_visible()


with sync_playwright() as p:
    broswer = p.chromium.launch(headless=False)
    context = broswer.new_context()
    page = context.new_page()
    page.goto("https://amazon.in")

    page.wait_for_timeout(3000)
    page.close()
    context.close()
    broswer.close()