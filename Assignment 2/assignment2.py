import asyncio

from navigator import navigator
from form_filler import form_filler
from tab_manager import tab_manager


async def main():

    print("Running Navigator")
    await navigator()

    print("\nRunning Form Filler")
    await form_filler()

    print("\nRunning Tab Manager")
    await tab_manager()


if __name__ == "__main__":
    asyncio.run(main())