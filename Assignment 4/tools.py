from langchain.tools import tool
from browser import page
from memory import remember
import json
from pathlib import Path

@tool
def get_user_profile() -> dict:
    """Returns user information."""

    profile_path = Path(__file__).parent / "user_profile.json"

    with open(profile_path, "r") as f:
        profile = json.load(f)

    remember(
        "get_user_profile",
        "Fetched profile"
    )

    return profile

@tool
def navigate_to(url: str):
    """Navigate to a website."""

    page.goto(url)

    result = f"Opened {url}"

    remember(
        "navigate_to",
        result
    )

    return result


@tool
def click_element(selector: str):
    """Click an element using CSS selector."""

    page.locator(selector).click()

    result = f"Clicked {selector}"

    remember(
        "click_element",
        result
    )

    return result


@tool
def type_text(selector: str, text: str):
    """Type text into an element."""

    page.locator(selector).fill(text)

    result = f"Typed '{text}'"

    remember(
        "type_text",
        result
    )

    return result

TOOLS = [
    navigate_to,
    click_element,
    type_text,
    get_user_profile
]