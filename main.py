import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix= "$", intents=intents)

@bot.event
async def on_ready():
    print(f"bot conectdo como {bot.user}")

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir("images"))
    with open(f"images/{img_name}", "rb") as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def animales(ctx):
    folder_path = "images/animales"
    
    if not os.path.exists(folder_path):
        await ctx.send("¡La categoría 'animales' no existe!")
        return
    
    imagenes = os.listdir(folder_path)
    if not imagenes:
        await ctx.send("No hay imágenes en la categoría 'animales'.")
        return

    img_name = random.choice(imagenes)
    with open(f"{folder_path}/{img_name}", "rb") as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

bot.run("TOKEN")
