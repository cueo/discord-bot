import os

import discord

from channels import PLACES, STREAMS, STATES
from env import load

load()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')

STATE_CATEGORY = '🌆 STATES'


# noinspection PyAttributeOutsideInit
class MrRobot(discord.Client):
    async def on_ready(self):
        for _guild in self.guilds:
            if _guild.name == GUILD:
                self.guild = _guild

        print(f'Connected to server={self.guild.name}')

        self.channels = [channel.name for channel in self.guild.channels]

    async def on_message(self, message):
        content = message.content
        channel = message.channel
        print(f'Received message={content} in channel={channel}')

        if content == 'ping':
            await channel.send('pong')

        msg = content.lower()
        channels = {'general', 'test'}
        if channel.name in channels and msg in STATES:
            print(f'Creating channel for state={msg}')
            await self.create_channel(msg, STATE_CATEGORY, dryrun=False)

    async def create_channel(self, name, category_name, dryrun=True):
        if name in self.channels:
            print(f'channel={name} already exists')
            return

        print(f'Creating channel={name} under category={category_name}')
        category = discord.utils.get(self.guild.categories, name=category_name)
        if not dryrun:
            try:
                await self.guild.create_text_channel(name, category=category)
            except TypeError as e:
                print(f'Failed due to error={e}')


client = MrRobot()
client.run(TOKEN)