import discord
from discord.ext import commands
import datetime

class logger(commands.Cog):
    def __init__(self,bot:commands.Bot):
        self.bot = bot
        self.logger = self.bot.get_channel(1272762949936746496)
    
    @commands.Cog.listener()
    async def on_message(self,message:discord.Message):
        if message.author == self.bot.user: return

    #function embed
    async def console_log(self,embedtype,title,desc:None,before:discord.Message=None,after:discord.Message=None):
        """ctx: used for author content
        embedtype: to check type of embed and return specific color
        before and after is message
        """

        def check_embedtype(type):
            match type:
                case "on_message_edit":
                    return discord.Color.yellow()
                case "on_message_delete":
                    return discord.Color.red()
                
                case _:
                    return discord.Color.default()
        
        chk_ = check_embedtype(embedtype)
        
        embed = discord.Embed(
            color=chk_,
            title=title,
            description=desc,
            timestamp=datetime.datetime.now()
        )
        
        embed.add_field(
            name='ข้อความถูกแก้ไข',
            value=f"""
โดย: {before.author.name}
ที่: {before.channel.mention}
ข้อความเก่า: ```{before.content}```
ข้อความใหม่: ```{after.content}```
"""
        )
        default_icon = 'https://static-00.iconduck.com/assets.00/profile-default-icon-512x511-v4sw4m29.png'
        icon_null = before.author.avatar.url if before.author.avatar else default_icon
        embed.set_author(name=before.author.name,url=None,icon_url=icon_null)
        if embedtype is "on_message_delete":
            embed.add_field(
                f"""
โดย: {before.author.name}
ที่: {before.channel.mention}
ข้อความที่ถูกลบ: ```{before.content} ```
"""
            )
            
        return embed


    @commands.Cog.listener()
    async def on_message_edit(self, before:discord.Message, after:discord.Message):
        if before.content != after.content:
            content=await self.console_log(
                embedtype='on_message_edit',
                desc='สถานการข้อความถูกแก้ไข',
                before=before,
                after=after,
                title='คำเตือน: ข้อความถูกแก้ไข'
            )
            if content:
                sending_ = self.logger
                await sending_.send(embed=content)

    @commands.Cog.listenner()
    async def on_message_delete(self, message:discord.message):
        if message:
            content_del = await self.console_log(
                embedtype='on_message_delete',
                desc='สถานการข้อความถูกลบ',
                before=message,
                title='คำเตือน: ข้อความถูกลบ'
            )

            if content_del:
                send_content = self.logger
                await send_content.send(embed=content_del)


async def setup(bot):
    await bot.add_cog(logger(bot))