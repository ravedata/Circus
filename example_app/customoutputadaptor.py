
from __future__ import unicode_literals
from chatterbot.input import InputAdapter
from chatterbot.conversation import Statement
from chatterbot.input.variable_input_type_adapter import InputAdapter

#ass CustomeVariableInputTypeAdapter(InputAdapter):

#  JSON = 'json'
#  TEXT = 'text'
#  OBJECT = 'object'
#  VALID_FORMATS = (JSON, TEXT, OBJECT, )

#  def detect_type(self, statement):
#      import sys

#      if sys.version_info[0] < 3:
#          string_types = basestring # NOQA
#      else:
#          string_types = str

#      if hasattr(statement, 'text'):
#          return self.OBJECT
#      if isinstance(statement, string_types):
#          return self.TEXT
#      if isinstance(statement, dict):
#          return self.JSON

#      input_type = type(statement)

#      raise self.UnrecognizedInputFormatException(
#          'The type {} is not recognized as a valid input type.'.format(
#              input_type
#          )
#      )

#  def process_input(self, statement):
#      input_type = self.detect_type(statement)

#      # Return the statement object without modification
#      if input_type == self.OBJECT:
#          print('without')
#          return statement

#      # Convert the input string into a statement object
#      if input_type == self.TEXT:
#          print('string')
#          return Statement(statement)

#      # Convert input dictionary into a statement object
#      if input_type == self.JSON:
#          input_json = dict(statement)
#          text = input_json['text']
#          del input_json['text']
#          #print(text)
#          if text.isnumeric():
#              CustomOutputAdapter().add_f(text)
#              text = 'nearby restaurants'

#              #CustomOutputAdapter.printme(self, 'hi')

#          return Statement(text, **input_json)

#  class UnrecognizedInputFormatException(Exception):
#      """
#      Exception raised when an input format is specified that is
#      not in the VariableInputTypeAdapter.VALID_FORMATS variable.
#      """

#      def __init__(self, value='The input format was not recognized.'):
#          self.value = value

#      def __str__(self):
#          return repr(self.value)



import datetime

now = datetime.datetime.today()


from chatterbot.output.output_adapter import OutputAdapter
import requests

from chatterbot.conversation import statement
## Call the weather package  here


