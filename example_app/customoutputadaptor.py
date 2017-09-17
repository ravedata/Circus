from chatterbot.output.output_adapter import OutputAdapter
from chatterbot.conversation import statement
## Call the weather package  here
class CustomOutputAdapter(OutputAdapter):
    """
    A generic class that can be overridden by a subclass to provide extended
    functionality, such as delivering a response to an API endpoint.
    """

    def process_response(self, statement, session_id=None):
        """
        Override this method in a subclass to implement customized functionality.

        :param statement: The statement that the chat bot has produced in response to some input.

        :param session_id: The unique id of the current chat session.

        :returns: The response statement.
        """
       # statement.text="Overridden";

        statement.text = "weather";
        if 'weather' not in statement.text:
            return statement

        else:
            statement.text="The weather today is beautiful"
            return statement

