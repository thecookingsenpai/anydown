import requests

def telegram_bot_sendtext(bot_message):

   bot_chatID  = "1268192061"

   bot_token = '1108561287:AAFt48JjwPsIeUvBzWTjVXOsxBXEUtRnnZQ'
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()

telegram_bot_sendtext("DONE")