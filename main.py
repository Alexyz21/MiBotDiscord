import asyncio
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Cargamos el token del archivo .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Configuramos los intents necesarios
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Inicializamos el bot con el prefijo !
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("-----------------------------------")
    print(f"¡Bot encendido con éxito!")
    print(f"Conectado como: {bot.user.name} (ID: {bot.user.id})")
    print("-----------------------------------")

# Función para cargar los módulos de la carpeta cogs
async def cargar_extensiones():
    if not os.path.exists("./cogs"):
        os.makedirs("./cogs")
        print("[AVISO] Se creó la carpeta 'cogs' automáticamente.")
        return

    for archivo in os.listdir("./cogs"):
        if archivo.endswith(".py"):
            nombre_cog = archivo[:-3]
            try:
                await bot.load_extension(f"cogs.{nombre_cog}")
                print(f"[✔] Módulo cargado con éxito: {nombre_cog}")
            except Exception as e:
                print(f"[✖] Error al cargar el módulo {nombre_cog}: {e}")

async def main():
    async with bot:
        await cargar_extensiones()
        if TOKEN:
            print("[INFO] Intentando conectar con Discord...")
            await bot.start(TOKEN)
        else:
            print("[ERROR CRÍTICO] No se encontró el DISCORD_TOKEN en el archivo .env")

if __name__ == "__main__":
    asyncio.run(main())