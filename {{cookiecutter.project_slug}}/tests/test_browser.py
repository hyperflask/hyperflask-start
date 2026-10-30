from playwright.sync_api import Page, expect


def test_index_in_browser(page: Page):
    page.goto("/")
    expect(page.get_by_role("heading", level=1)).to_contain_text("Welcome")
