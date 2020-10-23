import discord
from discord.ext import commands

client = commands.Bot(command_prefix='--')

@client.event
async def on_ready():
    bot_channel = client.get_channel(768867455510118471)
    print('We have logged in as {0.user}'.format(client))

    await bot_channel.send('Bot Online!')

@client.command(name = 'random')
async def version(context):

    if context.message.author == client.user: #checks that the message author is different from the bot
        return

    print('Randomized teams generator')

    my_embed= discord.Embed(title = 'Teams', description='Randomized teams', color=0xbe00ee)
    my_embed.add_field(name = 'TEAM A', value = 'x', inline = False)
    my_embed.add_field(name = 'TEAM B', value = 'y', inline = False)


    await context.message.channel.send(embed = my_embed)


@client.command(name = 'list')
async def members_list(request):
    channel = client.get_channel(768867455510118471)
    curMembers = []
    for member in VoiceChannel.members:
        curMembers.append(member)

    await channel.send(curMembers)

    #await context.message.channel.send(currMember)


#Run client on the server
client.run('NzY4ODI5Nzk1MDE4MzQyNDQw.X5GKiw.ss0u5N1shVqY8KeQNUIc_Ka-QiY')

 