import discord
from discord.ext import commands
import time
import os
import asyncio
from discord import Forbidden
import requests
import string
import random
import aiohttp
import io

"""
If you want to install all these packages here you go:
pip install discord==1.7.0
pip install time
pip install os
pip install asyncio
pip install random
pip install string
pip install requests
pip install io
pip install aiohttp

DISCLAIMER:
    
Note that some commands here are made by astraa so credits to him <3
Also this is kinda broken ngl
"""


# Replace these with the actual IDs of your master and servant accounts
MASTER_USER_ID = 1116005717183299725  # Master account ID
SERVANT_USER_ID = 1244995157523435581  # Servant account ID
SERVANTTOKEN='MTI0NDk5NTE1NzUyMzQzNTU4MQ.G9uh6r.MM82_dnoejZxaZSsRcVwxXEoGb2uvZhVlTi1M4'
IPINFO_API_TOKEN = "7d7c35ba54fdf1"
PREFIX = ">"


# Initialize the bot
bot = commands.Bot(command_prefix=PREFIX)

# Event to handle messages
@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author.id == SERVANT_USER_ID:
        return

    # Check if the message is from the master account and starts with the command prefix
    if message.author.id == MASTER_USER_ID:
        # Process commands
        await bot.process_commands(message)

@bot.event
async def on_ready():
    print('''

 ██▓     ██▓▄▄▄█████▓▄▄▄█████▓ ██▓    ▓█████    ▓█████▄ ▓█████ ██▒   █▓ ██▓ ██▓    
▓██▒    ▓██▒▓  ██▒ ▓▒▓  ██▒ ▓▒▓██▒    ▓█   ▀    ▒██▀ ██▌▓█   ▀▓██░   █▒▓██▒▓██▒    
▒██░    ▒██▒▒ ▓██░ ▒░▒ ▓██░ ▒░▒██░    ▒███      ░██   █▌▒███   ▓██  █▒░▒██▒▒██░    
▒██░    ░██░░ ▓██▓ ░ ░ ▓██▓ ░ ▒██░    ▒▓█  ▄    ░▓█▄   ▌▒▓█  ▄  ▒██ █░░░██░▒██░    
░██████▒░██░  ▒██▒ ░   ▒██▒ ░ ░██████▒░▒████▒   ░▒████▓ ░▒████▒  ▒▀█░  ░██░░██████▒
░ ▒░▓  ░░▓    ▒ ░░     ▒ ░░   ░ ▒░▓  ░░░ ▒░ ░    ▒▒▓  ▒ ░░ ▒░ ░  ░ ▐░  ░▓  ░ ▒░▓  ░
░ ░ ▒  ░ ▒ ░    ░        ░    ░ ░ ▒  ░ ░ ░  ░    ░ ▒  ▒  ░ ░  ░  ░ ░░   ▒ ░░ ░ ▒  ░
  ░ ░    ▒ ░  ░        ░        ░ ░      ░       ░ ░  ░    ░       ░░   ▒ ░  ░ ░   
    ░  ░ ░                        ░  ░   ░  ░      ░       ░  ░     ░   ░      ░  ░
          
    ''')
    


    time.sleep(2)
    print(f"[+] Logged in as: {bot.user.name}")
    print(f'[!] Servant ID: {SERVANT_USER_ID}')
    activity = discord.Streaming(name="Little devil", url="https://www.youtube.com/watch?v=2g5xkLqIElU")
    await bot.change_presence(activity=activity)

bot.remove_command('help')

'''
# Command to respond to >help
@bot.command(name='help1')
async def help_command(ctx):
    if ctx.author.id == MASTER_USER_ID:
        await ctx.send("Hello, how can I help?")

'''



@bot.command()
async def ping(ctx):
    if ctx.author.id == MASTER_USER_ID:
        ping = round(bot.latency * 1000)
        response = f'Pong! {ping} MS'
        await ctx.send(response)

@bot.command()
async def minesweeper(ctx, size: int=5):
    if ctx.author.id == MASTER_USER_ID:
        #await ctx.message.delete()
        size = max(min(size, 8), 2)
        
        bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for _ in range(size - 1)]
        is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
        has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
        
        m_numbers = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣']
        m_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        message = "**Click to play**:\n"
        for y in range(size):
            for x in range(size):
                tile = "||{}||".format(chr(11036))  
                if has_bomb(x, y):
                    tile = "||{}||".format(chr(128163))  
                else:
                    count = 0
                    for xmod, ymod in m_offsets:
                        if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                            count += 1
                    if count != 0:
                        tile = "||{}||".format(m_numbers[count - 1])
                message += tile
            message += "\n"
        
        await ctx.send(message)


