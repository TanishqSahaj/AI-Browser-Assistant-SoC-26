import asyncio
from parse_intent import parse_intent

commands = [
    "Apply to this job",
    "Close all tabs",
    "Email this summary to my boss",
    "Go to linkedin.com",
    "Open github and search for browser-use",
    "Fill the signup form on example.com",
    "Summarize the current webpage",
    "Click the login button",
    "Book a hotel in Mumbai",
    "Download the latest resume from my drive"
]


async def main():
    for command in commands:
        print("\n" + "=" * 50)
        print("COMMAND:", command)

        try:
            result = await parse_intent(command)
            print(result)

        except Exception as e:
            print("FAILED:", e)


asyncio.run(main())