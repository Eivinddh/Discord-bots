from redbot.core import commands, checks
from random import randint
import random


class Echokalender(commands.Cog):
    """Bot til echo sin eksamenskalender"""

    @commands.command()
    @checks.admin_or_permissions(manage_guild=True)
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
            #winner_int = randint(0, len(members) - 1)
            winner = random.choice(members)
            await ctx.send(
                "Vinneren i dagens kalender er... *drum roll*... \n{0}".format(
                    winner.mention
                )
            )
