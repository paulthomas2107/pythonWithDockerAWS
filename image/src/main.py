import numpy as np


def handler(event, container):
    arr = np.random.randint(0, 10, (3, 3))
    response = {
        "statusCode": 200,
        "body": {"message": "Hello from Paul !", "array": arr.tolist()}
    }

    return response