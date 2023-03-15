import boto3
import logging
import uuid
from botocore.exceptions import ClientError

from src.updator.producer.constants import MESSAGE_GROUP_GENERAL_MUTATION
from src.updator.proto_py.mutation_pb2 import MutationRequests


class MutationProducer:
    """It encapsulates the sending of graph mutations to an AWS SQS queue.
    """

    def __init__(self, queue_name: str, region_name: str) -> None:
        sqs = boto3.resource("sqs", region_name=region_name)
        self.queue = sqs.find_queue_by_name(QueueName=queue_name)

    def Produce(self, mutations: MutationRequests) -> bool:
        """Sends a batch of mutations in a single message to an SQS queue.

        Args:
            mutations (MutationRequests): The batch of mutations to send to the
                queue.

        Raises:
            error: ClientError

        Returns:
            bool: It returns True only when the mutations are successfully
                sent to the queue.
        """
        try:
            self.queue.send_message(
                MessageBody=mutations.SerializeToString(),
                MessageGroupId=MESSAGE_GROUP_GENERAL_MUTATION,
                MessageDeduplicationId=uuid.uuid4())
            return True
        except ClientError as error:
            logging.exception(
                f"ProduceMutations failed to send messages: {self.queue}")
            raise error
