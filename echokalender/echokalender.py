from redbot.core import commands
from random import randint


class Echokalender(commands.Cog):
    """Bot til echo sin eksamenskalender"""

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
            winner_int = randint(0, len(members) - 1)
            await ctx.send(
                "Vinneren i dagens kalender er... *drum roll*... \n{0}".format(
                    members[winner_int]
                )
            )
