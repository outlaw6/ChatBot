from chatterbot import ChatBot

bot = ChatBot('Milan', storage_adapter='chatterbot.storage.SQLStorageAdapter',\
               input_adapter='chatterbot.input.TerminalAdapter',\
               output_adapter='chatterbot.output.TerminalAdapter',\
      database='./db.sqlite3')

while True:
      try:
          bot_input = bot.get_response(None)
      except(EOFError):
          break
