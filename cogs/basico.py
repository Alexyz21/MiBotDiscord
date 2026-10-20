import discord
from discord.ext import commands

class Basico(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Comando simple para saludar
    @commands.command(name="hola", help="Responde con un saludo.")
    async def hola(self, ctx):
        await ctx.send(f"¡Hola {ctx.author.mention}! El sistema de Akatsuki está en línea y operativo. ♕")

    # Comando de prueba de velocidad (Ping)
    @commands.command(name="ping", help="Muestra la latencia del bot.")
    async def ping(self, ctx):
        latencia = round(self.bot.latency * 1000)
        await ctx.send(f"🏓 ¡Pong! La latencia es de `{latencia}ms`.")

async def setup(bot):
    await bot.add_cog(Basico(bot))