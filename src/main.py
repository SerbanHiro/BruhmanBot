import discord
import os
import random
import asyncio
from replit import db
#from keep_alive import keep_alive
from raspunsuri import update_cuvinte
from cuvinte import update_cuvinte_bruhman

from discord.ext import commands
from discord.ext import tasks

bot = commands.Bot(command_prefix='$')
bot.remove_command('help')

client = discord.Client()

ID = 0 # ID ul pt camera
troll = 0 # bruhman troll

bruh=[
  "esti fraier",
  "esti adoptat"
]

# LOGGING PHASE
@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))
  mytask.start()
# LOGGING PHASE

# HELP
@bot.command(pass_context=True)
async def help(ctx):
  #print(message.author.roles)
  if "access" in [y.name.lower() for y in ctx.message.author.roles]:
    await ctx.message.channel.send("```bash\nDaca este prima oara cand folositi botul, scrieti \"$initialize\"\nDaca vrei sa faci \"factory reset\" scrie \"$clear\" si dupa \"$initialize\"\nAi nevoie de un rank special numit \"access\"\n\n-COMMANDS-\nPentru a sterge un anumit numar de mesaje scrieti \"$purge <amount>\"\nPentru ca \"Browman\" sa primeasca ping trebuie sa puneti \"$setroom <channel ID>\", daca vreti sa va opriti scrieti \"$setroom 0\"\n-COMMANDS-\n\n-Raspunsuri-\nPentru a vedea o lista cu toate raspunsurile existente scrie \"$list raspunsuri\"\nPentru a adauga un raspuns nou scrie \"$rnew raspuns\"\nPentru a sterge un raspuns deja existent scrie \"$rdel raspuns\"\n-Raspunsuri-\n\n-Cuvinte Specifice-\n Pentru a vedea o lista cu toate cuvintele interzise existente scrie \"$list cuvinte\"\nPentru a adauga un cuvant nou scrie \"$cnew cuvant\"\nPentru a sterge un cuvant deja existent scrie \"$cdel raspuns\"\n-Cuvinte Specifice-\n\n-User Related-\nTEMPORAR: \"$bruhman enable\" tot timpul cand browman scrie ori primeste reply cu \"esti fraier\" ori cu \"esti adoptat\", sa fie folosit cu incredere...\nTEMPORAR: \"$bruhman disable\" face sa nu ii mai dea reply\nVOICECHAT TROLL ENABLE: Este o sansa ca intre 10 secunde si 1 minut browman sa fie scos din vc, pentru a activa scrie \"$browvc enable\"\nVOICECHAT TROLL DISABLE: Pentru ca browman sa nu mai fie scos random scrie \"$browvc disable\" \n\n-User Related-\n\nSource code: \"$github\"```")
  else:
    await ctx.message.channel.send("N ai acces johnule")
# HELP

# INITIALIZE DATABASE
@bot.command()
async def initialize(ctx):
  if "access" in [y.name.lower() for y in ctx.message.author.roles]:
    # INITIALIZE BRUHMAN WORDS
    db["cuvinte_bruhman"]=[
      "trist",
      "no shit sherlock",
      "shit"
    ]
  
    # INITIALIZE BRUHMAN ANSWERS
    db["cuvinte"]=[
      "Esti adoptat",
      "Ratie + camile",
      "I did your mom"
    ]
    await ctx.message.channel.send("Data de baze a fost initializata!")
  else:
    await ctx.message.channel.send("La asta nici mort n ai acces boss")
# INITIALIZE DATABASE

# CLEAR DATABASE
@bot.command()
async def clear(ctx):
  db.clear()
  await ctx.message.channel.send("Data de baze a fost stearsa! Scrie \"$initialize\" pentru a o reinitializa.")
# CLEAR DATABASE

# LISTE
@bot.command()
async def list(ctx,arg1):
  if arg1 == "raspunsuri":
    await ctx.message.channel.send(db["cuvinte"])
  elif arg1 == "cuvinte":
    await ctx.message.channel.send(db["cuvinte_bruhman"])
# LISTE

# BRUHMAN TROLL
@bot.command()
async def bruhman(ctx,arg1):
  global troll
  if arg1 == "enable":
    if "access" in [y.name.lower() for y in ctx.message.author.roles]:
      if troll == 0:
        await ctx.message.channel.send("Pfuai ce o sa si o primeasca browman...")
      else:
        await ctx.message.channel.send("Usor johnule ca imediat plange...")
      troll = 1
    else:
      await ctx.message.channel.send("Mama ta e o florareasa ratata")
  elif arg1 == "disable":
    if "access" in [y.name.lower() for y in ctx.message.author.roles]:
      if troll == 1:
        await ctx.message.channel.send("Deja te ai plictisit :(((?")
      else: 
        await ctx.message.channel.send("Ho ma ca deja e dezactivat!!!")
      troll = 0
    else:
      await ctx.message.channel.send("Mama ta e o florareasa ratata + esti foarte fraier")
# BRUHMAN TROLL

# GITHUB
@bot.command()
async def github(ctx):
  await ctx.message.channel.send("https://github.com/SerbanHiro/BruhmanBot")
# GITHUB

# PURGE
@bot.command()
async def purge(ctx,arg1):
  if "access" in [y.name.lower() for y in ctx.message.author.roles]:
    try:
      num=int(arg1)
    except ValueError:
      await ctx.message.channel.send("<amount> in $purge <amount> trebuie sa fie un numar me boy!")
      return
    await ctx.channel.purge(limit = num+1)
  else:
    await ctx.message.channel.send("Hai ca ai rank daca e :)))")
# PURGE

