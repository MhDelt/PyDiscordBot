from discord.ext import commands
import random
import re
import dbHandler

description = '''Bot, that hates you, your family and your cat.'''

bot = commands.Bot(command_prefix='!', description=description)


@bot.event
async def on_ready():
    print(f'{bot.user.name} ready to fuck you off')
    print('_____')


@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return
    message_str = message.content.lower()
    if message_str == 'ping':
        await message.channel.send(f'Fuck you, {message.author.mention}!')
    else:
        await bot.process_commands(message)


@bot.command(name='roll', description='Rolls one dice with N faces or N dices with M faces')
async def roll(ctx, *args):
    ans = 'Bonk'
    if len(args) == 0:
        ans = 'So what did you expect from me? Im not a magician, you twat'
    elif len(args) == 1:
        if args[0].isnumeric():
            res = random.randint(1, int(args[0]))
            ans = 'Your fucking result is ' + str(res)
        elif args[0].lower() == 'rick':
            ans = 'https://youtu.be/dQw4w9WgXcQ'
        else:
            ans = 'Number of faces is NUMBER, idiot'
    elif len(args) == 2:
        if args[0].isnumeric() and args[1].isnumeric():
            sum = 0
            ans = ''
            for i in range(int(args[0])):
                res = random.randint(1, int(args[1]))
                sum += res
                ans += "{0}, ".format(res)

            ans = 'Here are your fucking dices: ' + str(ans) + ' fucking sum is ' + str(sum) + '. Now, go fuck yourself'
        else:
            ans = 'Are you fucking stupid? Dices and faces must be fucking NUMBERS, your fucking cunt'
    await ctx.send(ans)


@bot.command(name='fuck', description='Fucks someone')
async def fuck(ctx, *name):
    ans = 'Bonk'
    if len(name) == 0:
        ans = f'Fuck you, {ctx.message.author.mention}'
    elif len(name) == 1:
        name = str(name)
        name = re.sub("\{|\}|\(|\)|\'|\,", '', name)
        ans = f'Fuck you, {name}'
    else:
        ans = 'Fuck you all, '
        for i in name:
            n = str(i)
            n = re.sub("\{|\}|\(|\)|\'|\,", '', n)
            ans += n
    await ctx.send(ans)


@bot.command(name='add', description='Adds event to list')
async def add_event(ctx, name='EmptyName'):
    id = dbHandler.create_event(str(name))
    await ctx.send(f'Fucking event added with id {id}')


@bot.command(name='events', description='Gets all events in the list')
async def get_event(ctx):
    events = dbHandler.get_all_events()
    if len(events) == 0:
        ans = 'There is no fucking events'
    else:
        ans = ''
        for event in events:
            ans += f'{event.doc_id}) {event["name"]} \n'
    await ctx.send(ans)


@bot.command(name='remove', description='Remove event by ID')
async def remove_event(ctx, id=-1):
    if id == -1:
        ans = 'Which event I should remove, dumbass?'
    else:
        dbHandler.remove_event_by_id(id)
        ans = f'Event {id} removed'
    await ctx.send(ans)


def run(token):
    bot.run(token)
