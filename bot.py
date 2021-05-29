import discord
from discord.ext import commands
import random, math
client = commands.Bot(command_prefix="=")

@client.event
async def on_ready():
    print("Yup, I am ready Senpai")
@client.command(aliases=['hi','Hello','HELLO','HI','Hi'])
async def hello(ctx):
    greetings = ["Hi", "Hello","Kon'nichiwa","Ha bol","BF ke saath busy hu, baad me aa"]
    selectedGreet =random.choice(greetings)
    await ctx.send(selectedGreet)

@client.command(aliases=['goodbye',"Bye","BYE",'Goodbye', 'Good morning'])
async def bye(ctx):
    byemsgs=["Chala ja bhosadike", "Pehli fursat me nikal"]
    await ctx.send(random.choice(byemsgs))

@client.command(aliases=["gn","GN"])
async def goodnight(ctx):
    gnmsgs=["Good night Hiran, Dreams, cause you already sweet!!", "Ja mar ja saale", "Tussi ja rahe ho?, Tussi na jaao", "I wish you won't wakeup", "Tussi ja rahe ho , toh ja na bc , roka kisne hai"]
    await ctx.send(random.choice(gnmsgs))

@client.command()
async def rndm(ctx,*,number):
    l=len(number)
    num=int(number)
    randnum = random.randint(0,10**(l))
    if randnum > num:
        msg="My number is "+ str(randnum)+", you said " + str(num) + " LoLa, YOU LOOSE :stuck_out_tongue:"
    elif randnum< num:
        msg="My number is "+ str(randnum)+ ", you said "+ str(num) +", Zyada khush na ho, next time hara dungi :smirk:"
    else:
        msg="OMG :heart_eyes: neuron sync "+" I LOVE YOU baby, marry me :kissing_heart:"
    await ctx.send(msg)

@client.command(aliases=['ILOVEYOU', 'Iloveyou','ily','iloveyou'])
async def ILY(ctx):
    proposeReply= ['I love ME too! :smiling_face_with_3_hearts:','Awww, but my hatred for you is even more truthful than this','*takes out pepper spray*','I love you too, but as a FRIEND','I have a boyfriend', "Already? Damn, I'm good!",'Ugh, here we go again!']
    await ctx.send(random.choice(proposeReply))

@client.command()
async def whobf(ctx):
    await ctx.send(random.choice(['Vishal','Doku-shin','Zeheral','Snek']))

@client.command()
async def hbd(ctx,*,person):
    await ctx.send("Happy Birthday " + person +'. :birthday::birthday::birthday::partying_face::partying_face:')

client.run("")