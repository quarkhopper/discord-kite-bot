# commands/getbackup.py
from discord.ext import commands
import discord
import kitestrings

class GetBackup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def getbackup(self, ctx):
        backup_path = kitestrings.export_backup()
        if not backup_path.exists():
            await ctx.send("🚫 No backup memory file found.")
            return
        
        await ctx.send(file=discord.File(backup_path, filename="kite_memory.bak"))

async def setup(bot):
    await bot.add_cog(GetBackup(bot))
