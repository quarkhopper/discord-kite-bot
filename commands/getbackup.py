# commands/getbackup.py
from discord.ext import commands
import discord
import kitestrings
from config_manager import check_command_channel, has_required_roles
import os

class GetBackup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        help="Retrieves the last saved backup of Kite's memory file.",
        brief="Download the backup memory file."
    )
    @commands.check(check_command_channel)  # Enforce channel restriction globally
    @has_required_roles(sensitive=True)  # Requires "Vetted" + "Kite flyer"
    async def getbackup(self, ctx):
        """!getbackup
        
        **Detailed Description:**  
        This command allows you to **download the last backed-up memory file**.

        **Usage:**  
        `!getbackup` → Retrieves the most recent backup of Kite’s memory.

        **Requirements:**  
        - **Server Mode Only**: This command only works in the **#kite** channel.  
        - **Roles Required**: "Vetted" and "Kite flyer".  

        **Arguments:**  
        - *(None)*
        """

        backup_path = kitestrings.export_backup()
        if not os.path.exists(backup_path) or os.path.getsize(backup_path) == 0:
            await ctx.send("🚫 No backup memory file found.")
            return
        
        await ctx.send(file=discord.File(backup_path, filename="kite_memory.bak"))

async def setup(bot):
    """Registers this command with the bot."""
    await bot.add_cog(GetBackup(bot))
