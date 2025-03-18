import logging
from discord.ext import commands

logger = logging.getLogger("discord")

class BotErrors(commands.Cog):
    """Handles centralized error checks and messages for the bot."""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """Handles command errors, ensuring minimal spam in chat."""
        if isinstance(error, commands.CommandNotFound):
            # Silently ignore unknown commands (just log them)
            logger.warning(f"🚫 Unknown command attempted: {ctx.message.content}")
            return  

        if isinstance(error, commands.CheckFailure):
            # Log only in server logs (no chat message)
            logger.warning(f"🚫 {ctx.command} failed: User {ctx.author} lacks permission or used in wrong channel.")
            return  

        # Send real errors to the #kite channel if possible
        config = self.bot.get_cog("ConfigManager")
        if config:
            kite_channel_name = config.get_channel_name()
            for channel in ctx.guild.text_channels:
                if channel.name == kite_channel_name:
                    await channel.send(f"❌ An error occurred while executing `{ctx.command}`:\n```\n{error}\n```")
                    return

        # Fallback if #kite channel is not found
        logger.error(f"❌ Unhandled error in command {ctx.command}: {error}")

# ✅ Properly register the Cog with the bot
async def setup(bot):
    """Required setup function for loading the cog."""
    await bot.add_cog(BotErrors(bot))
