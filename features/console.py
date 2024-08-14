import discord
from discord.ext import commands

class console(commands.Cog):
    def __init__(self,bot:commands.Bot):
        self.bot = bot
        self.console = self.bot.get_channel(1272763038528704555)

    @commands.Cog.listener()
    async def on_message(self,message:discord.Message):
        if message.author == self.bot.user: return
        if not self.console: return
        if message.content.startswith('!gameinfo'):
                game_info = {}

                for member in message.guild.members:
                    if member.activity and isinstance(member.activity, discord.Game):
                        game_name = member.activity.name
                        if game_name in game_info:
                            game_info[game_name].append(member.mention)
                        else:
                            game_info[game_name] = [member.mention]

                
                embed = discord.Embed(title="ข้อมูลเกมในเซิร์ฟเวอร์", color=discord.Color.blue())

                for game, players in game_info.items():
                    embed.add_field(name=game, value=f"{len(players)} คน\n" + "\n".join(players), inline=False)

                if not game_info:
                    embed.add_field(name="ไม่มีผู้เล่น", value="ไม่มีสมาชิกที่กำลังเล่นเกมในขณะนี้", inline=False)

                await message.channel.send(embed=embed)

    