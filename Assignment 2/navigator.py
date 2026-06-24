import json
from playwright.async_api import async_playwright, TimeoutError


async def navigator():
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)

            page = await browser.new_page()

            await page.goto(
                "https://news.ycombinator.com",
                timeout=15000
            )

            await page.wait_for_selector(".titleline a")

            titles = await page.locator(
                ".titleline a"
            ).all_text_contents()

            top_five = titles[:5]

            with open("articles.json", "w") as f:
                json.dump(top_five, f, indent=4)

            print("Saved top 5 articles")

            await browser.close()

    except TimeoutError:
        print("Timeout while loading website")

    except Exception as e:
        print(f"Element not found / Error: {e}")