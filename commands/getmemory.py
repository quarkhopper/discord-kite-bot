# commands/getmemory.py
from discord.ext import commands
import discord
import kitestrings
from config_manager import check_command_channel, has_required_roles

class GetMemory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.check(check_command_channel)  # Enforce channel restriction globally
    @has_required_roles(sensitive=True)  # Dynamically enforce "Vetted" + "Kite flyer"
    async def getmemory(self, ctx):
        """Usage: !getmemory
        
        Retrieves the current Kite memory file for download.
        """

        memory_path = kitestrings.export_memory()
        if not memory_path.exists():
            await ctx.send("🚫 No memory file found.")
            return
        
        await ctx.send(file=discord.File(memory_path, filename="kite_memory.txt"))

async def setup(bot):
    await bot.add_cog(GetMemory(bot))
