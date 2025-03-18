# commands/command_pattern.py
from discord.ext import commands
import kitestrings
from config_manager import check_command_channel, has_required_roles

class CommandPattern(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.check(check_command_channel)  # Enforce channel restriction globally
    @has_required_roles()  # Dynamically enforce "Vetted" role
    # @has_required_roles(sensitive=True)  # Uncomment for sensitive commands
    async def commandname(self, ctx, arg: str = None):
        """!commandname <arg>
        
        A brief, clear description of what this command does.
        
        Usage:
        `!commandname <arg>` → Example usage explanation.
        
        - **Server Mode Only**: Requires the "Vetted" role.
        
        Arguments:
        - **arg**: Description of the argument.
        """

        if not arg:
            await ctx.send("⚠️ Usage: `!commandname <arg>`")
            return

        try:
            # Command implementation goes here
            await ctx.send(f"✅ Command executed with argument: {arg}")
        except Exception as e:
            await ctx.send(f"❌ Error executing command: {e}")

async def setup(bot):
    await bot.add_cog(CommandPattern(bot))
