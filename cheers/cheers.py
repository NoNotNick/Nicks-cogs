import discord
from discord.ext import commands
from random import randint
from random import choice

class Cheers:
    """Grab a glass and share it with your mates"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def cheers(self, ctx, user : discord.Member, number : int = 1000):
        """Grab your mugs!"""
        author = ctx.message.author
        if number > 1:
            n = randint(1, number)
            u = user.mention
            await self.bot.say("{} Woo-wee grab your mugs! Because You have {} Beers".format(author.mention, n))
            await self.bot.say("And you both grab your mugs and put them in there air before screaming CHEERS!. And you and {} downed every last drop. It was a good night".format(u))
        else:
            await self.bot.say("{} You broke all the bottles".format(author.mention))
       
# this is a really useless thing but hey i coded it so it is indeed special!

def setup(bot):
    bot.add_cog(Cheers(bot))

