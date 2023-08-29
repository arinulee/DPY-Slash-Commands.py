import discord
from discord import app_commands 

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False #we use this so the bot doesn't sync commands more than once

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #check if slash commands have been synced 
            await tree.sync(guild = discord.Object(id=guild_id)) #guild specific: leave blank if global (global registration can take 1-24 hours)
            self.synced = True
        print(f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(guild = discord.Object(id=guild_id), name = 'tester', description='testing') #guild specific slash command
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"I am working! I was made with Discord.py!", ephemeral = True) 

client.run('MTE0NTc5MzQ2MjcyNjMxMjAxNg.G6dg9T.IEXdyGhI0pQJ9x4e0F7cAa03FGs03DAJu8eKMg')
