# commands/setmemory.py
from discord.ext import commands
import asyncio  
import kitestrings
from config_manager import check_command_channel, has_required_roles

class SetMemory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.check(check_command_channel)  # Enforce channel restriction globally
    @has_required_roles(sensitive=True)  # Dynamically enforce "Vetted" + "Kite flyer"
    async def setmemory(self, ctx):
        """Usage: !setmemory (with file attached)

        Overwrites Kite's current memory with the content of the uploaded file.
        Requires confirmation before overwriting.
        """

        if not ctx.message.attachments:
            await ctx.send("Usage: `!setmemory` (with file attached)")
            return

        await ctx.send(
            "⚠️ This will overwrite the current Kite memory. "
            "Reply with `yes` to confirm or anything else to cancel."
        )

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        try:
            reply = await self.bot.wait_for('message', check=check, timeout=30)
            if reply.content.lower() != "yes":
                await ctx.send("🚫 Operation cancelled.")
                return

            attachment = ctx.message.attachments[0]
            file_bytes = await attachment.read()
            kitestrings.set_memory(file_bytes)
            await ctx.send("✅ Memory successfully updated.")
        except Exception as e:
            await ctx.send(f"❌ Error: {e}")
        except asyncio.TimeoutError:
            await ctx.send("⏳ Confirmation timed out. Please try again.")

async def setup(bot):
    await bot.add_cog(SetMemory(bot))
