# commands/getbackup.py
from discord.ext import commands
import discord
import kitestrings
from config_manager import check_command_channel, has_required_roles
import os

class GetBackup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.check(check_command_channel)  # Enforce channel restriction globally
    @has_required_roles(sensitive=True)  # Requires "Vetted" + "Kite flyer"
    async def getbackup(self, ctx):
        """!getbackup
        
        Retrieves the backup of Kite's memory file for download.
        If no backup exists, informs the user instead.
        
        Usage:
        `!getbackup` → Retrieves the last saved backup of Kite’s memory.
        
        - **Server Mode Only**: Requires the "Vetted" and "Kite flyer" roles.
        
        Arguments:
        - *(None)*: This command takes no arguments.
        """

        backup_path = kitestrings.export_backup()
        if not os.path.exists(backup_path) or os.path.getsize(backup_path) == 0:
            await ctx.send("🚫 No backup memory file found.")
            return
        
        await ctx.send(file=discord.File(backup_path, filename="kite_memory.bak"))

async def setup(bot):
    await bot.add_cog(GetBackup(bot))
