from agent import agent
from tools import TOOLS
from memory import get_history

tool_map = {
    tool.name: tool
    for tool in TOOLS
}


def run_agent(command: str):

    messages = [
        (
            "human",
            command
        )
    ]

    print("\nMEMORY:")
    print(get_history())

    response = agent.invoke(messages)

    while response.tool_calls:

        for tool_call in response.tool_calls:

            tool_name = tool_call["name"]

            tool_args = tool_call["args"]

            print("\nTOOL:")
            print(tool_name)

            print("ARGS:")
            print(tool_args)

            result = tool_map[
                tool_name
            ].invoke(tool_args)

            print("RESULT:")
            print(result)

            messages.append(response)

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call["id"],
                    "content": str(result)
                }
            )

        response = agent.invoke(messages)

    print("\nFINAL ANSWER:")
    print(response.content)