# SET ROOM
@bot.command()
async def setroom(ctx,arg1):
  global ID
  if "access" in [y.name.lower() for y in ctx.message.author.roles]:
    try:
      num=int(arg1)
    except ValueError:
      await ctx.message.channel.send("<ID> in $setroom <ID> trebuie sa fie un numar me boy!")
      return
    ID=num
    await ctx.message.channel.send("Camera de spam a fost setata!")
  else:
    await ctx.message.channel.send("Hai ca ai rank daca e :)))")
# SET ROOM

# ADD NEW RESPONSE TO DATABASE
@bot.command()
async def rnew(ctx):
  if "access" in [y.name.lower() for y in ctx.message.author.roles]:
    cuvinte_noi = ctx.message.content.split("$rnew ",1)[1]
    if update_cuvinte(cuvinte_noi) == 1:
      await ctx.message.channel.send("Deja exista acest raspuns!")
    else:
      await ctx.message.channel.send("Ai adaugat un raspuns nou!")
  else:
    await ctx.message.channel.send("N ai acces johnule")
# ADD NEW RESPONSE TO DATABASE

# REMOVE RESPONSE FROM DATABASE
@bot.command()
async def rdel(ctx):
  if "access" in [y.name.lower() for y in ctx.message.author.roles]:
    if "cuvinte" in db.keys():
      i=0
      for words in db["cuvinte"]:
        if ctx.message.content.split("$rdel ",1)[1] == words:
          break
        i=i+1
      if i == len(db["cuvinte"]):
        await ctx.message.channel.send("Nu exista acest raspuns!")
      else:
        await ctx.message.channel.send("Cuvantul a fost sters!")
        del db["cuvinte"][i]
  else:
    await ctx.message.channel.send("N ai acces johnule")
# REMOVE RESPONSE FROM DATABASE

# ADD NEW WORD TO DATABASE
@bot.command()
async def cnew(ctx):
  if "access" in [y.name.lower() for y in ctx.message.author.roles]:
    cuvinte_noi = ctx.message.content.split("$cnew ",1)[1]
    if update_cuvinte_bruhman(cuvinte_noi) == 1:
      await ctx.message.channel.send("Deja exista acest raspuns!")
    else:
      await ctx.message.channel.send("Ai adaugat un raspuns nou!")
  else:
    await ctx.message.channel.send("N ai acces johnule")
# ADD NEW WORD TO DATABASE

# REMOVE WORD FROM DATABASE
@bot.command()
async def cdel(ctx):
  if "access" in [y.name.lower() for y in ctx.message.author.roles]:
    if "cuvinte_bruhman" in db.keys():
      i=0
      for words in db["cuvinte_bruhman"]:
        if ctx.message.content.split("$cdel ",1)[1] == words:
          break
        i=i+1
      if i == len(db["cuvinte_bruhman"]):
        await ctx.message.channel.send("Nu exista acest cuvant!")
      else:
        await ctx.message.channel.send("Cuvantul a fost sters!")
        del db["cuvinte_bruhman"][i]
    else:
      await ctx.message.channel.send("N ai acces johnule")
# REMOVE WORD FROM DATABASE

# BRUHMAN VC TROLL
vcok = 0
@bot.command()
async def browvc(ctx,arg1):
  global vcok
  if arg1 == "enable":
    if "access" in [y.name.lower() for y in ctx.message.author.roles]:
      try:
        await ctx.message.channel.send("Hehe boai vc activat :)))")
        vcok = 1
        vctask.start()
      except:
        print('Browman nu e in vc')
    else:
      await ctx.message.channel.send("ce fraier :))))")
  elif arg1 == "disable":
    if "access" in [y.name.lower() for y in ctx.message.author.roles]:
      try:
        await ctx.message.channel.send("Vc dezactivat, cata tristete :(((")
        vcok = 0
        vctask.stop()
      except:
        print('Task stop error...')
    else:
      await ctx.message.channel.send("ce fraier :))))")
# BRUHMAN VC TROLL
      
# ON MESSAGE
@bot.event
async def on_message(message):
  await bot.process_commands(message)
  
  if message.author == bot.user:
    return
  
  # variabilele globale
  global troll
  # variabilele globale
    
  # BRUHMAN TROLL
  if troll == 1:
    if message.author.id == 459401996890275860:
      await message.reply(random.choice(bruh))
  # BRUHMAN TROLL

  # focsani related
  if message.content == "focsani":
    await message.reply("e cringe + ratio + esti adoptat + arunca-te pe geam + ratie de mancare + john cena pam pampampammmm")
  # focsani related
  
  # RANDOM RESPONSE CHOICE
  if any(word in message.content for word in db["cuvinte_bruhman"]):
    await message.channel.send(random.choice(db["cuvinte"]))
  # RANDOM RESPONSE CHOICE
    
# ON MESSAGE
@tasks.loop(seconds=1)
async def mytask():
  try:
    #459401996890275860 - bruhman's ID
    Task_ping_time = random.randint(60,3600)
    
    # using one thread at a time
    await asyncio.sleep(Task_ping_time)
    channel = bot.get_channel(int(ID))
    await channel.send("<@"+str(459401996890275860)+"> "+str(random.choice(db["cuvinte"])))
    print(Task_ping_time)
  except:
    print('Channel not found')

@tasks.loop(seconds=1)
async def vctask():
  try:
    Task_vc_time = random.randint(10,60)
    # using one thread at a time
    await asyncio.sleep(Task_vc_time)
    if vcok == 1:
      guild = bot.get_guild(937988484789051422)
      member = await guild.fetch_member(459401996890275860)
      await member.move_to(None)
    else:
      print("Browvc already disabled")
  except:
    print('Not in voicechat')

# TOKEN
my_secret = os.environ['env']
bot.run(my_secret)
# TOKEN