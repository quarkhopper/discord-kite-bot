import logging
from discord.ext import commands

logger = logging.getLogger("discord")

class BotErrors(commands.Cog):
    """Handles centralized error checks and messages for the bot."""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """Handles common command errors to suppress unnecessary stack traces."""
        if isinstance(error, commands.CheckFailure):
            # Log a simple one-line error instead of full traceback
            logger.warning(f"🚫 {ctx.command} failed: User {ctx.author} lacks permission or used in wrong channel.")
            return  # Stop further error propagation

        # Send error message to the correct channel if possible
        config = self.bot.get_cog("ConfigManager")
        if config:
            kite_channel_name = config.get_channel_name()
            for channel in ctx.guild.text_channels:
                if channel.name == kite_channel_name:
                    await channel.send(f"❌ An error occurred while executing `{ctx.command}`:\n```\n{error}\n```")
                    return

        # Fallback if #kite channel is not found
        await ctx.send(f"❌ Error occurred: `{error}`")

# ✅ Properly register the Cog with the bot
async def setup(bot):
    """Required setup function for loading the cog."""
    await bot.add_cog(BotErrors(bot))
