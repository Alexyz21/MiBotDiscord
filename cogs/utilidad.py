import discord
from discord.ext import commands
import aiohttp

class Utilidad(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="robaremoji", help="Robar un emoji de otro servidor y añadirlo al actual.")
    @commands.has_permissions(manage_emojis=True)
    async def robaremoji(self, ctx, emoji: discord.Emoji):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(emoji.url) as resp:
                    if resp.status != 200:
                        return await ctx.send(f"❌ Error al descargar (Código HTTP: {resp.status})")
                    data = await resp.read()

            nuevo_emoji = await ctx.guild.create_custom_emoji(name=emoji.name, image=data)
            await ctx.send(f"✅ ¡Emoji robado con éxito! Añadido como: {nuevo_emoji}")

        except discord.Forbidden:
            await ctx.send("❌ Error: No tengo permisos de *Gestionar Emojis* en este servidor.")
        except discord.HTTPException as e:
            await ctx.send(f"❌ Error de Discord al subir el emoji: {e}")

    @robaremoji.error
    async def robaremoji_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("⚠️ No tienes permisos de *Gestionar Emojis* para usar este comando.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("⚠️ Uso incorrecto. Debes escribir el comando y poner el emoji al lado (Ejemplo: `!robaremoji 🍕` o con el emoji de otro servidor).")
        else:
            await ctx.send(f"⚠️ Ocurrió un error inesperado: {error}")

async def setup(bot):
    await bot.add_cog(Utilidad(bot))