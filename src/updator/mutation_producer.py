import logging
from botocore.exceptions import ClientError
from typing import List

from src.updator.proto_py.mutation_pb2 import MutationRequest


def ProduceMutations(messages: List[MutationRequest], queue) -> bool:
    """Send a batch of mutation messages in a single request to an SQS queue.

    Args:
        messages (List[MutationRequest]): The mutation messages to send to the
            queue.
        queue: The SQS queue to receive the mutation messages.

    Raises:
        error: ClientError

    Returns:
        bool: It returns True only when all the messages are successfully sent.
    """
    try:
        entries = [
            {"MessageBody": msg.SerializeToString()}
            for msg in enumerate(messages)]

        response = queue.send_messages(Entries=entries)

        return not ("Failed" in response)
    except ClientError as error:
        logging.exception(f"ProduceMutations failed to send messages: {queue}")
        raise error
