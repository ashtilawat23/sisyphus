class AIAgent:
    """
    Base class for all AI agents in the Sisyphus package.
    This class provides basic attributes and methods that all agents share.
    """
    def __init__(self, name, task):
        """
        Initializes a new AI agent.

        :param name: A unique name for the agent.
        :param task: The specific task the agent is designed to perform.
        """
        self.name = name
        self.task = task

    def train(self, data):
        """
        Train the AI agent on a dataset.

        :param data: The training data.
        """
        raise NotImplementedError("This method needs to be implemented by subclasses.")

    def perform_task(self, input_data):
        """
        Perform the agent's task on the given input data.

        :param input_data: The input data for the task.
        :return: The result of the task.
        """
        raise NotImplementedError("This method needs to be implemented by subclasses.")

def check_output(output):
    """
    Utility function to check the output of an AI agent's task.

    :param output: The output to check.
    :return: True if the output meets the criteria, False otherwise.
    """
    # Implement your output checking logic here
    # For example, check if the output is within a certain range, non-empty, etc.
    if output:  # Placeholder condition
        return True
    else:
        return False
