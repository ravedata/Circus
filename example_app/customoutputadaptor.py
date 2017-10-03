from chatterbot.output.output_adapter import OutputAdapter
from chatterbot.conversation import statement
import requests

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

        #statement.text = "weather";
        if 'Weather' not in statement.text:
            return statement

        else:
            r = requests.get(
                'http://api.openweathermap.org/data/2.5/weather?zip=201309,in&appid=59a26d0367ff724f5328fd04f954e3ee')
            json_object = r.json()
            # print(r.text)
            temp_k=float(json_object['main']['temp'])
            temp_c=round(temp_k - 273,2)
            vis=json_object['visibility']
            temp_mi=round(float(json_object['main']['temp_min']) - 273, 2)
            temp_ma=round(float(json_object['main']['temp_max']) - 273, 2)
            humid=round(float(json_object['main']['humidity']), 2)
            cntry = json_object['sys']['country']
            cty = json_object['name']
            statement.text='Current Temp: '+str(temp_c)+'<br>'+'Max Temp: '+str(temp_ma)+'<br>'+'Min Temp: '+'<br>'+str(temp_mi)+'Current Visibility:'+str(vis)+'<br>'+'Humidity: '+str(humid)+'<br>'+'City Name: '+str(cty)+'<br>'+'Country Name: '+str(cntry)
            #statement.text="The weather today is beautiful"
            return statement