@bot.command()
async def help(ctx):
    if ctx.author.id == MASTER_USER_ID:
        message = await ctx.send("```ini\n[Welcome to the Little Devil selfbot created by el diablo, please stand by]\n```")

        await asyncio.sleep(1)  
            
        new_message = "```ini\nCreated by diablo this is a multihandler\n[>info]: >info <userid> or <username>\n[>ping]: Returns your MS\n[>geocode]: >geocode <latitude> <longitude> (must be integers)\n[>exit]: Exits out of the selfbot\n[>iplookup]: >iplookup <ip>\n[>minesweeper]: play a game of minesweeper :D\n[>hack]: >hack (user) this time its a fun command```"
        await message.edit(content=new_message)



@bot.command()
async def hack(ctx, user: discord.Member=None):
    if ctx.author.id == MASTER_USER_ID:
        #await ctx.message.delete()
        gender = ["Male", "Female", "Trans", "Other", "Retard"]
        age = str(random.randrange(10, 25))
        height = ['4\'6\"', '4\'7\"', '4\'8\"', '4\'9\"', '4\'10\"', '4\'11\"', '5\'0\"', '5\'1\"', '5\'2\"', '5\'3\"',
                '5\'4\"', '5\'5\"',
                '5\'6\"', '5\'7\"', '5\'8\"', '5\'9\"', '5\'10\"', '5\'11\"', '6\'0\"', '6\'1\"', '6\'2\"', '6\'3\"',
                '6\'4\"', '6\'5\"',
                '6\'6\"', '6\'7\"', '6\'8\"', '6\'9\"', '6\'10\"', '6\'11\"']
        weight = str(random.randrange(60, 300))
        hair_color = ["Black", "Brown", "Blonde", "White", "Gray", "Red"]
        skin_color = ["White", "Pale", "Brown", "Black", "Light-Skin"]
        religion = ["Christian", "Muslim", "Atheist", "Hindu", "Buddhist", "Jewish"]
        sexuality = ["Straight", "Gay", "Homo", "Bi", "Bi-Sexual", "Lesbian", "Pansexual"]
        education = ["High School", "College", "Middle School", "Elementary School", "Pre School",
                    "Retard never went to school LOL"]
        ethnicity = ["White", "African American", "Asian", "Latino", "Latina", "American", "Mexican", "Korean", "Chinese",
                    "Arab", "Italian", "Puerto Rican", "Non-Hispanic", "Russian", "Canadian", "European", "Indian"]
        occupation = ["Retard has no job LOL", "Certified discord retard", "Janitor", "Police Officer", "Teacher",
                    "Cashier", "Clerk", "Waiter", "Waitress", "Grocery Bagger", "Retailer", "Sales-Person", "Artist",
                    "Singer", "Rapper", "Trapper", "Discord Thug", "Gangster", "Discord Packer", "Mechanic", "Carpenter",
                    "Electrician", "Lawyer", "Doctor", "Programmer", "Software Engineer", "Scientist"]
        salary = ["Retard makes no money LOL", "$" + str(random.randrange(0, 1000)), '<$50,000', '<$75,000', "$100,000",
                "$125,000", "$150,000", "$175,000",
                "$200,000+"]
        location = ["Retard lives in his mom's basement LOL", "America", "United States", "Europe", "Poland", "Mexico",
                    "Russia", "Pakistan", "India",
                    "Some random third world country", "Canada", "Alabama", "Alaska", "Arizona", "Arkansas", "California",
                    "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana",
                    "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
                    "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
                    "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
                    "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
        email = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@protonmail.com", "@disposablemail.com",
                "@aol.com", "@edu.com", "@icloud.com", "@gmx.net", "@yandex.com"]
        dob = f'{random.randrange(1, 13)}/{random.randrange(1, 32)}/{random.randrange(1950, 2021)}'
        name = ['James Smith', "Michael Smith", "Robert Smith", "Maria Garcia", "David Smith", "Maria Rodriguez",
                "Mary Smith", "Maria Hernandez", "Maria Martinez", "James Johnson", "Catherine Smoaks", "Cindi Emerick",
                "Trudie Peasley", "Josie Dowler", "Jefferey Amon", "Kyung Kernan", "Lola Barreiro",
                "Barabara Nuss", "Lien Barmore", "Donnell Kuhlmann", "Geoffrey Torre", "Allan Craft",
                "Elvira Lucien", "Jeanelle Orem", "Shantelle Lige", "Chassidy Reinhardt", "Adam Delange",
                "Anabel Rini", "Delbert Kruse", "Celeste Baumeister", "Jon Flanary", "Danette Uhler", "Xochitl Parton",
                "Derek Hetrick", "Chasity Hedge", "Antonia Gonsoulin", "Tod Kinkead", "Chastity Lazar", "Jazmin Aumick",
                "Janet Slusser", "Junita Cagle", "Stepanie Blandford", "Lang Schaff", "Kaila Bier", "Ezra Battey",
                "Bart Maddux", "Shiloh Raulston", "Carrie Kimber", "Zack Polite", "Marni Larson", "Justa Spear"]
        phone = f'({random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)})-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}'
        if user is None:
            user = ctx.author
            password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                        "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                        "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
            message = await ctx.send(f"`Hacking {user}...\n`")
            await asyncio.sleep(1)
            await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
            await asyncio.sleep(1)
            await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
            await asyncio.sleep(1)
            await message.edit(
                content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
            await asyncio.sleep(1)
            await message.edit(
                content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
            await asyncio.sleep(1)
            await message.edit(
                content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
            await asyncio.sleep(1)
            await message.edit(
                content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")
        else:
            password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                        "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                        "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
            message = await ctx.send(f"`Hacking {user}...\n`")
            await asyncio.sleep(1)
            await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
            await asyncio.sleep(1)
            await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
            await asyncio.sleep(1)
            await message.edit(
                content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
            await asyncio.sleep(1)
            await message.edit(
                content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
            await asyncio.sleep(1)
            await message.edit(
                content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
            await asyncio.sleep(1)
            await message.edit(
                content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")


@bot.command()
async def geocode(ctx, latitude, longitude):
    if ctx.author.id == MASTER_USER_ID:
        response = f"```diff\n- Address: ```https://maps.google.com/?q={latitude},{longitude}"
        await ctx.send(response)











@bot.command()
async def iplookup(ctx, ip: str):
    if ctx.author.id == MASTER_USER_ID:
        url = f"https://ipinfo.io/{ip}/json?token={IPINFO_API_TOKEN}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            ip = data.get('ip', 'N/A')
            city = data.get('city', 'N/A')
            region = data.get('region', 'N/A')
            country = data.get('country', 'N/A')
            loc = data.get('loc', 'N/A')
            org = data.get('org', 'N/A')
            postal = data.get('postal', 'N/A')
            timezone = data.get('timezone', 'N/A')
            
            response = (
                f"```ini\n"
                f"[IP Information for {ip}]\n"
                f"[City] = {city}\n"
                f"[Region] = {region}\n"
                f"[Country] = {country}\n"
                f"[Location] = {loc}\n"
                f"[Organization] = {org}\n"
                f"[Postal Code] = {postal}\n"
                f"[Timezone] = {timezone}\n"
                f"```"
            )
        else:
            response = f"Could not retrieve information for IP: {ip}. Please ensure the IP address is valid."
        message  =  await ctx.send("```ini\n[Stand by as we fetch the ip]\n```")
        time.sleep(2)
        await message.edit(content = response)







@bot.command()
async def exit(ctx):
    if ctx.author.id == MASTER_USER_ID:
        print(f'Exiting python process, Logging out of {bot.user.name}')
        await ctx.send('```ini\n [exiting] ```')
        await bot.change_presence(activity=None)
        os._exit(0)


@bot.command()
async def info(ctx, user: discord.User):
    if ctx.author.id == MASTER_USER_ID:
        user_id = user.id
        username = user.name
        tag = user.discriminator
        created_at = user.created_at.strftime("%Y-%m-%d %H:%M:%S")
        avatar_url = user.avatar_url if user.avatar else user.default_avatar_url
        
        
        badges = []
        if user.public_flags.staff:
            badges.append('Staff')
        if user.public_flags.partner:
            badges.append('Partner')
        if user.public_flags.hypesquad:
            badges.append('HypeSquad')
        
        
        badges_str = ', '.join(badges) if badges else 'None'
        
        response = (
            f'[UserInfo]\n'
            f'UserID = {user_id}\n'
            f'Username = {username}#{tag}\n'
            f'Avatar = {avatar_url}\n'
            f'AccountCreationDate = {created_at}\n'
            f'\n'
            f'[AccountBadges]\n'
            f'Badges = {badges_str}\n'
        )
        
        await ctx.send(f'```ini\n{response}```')



# Run the bot with the token of the servan
bot.run(SERVANTTOKEN, bot = False)