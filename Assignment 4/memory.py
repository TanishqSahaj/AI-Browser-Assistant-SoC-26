history = []


def remember(action, observation):
    history.append({
        "action": action,
        "observation": observation
    })

    print("MEMORY:", history)


def get_history():
    return history


def latest():
    if history:
        return history[-1]
    return None