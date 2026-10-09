import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'성공적으로 로그인했습니다! 봇 이름: {bot.user.name}')

@bot.command()
async def 안녕(ctx):
    await ctx.send(f'안녕하세요, {ctx.author.mention}님!')

# 맨 아래에 발급받은 디스코드 봇 토큰을 따옴표 안에 넣으세요
bot.run('MTU1ODA3ODA4NzA4NDkwMDQwNA.G6vZym.958zNeTgt78Ciod0g29Vj1Ibo1pDXjrOuabM44')
from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()
