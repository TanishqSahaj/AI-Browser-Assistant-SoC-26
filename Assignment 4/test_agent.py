from agent import TOOLS
from memory import get_history


print("\n---- TASK 1 ----")

result = TOOLS["navigate_to"].invoke(
    "https://www.google.com"
)

print(result)


print("\n---- TASK 2 ----")

result = TOOLS["type_text"].invoke(
    "textarea[name='q']|AI News"
)

print(result)


print("\n---- TASK 3 ----")

profile = TOOLS["get_user_profile"].invoke(
    ""
)

print(profile)


print("\n---- MEMORY ----")

print(
    get_history()
)