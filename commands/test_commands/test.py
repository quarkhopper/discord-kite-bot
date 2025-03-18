from discord.ext import commands
import kitestrings

class TestCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        if not ctx.message.attachments:
            await ctx.send("Please attach a file to save.")
            return

        attachment = ctx.message.attachments[0]
        file_bytes = await attachment.read()

        try:
            kitestrings.process_and_save_attachment(file_bytes)
            await ctx.send("✅ Attachment processed and saved successfully.")
        except Exception as e:
            await ctx.send(f"❌ Error saving attachment: {e}")

async def setup(bot):
    await bot.add_cog(TestCommands(bot))
