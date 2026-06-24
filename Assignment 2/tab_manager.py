import asyncio
from playwright.async_api import async_playwright, TimeoutError


async def open_tab(context, url):

    page = await context.new_page()

    await page.goto(url)

    title = await page.title()

    return page, title


async def tab_manager():

    urls = [
        "https://google.com",
        "https://github.com",
        "https://bbc.com",
        "https://wikipedia.org",
        "https://news.ycombinator.com"
    ]

    try:

        async with async_playwright() as p:

            browser = await p.chromium.launch(
                headless=False
            )

            context = await browser.new_context()

            results = await asyncio.gather(
                *[open_tab(context, url) for url in urls]
            )

            pages = []
            titles = []

            for page, title in results:
                pages.append(page)
                titles.append(title)

            print("\nTab Titles\n")

            for idx, title in enumerate(titles, 1):
                print(f"{idx}. {title}")

            for page in pages[1:]:
                await page.close()

            print("\nClosed all tabs except first")

            await browser.close()

    except TimeoutError:
        print("Tab load timeout")

    except Exception as e:
        print(f"Error opening tabs: {e}")