from sisyphus.core import AIAgent

class NarrowTaskAgent(AIAgent):
    """
    Base class for all Narrow Task AI Agents in the Sisyphus package.
    Extends the AIAgent class with additional attributes and methods specific to narrow tasks.
    """

    def __init__(self, name, task, task_specific_parameter):
        """
        Initializes a new Narrow Task AI Agent.

        :param name: A unique name for the agent.
        :param task: The specific narrow task the agent is designed to perform.
        :param task_specific_parameter: A parameter that's specific to the narrow task agents.
        """
        super().__init__(name, task)
        self.task_specific_parameter = task_specific_parameter

    def prepare_data(self, data):
        """
        Prepare data specific to the narrow task.

        :param data: The raw data.
        :return: The prepared data ready for training or inference.
        """
        # Implement data preparation logic specific to the narrow task
        # This might include preprocessing steps like normalization, tokenization, etc.
        return data  # Placeholder return

    def evaluate_performance(self, predictions, ground_truth):
        """
        Evaluate the performance of the agent on a task.

        :param predictions: The model's predictions.
        :param ground_truth: The true values.
        :return: The performance metric.
        """
        # Implement performance evaluation logic
        # This might include calculating metrics like accuracy, F1 score, etc.
        raise NotImplementedError("This method needs to be implemented by subclasses.")