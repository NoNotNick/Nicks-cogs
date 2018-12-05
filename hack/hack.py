import discord
from discord.ext import commands
import asyncio
import random


class Hacking:
    """Hack your friendz"""

    def __init__(self, bot):
        self.bot = bot
        self.emails = [ 
            '@yahoo.com', '@gmail.com', '@outlook.com', '@protonmail.com', '@hotmail.com',
            '@memes.com', '@god.com', '@pornhub.com'
            ]
        self.password = [ 'mydogisgreat', 'bicisbig', 'thebestofthebest', 'hackerman',
            'this1ssecure', 'hackmedaddy', 'specialSnowflakeIsDaBest', 'i love you'
        ]

#feel free to edit this code 

    @commands.command()
    async def hack(self, user : discord.Member):
        """Hack your friends"""
        u = user.mention
        un = user.name
        emails = random.choice(self.emails)
        passwords = random.choice(self.password)
        msg = await self.bot.say("Hacking... {}".format(u))
        await asyncio.sleep(4)
        msg2 = await self.bot.edit_message(msg, "Grabbing login...")
        await asyncio.sleep(4)
        msg3 = await self.bot.edit_message(msg2, "Login... ``email: {}{}`` ``Passowrd: {}``".format(un, emails, passwords))
        await asyncio.sleep(3)
        msg4 = await self.bot.edit_message(msg3, "``finding address...``")
        await asyncio.sleep(3)
        msg5 = await self.bot.edit_message(msg4, "``Tracking PO box...``")
        await asyncio.sleep(3)
        msg6 = await self.bot.edit_message(msg5, "``Sending post cards...``")
        await asyncio.sleep(3)
        msg7 = await self.bot.edit_message(msg6, "``exploiting computer with zero days..``")
        await asyncio.sleep(3)
        msg8 = await self.bot.edit_message(msg7, "Done. Now they shouldnt mess with you any more...")

def setup(bot):
    bot.add_cog(Hacking(bot))

