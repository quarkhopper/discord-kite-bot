# commands/setmemory.py
from discord.ext import commands
import kitestrings

class SetMemory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setmemory(self, ctx):
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
