# commands/command_pattern.py
from discord.ext import commands
import kitestrings
from config_manager import check_command_channel, has_required_roles

class CommandPattern(commands.Cog):
    """
    This file provides a standard template for defining commands.
    All commands should follow this pattern for consistency.
    
    **Help & Usage Standards:**
    - Each command must have `help="..."` (full description) and `brief="..."` (short summary).
    - `!help` should give a **complete description**, not just a placeholder like `!commandname (with args)`.
    - Commands should have:
      - **Usage section** explaining how to use the command.
      - **Requirements section** listing roles or channel restrictions.
      - **Arguments section** describing parameters (or noting if none are required).
    """

    @commands.command(
        help="A complete description of what this command does.",
        brief="A short summary for `!help` listing."
    )
    @commands.check(check_command_channel)  # Enforce channel restriction globally
    @has_required_roles(sensitive=False)  # General role required; use (sensitive=True) for protected commands
    async def commandname(self, ctx, arg: str = None):
        """!commandname <arg>
        
        **Detailed Description:**  
        Explain exactly what the command does. This should be **clear and informative**.  

        **Usage:**  
        `!commandname <arg>` → Example of how to use this command.

        **Requirements:**  
        - **Server Mode Only**: This command only works in the **#kite** channel.  
        - **Roles Required**: "Vetted" (and "Kite flyer" if sensitive).  

        **Arguments:**  
        - **arg** *(optional)*: Describe what this argument is used for.
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
    """Registers this command pattern cog."""
    await bot.add_cog(CommandPattern(bot))
