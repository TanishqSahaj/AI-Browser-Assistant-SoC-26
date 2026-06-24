import asyncio
import json
from pathlib import Path


async def load_users(file_path: str) -> list[dict]:
    """Asynchronously load user data from a JSON file."""

    def read_file():
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    return await asyncio.to_thread(read_file)


async def print_users(users: list[dict]) -> None:
    """Print user information in a readable format."""
    for i, user in enumerate(users, start=1):
        print(f"\nUser #{i}")
        print("-" * 40)
        print(f"Name    : {user.get('name', 'N/A')}")
        print(f"Email   : {user.get('email', 'N/A')}")
        print(f"Phone   : {user.get('phone', 'N/A')}")
        print(f"Address : {user.get('address', 'N/A')}")


async def main():
    file_path = Path(__file__).parent / "user.json"

    if not Path(file_path).exists():
        print(f"Error: {file_path} not found.")
        return

    users = await load_users(file_path)
    await print_users(users)


if __name__ == "__main__":
    asyncio.run(main())