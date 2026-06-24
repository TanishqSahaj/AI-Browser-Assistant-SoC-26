import json
import traceback
from pathlib import Path

from playwright.async_api import async_playwright, TimeoutError


json_path = Path(__file__).parent / "user_data.json"


async def form_filler():
    try:
        # Load user data
        with open(json_path, "r", encoding="utf-8") as f:
            user = json.load(f)

        async with async_playwright() as p:

            browser = await p.chromium.launch(
                headless=False
            )

            page = await browser.new_page()

            # Open DemoQA form
            await page.goto(
                "https://demoqa.com/automation-practice-form",
                timeout=30000
            )

            await page.wait_for_load_state("networkidle")

            # Remove ad iframes that sometimes block clicks
            await page.evaluate("""
                document.querySelectorAll('iframe').forEach(
                    iframe => iframe.remove()
                );
            """)

            # First Name
            await page.fill(
                "#firstName",
                user["first_name"]
            )

            # Last Name
            await page.fill(
                "#lastName",
                user["last_name"]
            )

            # Email
            await page.fill(
                "#userEmail",
                user["email"]
            )

            # Gender
            gender = user["gender"].lower()

            if gender == "male":
                await page.locator(
                    "label[for='gender-radio-1']"
                ).click(force=True)

            elif gender == "female":
                await page.locator(
                    "label[for='gender-radio-2']"
                ).click(force=True)

            else:
                await page.locator(
                    "label[for='gender-radio-3']"
                ).click(force=True)

            # Mobile Number
            await page.fill(
                "#userNumber",
                user["mobile"]
            )

            # Subject
            if user.get("subjects"):
                await page.fill(
                    "#subjectsInput",
                    user["subjects"][0]
                )
                await page.keyboard.press("Enter")

            # Hobby
            await page.locator(
                "label[for='hobbies-checkbox-1']"
            ).click(force=True)

            # Address
            await page.fill(
                "#currentAddress",
                user["address"]
            )

            print("Form filled successfully")

            # Screenshot before submission
            await page.screenshot(
                path="form_filled.png",
                full_page=True
            )

            print("Screenshot saved as form_filled.png")

            await browser.close()

    except FileNotFoundError:
        print(f"user_data.json not found at:\n{json_path}")

    except TimeoutError:
        print("Page load timeout")

    except KeyError as e:
        print(f"Missing key in JSON: {e}")

    except Exception:
        print("Unexpected error:")
        traceback.print_exc()