from redbot.core import commands
import random


class Echokalender(commands.Cog):
    """Bot til echo sin eksamenskalender"""

    @commands.command()
    async def rigged(self, ctx):
        """ Rigged command"""
        await ctx.send(
            "En feil har oppstått. Grunnet lav tilgang på økonomiske ressurser"
            + " trenger vi hjelp til å ordne opp i feilen. Vi tar imot "
            + "*frivillige donasjoner* på **2188** på vipps."
        )

    @commands.command()
    async def kalender(self, ctx):
        """Random echo kalender!"""
        # Your code will go here
        if ctx.author.voice is None:
            await ctx.send(
                "Du må bli med i en voice channel for å kunne avgjøre "
                + "kalenderen!"
            )
        else:
            channel = ctx.author.voice.channel
            members = channel.members
            winner = random.choice(members)
            await ctx.send(
                "Vinneren i dagens kalender er... *drum roll*... \n{0}".format(
                    winner.mention
                )
            )
