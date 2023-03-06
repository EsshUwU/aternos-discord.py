import discord
from discord.ext import commands 
from discord import app_commands
from python_aternos import Client, Lists
from dotenv import load_dotenv
import os


load_dotenv()
discord_token = os.getenv("TOKEN")
aternos_username = os.getenv("aternos_username")
aternos_password = os.getenv("aternos_password")
disc_userid = os.getenv("discord_user_id")


class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"we have logged in as {self.user}")


clientt = aclient()
tree = app_commands.CommandTree(clientt)

aternos = Client.from_credentials(aternos_username, aternos_password)
servs = aternos.list_servers()
myserv = servs[0]


@tree.command(name = "start", description = "Starts the Minecraft server")
async def self(interaction: discord.Interaction):
    global myserv
    try:
        myserv.start()   
        await interaction.response.send_message('Starting the Server!')
    except:
        await interaction.response.send_message('Server is already running')



@tree.command(name = "stop", description = "stop the Minecraft server")
async def self(interaction: discord.Interaction):
    user = interaction.user.id
    global disc_userid
    disc_userid2 = int(disc_userid)
    if user == disc_userid2: 
        global myserv
        myserv.stop()
        await interaction.response.send_message('Stopping the Server.')         
    else:
        await interaction.response.send_message('You cannot use this command.')


@tree.command(name = "players", description = "Displays current Online Players")
async def self(interaction: discord.Interaction):
    global myserv
    player_list = myserv.players_list
    player_count = myserv.players_count

    output_playerlist = '\n'.join(player_list)
    ff = '======================='

    await interaction.response.send_message(f"**Current Players Online : {player_count}**\n{ff}\n{output_playerlist}\n{ff}")
        

@tree.command(name = "serverip", description = "stop the Minecraft server")
async def self(interaction: discord.Interaction):
    global myserv
    server_add = myserv.address
    await interaction.response.send_message(server_add)

@tree.command(name = "status", description = "Shows server Status")
async def self(interaction: discord.Interaction):
    global myserv
    server_status = myserv.status
    await interaction.response.send_message(f"**Status : {server_status}**")


@tree.command(name = "ban", description = "Bans a player")
async def self(interaction: discord.Interaction,playername: str):
    user = interaction.user.id
    global disc_userid
    disc_userid2 = int(disc_userid)
    if user == disc_userid2: 
        global myserv
        ban = myserv.players(Lists.ban)
        ban.add(playername)
        await interaction.response.send_message(f"Banned {playername}")
    else:
        await interaction.response.send_message("You cannot use this command.")

@tree.command(name = "unban", description = "unbans a player")
async def self(interaction: discord.Interaction,playername: str):
    user = interaction.user.id
    global disc_userid
    disc_userid2 = int(disc_userid)
    if user == disc_userid2: 
        global myserv
        ban = myserv.players(Lists.ban)
        ban.remove(playername)
        await interaction.response.send_message(f"unbanned {playername}")
    else:
        await interaction.response.send_message("You cannout use this command.")

@tree.command(name = "serverinfo", description = "Display's the server info")
async def self(interaction: discord.Interaction):
    global myserv
    v1 = myserv.address
    v2 = myserv.css_class
    v3 = myserv.is_java
    v4 = myserv.motd
    v5 = myserv.slots
    v6 = myserv.players_count
    v7 = myserv.ram
    v8 = myserv.software
    v9 = myserv.version

    embed1 = discord.Embed(title="Server Information",colour=discord.Colour.blue())
    embed1.set_thumbnail(url = "https://cdn.discordapp.com/attachments/807644444609347635/1082016687718670407/1gYrULL7Ji6sFmUJnUgAAAAAAAAAAA0zRZuISC3ksF7wAAAABJRU5ErkJggg.png")
    embed1.add_field(name="Server Address", value=v1,inline=False)
    embed1.add_field(name="Server Status", value=v2,inline=False)
    if v3 == True:
        v33 = "Java"
    else:
        v33 = "Bedrock"
    embed1.add_field(name="Edition", value=v33,inline=False)
    embed1.add_field(name="Minecraft Version", value=v9,inline=False)
    embed1.add_field(name="Online Players", value=f"{v6} of {v5}",inline=False)
    embed1.add_field(name="Server Ram", value=v7,inline=False)
    embed1.add_field(name="Software", value=v8,inline=False)
    embed1.add_field(name="Message of the day", value=v4,inline=False)
    
    await interaction.response.send_message(embed=embed1)
    
clientt.run(discord_token)


