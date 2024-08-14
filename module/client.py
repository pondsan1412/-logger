import discord
from discord.ext import commands
import os

class discord_client(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned(),
            help_command=None,
            description='logger bot (ล้มละลาย)',
            intents=discord.Intents.all()
        )

    async def setup_hook(self):
        load_folder = "./features"
        for filename in os.listdir(load_folder):
            if filename.endswith('.py') and filename != '__':
                module_name = filename[:-3]
                try:

                    module_path = f"{load_folder}.{module_name}"
                    await self.load_extension(module_path)
                except Exception as e:
                    print(f'failed to load extension {module_name}')

    async def on_ready(self):
        print(self.user.name)