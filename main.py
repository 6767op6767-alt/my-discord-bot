import os
import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

# Flask 웹 서버 설정 (Render 포트 바인딩용)
app = Flask('')
@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()

# 디스코드 봇 설정
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'성공적으로 로그인했습니다! 봇 이름: {bot.user.name}')

@bot.command()
async def 안녕(ctx):
    await ctx.send(f'안녕하세요, {ctx.author.mention}님!')

# 디스코드 봇 실행
bot.run('MTU1ODA3ODA4NzA4NDkwMDQwNA.GBD9_H.2RoQZb2ylZQ7Ih0_aEkKHidg_pGGBA17aga9ag')
