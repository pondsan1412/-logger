from module.client import discord_client

app = discord_client()
app.run(
    token=None,
    reconnect=True,
    log_handler=None,

)

