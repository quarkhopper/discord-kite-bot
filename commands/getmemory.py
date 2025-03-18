# commands/getmemory.py
from discord.ext import commands
import discord
import kitestrings
from config_manager import check_command_channel, has_required_roles
import os

class GetMemory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        help="Retrieves the current Kite memory file for download.",
        brief="Download Kite’s current memory file."
    )
    @commands.check(check_command_channel)  # Enforce channel restriction globally
    @has_required_roles(sensitive=True)  # Requires "Vetted" + "Kite flyer"
    async def getmemory(self, ctx):
        """!getmemory
        
        **Detailed Description:**  
        This command allows you to **download Kite's current memory file**.

        **Usage:**  
        `!getmemory` → Retrieves the stored memory file.

        **Requirements:**  
        - **Server Mode Only**: This command only works in the **#kite** channel.  
        - **Roles Required**: "Vetted" and "Kite flyer".  

        **Arguments:**  
        - *(None)*
        """

        memory_path = kitestrings.export_memory()
        
        if not os.path.exists(memory_path) or os.path.getsize(memory_path) == 0:
            await ctx.send("🚫 No memory file found.")
            return
        
        await ctx.send(file=discord.File(memory_path, filename="kite_memory.kmem"))

async def setup(bot):
    """Registers this command with the bot."""
    await bot.add_cog(GetMemory(bot))
