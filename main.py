from pyrogram import Client

api_id =
api_hash = ""
plugins = dict(root="plugins")

app = Client("account",api_id = api_id ,api_hash = api_hash ,plugins = plugins)



app.run()