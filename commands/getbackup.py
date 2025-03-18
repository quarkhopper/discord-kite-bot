# commands/getbackup.py
from discord.ext import commands
import discord
import kitestrings
from config_manager import check_command_channel, has_required_roles

class GetBackup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.check(check_command_channel)  # Enforce channel restriction globally
    @has_required_roles(sensitive=True)  # Requires "Vetted" + "Kite flyer"
    async def getbackup(self, ctx):
        """Usage: !getbackup
        
        Retrieves the backup of Kite's memory file for download.
        """

        backup_path = kitestrings.export_backup()
        if not backup_path.exists():
            await ctx.send("🚫 No backup memory file found.")
            return
        
        await ctx.send(file=discord.File(backup_path, filename="kite_memory.bak"))

async def setup(bot):
    await bot.add_cog(GetBackup(bot))