class CustomOutputAdapter(OutputAdapter):
    """
    A generic class that can be overridden by a subclass to provide extended
    functionality, such as delivering a response to an API endpoint.
    """
    glo = 0
    def add_f(self, text):

        global glo
        glo = text
        print(glo)
    def process_response(self, statement, session_id=None):
        """
        Override this method in a subclass to implement customized functionality.

        :param statement: The statement that the chat bot has produced in response to some input.

        :param session_id: The unique id of the current chat session.

        :returns: The response statement.
        """
       # statement.text="Overridden";

        #statement.text = "weather";
        if 'Weather' in statement.text:
            r = requests.get(
                'http://api.openweathermap.org/data/2.5/weather?zip=201309,in&appid=59a26d0367ff724f5328fd04f954e3ee')
            json_object = r.json()
            # print(r.text)
            temp_k = float(json_object['main']['temp'])
            temp_c = round(temp_k - 273, 2)
            vis = json_object['visibility']
            temp_mi = round(float(json_object['main']['temp_min']) - 273, 2)
            temp_ma = round(float(json_object['main']['temp_max']) - 273, 2)
            humid = round(float(json_object['main']['humidity']), 2)
            cntry = json_object['sys']['country']
            cty = json_object['name']
            statement.text = '<b>Current Temp: </b>' + str(temp_c) + '<br>' + '<b>Max Temp: </b>' + str(temp_ma) + '<br>' + '<b>Min Temp: </b>' + str(temp_mi) + '<br>' + '<b>Current Visibility: </b>' + str(vis) + '<br>' + '<b>Humidity: </b>' + str(humid) + '<br>' + '<b>City Name: </b>' + str(cty) + '<br>' + '<b>Country Name: </b>' + str(cntry)
            return statement
            # statement.text="The weather today is beautiful"
        elif 'news' in statement.text:
            b = "";
            news = [];
            r = requests.get(
                'https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=82033ea854e846d9bfdf333d3eff8b3a')
            json_object = r.json()
            print(r.text)
            # for i in range(0,5):
            for i in range(0, 5):
                news_title = str(json_object['articles'][i]['title'])
                news_url = str(json_object['articles'][i]['url'])
                a = '<b>Title : </b>' + str(news_title) + '<br>' + '<b>Link : </b>' + '<a href = "' + news_url + '"' + 'target="_blank">Click here</a>' + '<br>'
                b = b + str(a) + '<br>'
                print(news_url)
            statement.text = '<b>Top 5 Headlines: </b>' + '<br>' + '<br>' + str(b)
            return statement
            # statement.text = r.text
        elif 'restaurant' in statement.text:
            print(self.glo)
            #print(CustomOutputAdapter.add_f.glo)

                #print(CustomeVariableInputTypeAdapter().add_f(a))
            b=str
            a = "";
            res = [];
            #print(abc)
            r = requests.get(
                'https://developers.zomato.com/api/v2.1/search?entity_type=city&q=noida%20sector%2062&apikey=747b5cac925195db25a1e09a3976be75')
            json_object = r.json()
            for i in range(0, 5):
                res_name = json_object['restaurants'][i]['restaurant']['name']
                res_address = json_object['restaurants'][i]['restaurant']['location']['address']
                res_photo = json_object['restaurants'][i]['restaurant']['thumb']
                res_link = json_object['restaurants'][i]['restaurant']['photos_url']
                print(r.text)
                b = '<b>Name : </b>' + str(res_name) + '<br>' + '<b>Address : </b>' + str(res_address) + '<br>' + '<b>Photo : </b>' + '<img src="' + res_photo + '" alt="Restaurnt" width="60" height="60">' + '<br>' + '<b>Link : </b>' + '<a href = "' + res_link + '"' + 'target="_blank">Click here</a>' + '<br>' + '<br>'
                print(res_address)
                # res.append(b)
                a = a + str(b)
            statement.text = '<b>Top 5 Restaurants: </b>' + '<br>' + '<br>' + str(a)

            return statement
        elif 'pnr' in statement.text:
            a = "";
            res = [];
            r = requests.get(
                'http://api.erail.in/pnr?key=94cme36em6&pnr=6533543051')
            json_object = r.json()
            # pnr_jdate = json_object['doj']
            # pnr_trainno = json_object['train']['number']
            # pnr_trainname = json_object['to_station']['name']
            # a = str(pnr_jdate) + '<br>' + str(pnr_trainno) + '<br>' + str(pnr_trainname) + '<br>'
            # print(r.text)
            statement.text = r.text
            return statement
        elif 'Cricket' in statement.text:
            a = ""
            k = 0
            r = requests.get(
                'http://cricapi.com/api/matches?apikey=9BO8SbUuzie9Ox5jzxEgit73Ty72')
            json_object = r.json()
            now = datetime.datetime.now()
            for i in range(0, 64):
                matchid = json_object['matches'][i]['unique_id']
                team1 = json_object['matches'][i]['team-1']
                team2 = json_object['matches'][i]['team-2']
                date = json_object['matches'][i]['date']
                #now1 = str(now)
                Sysdate = str(now)
                split_Sysdate, x = Sysdate.split(' ')
                #print(split_Sysdate)
                date1 = str(date)
                split_date, z = date1.split('T')
                #print(split_date)
                if team1 == 'India' or team2 == 'India':
                    if split_date == split_Sysdate:
                        a = str(matchid)
                        k = k + 1
                        break
                    break
            if k==1:
            #a = 1119500;
                x = requests.get(
                    'http://cricapi.com/api/cricketScore?unique_id=' + str(a) + '&apikey=9BO8SbUuzie9Ox5jzxEgit73Ty72')
                json_object = x.json()
                status = json_object['stat']
                score = json_object['description']
                # print(r.text)
                b = '<b>status : </b>' + str(status) + '<br>' + '<b>score : + </b>' + str(score)  + '<br>' + '<br>'
                print(b)
                statement.text = '<b>Live Cricket: </b>' + '<br>' + '<br>' + str(b)
            else:
                statement.text = 'Match Not started Yet'

            return statement
        else:
            return statement