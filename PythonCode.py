import discord
from discord.ext import commands
import asyncio

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
bot = commands.Bot(command_prefix = '>>', intents = intents)
Prefix = ">>"

@bot.event
async def on_ready():
    print("I am woke")
    AwakenChannel = bot.get_channel(850391054029160468)
    await AwakenChannel.send("Python program is operational.")
    
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(849727570340610083)
    await channel.send(f'Welcome {member.mention} to the foundation, Create an OC (Original Character) If you wish to participate.')

@bot.event
async def on_member_remove(LeftMember):
    Targetchannel = bot.get_channel(849727570340610083)
    await Targetchannel.send(f'{LeftMember.mention} Has resigned from the foundation.')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please submit the arguements of the command (Please mention the user or the ID of the user you want to ban).')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have permission to execute this command.")

#The below code bans player.
@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

#The below code unbans player.
@bot.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

bot.run("NTY5NTA5MDI0MjQ5MTUxNTEw.XLxqnA.OprPKNe7NsbGvWBA4ByRMsohoN8")
