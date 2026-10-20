import discord
from discord.ext import commands

class Bienvenida(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # -------------------------------------------------------------
        # PEGA AQUÍ LA ID DE TU CANAL 🦇┃𝑪𝑴𝑫
        # -------------------------------------------------------------
        ID_CANAL_BIENVENIDA = 1551475183125139569  # <--- Cambia esto por tu ID real
        
        canal = member.guild.get_channel(ID_CANAL_BIENVENIDA)

        if canal:
            # Descripción adaptada con tu nuevo diseño y la mención real del usuario
            descripcion = (
                f"Bienvenid@ a las filas, {member.mention}.\n"
                f"Has entrado al territorio de la <a:crown:1555495010877837382> **Port Mafia**.\n\n"
                f"<a:purplechain:1555493525263622254>  **Enlaces importantes:** <a:purplechain:1555493525263622254>\n"
                f"<a:purplebook:1555761052795281408> **Reglas:** No olvides leerlas antes de actuar en <#1551673284418863315>\n"
                f"<a:purplelightbulb:1555495047867400223> **Anuncios:** Recuerda siempre pasarte por  <#1555965155106619442>\n"
                f"<a:purpleworld:1555495134580183090> **Streamers:** No olvides apoyar a nuestros creadores de contenido <#1561911735600939091>\n"
                f"<a:76441crystalbox:1555961572709376021> **Sorteos:** Habrá botines exclusivos de vez en cuando, participa en <#1553519070954135613>\n."
            )

            embed = discord.Embed(
                title="<:emoji_13:1557904060265537546>  PORT MAFIA  <:emoji_13:1557904060265537546>",
                description=descripcion,
                color=9052370
            )

            # Miniatura con la foto de perfil real del usuario
            embed.set_thumbnail(url=member.display_avatar.url)
            
            # Pie de página
            embed.set_footer(text="Una vez bajo nuestra jurisdicción, no hay marcha atrás.")
            
            # Enviamos el embed al canal configurado
            await canal.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Bienvenida(bot))