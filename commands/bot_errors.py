from discord.ext import commands

class BotErrors(commands.Cog):
    """Handles centralized error checks and messages for the bot."""

    def __init__(self, bot):
        self.bot = bot

    async def handle_error(self, ctx, error):
        """Handles errors globally and ensures messages are sent in #kite."""
        config = self.bot.get_cog("ConfigManager")
        if not config:
            await ctx.send("❌ An error occurred, and configuration couldn't be loaded.")
            return

        kite_channel_name = config.get_channel_name()

        # Find the #kite channel
        for channel in ctx.guild.text_channels:
            if channel.name == kite_channel_name:
                await channel.send(f"❌ An error occurred while executing `{ctx.command}`:\n```\n{error}\n```")
                return

        # Fallback if #kite channel is not found
        await ctx.send(f"❌ Error occurred: `{error}` (could not locate #{kite_channel_name})")

# ✅ Properly register the Cog with the bot
async def setup(bot):
    """Required setup function for loading the cog."""
    await bot.add_cog(BotErrors(bot))  # ✅ Pass bot instance to the Cog
