# commands/getmemory.py
from discord.ext import commands
import discord
import kitestrings

class GetMemory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def getmemory(self, ctx):
        memory_path = kitestrings.export_memory()
        if not memory_path.exists():
            await ctx.send("🚫 No memory file found.")
            return
        
        await ctx.send(file=discord.File(memory_path, filename="kite_memory.txt"))

async def setup(bot):
    await bot.add_cog(GetMemory(bot))
