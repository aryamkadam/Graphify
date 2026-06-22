transfer_history = []


def save_transfer(
    target_ai
):

    transfer_history.append(
        target_ai
    )

    return transfer_history


def get_transfer_history():

    return transfer_history