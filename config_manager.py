import discord
import json
import re
from discord.ext import commands
import logging

logger = logging.getLogger("discord")

class ConfigManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config_channel_id = None  # Will be set dynamically
        self.command_config = {}  # In-memory config storage
        self.kite_channel = "kite"  # Default if not found in JSON
        self.general_role = "Vetted"  # Default
        self.sensitive_role = "Kite flyer"  # Default

    @commands.Cog.listener()
    async def on_ready(self):
        """Finds #bot-config dynamically and prepares for polling on demand."""
        await self.find_config_channel()
        await self.fetch_latest_config()

    async def find_config_channel(self):
        """Searches for #bot-config across all guilds."""
        await self.bot.wait_until_ready()
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                if channel.name == "bot-config":
                    self.config_channel_id = channel.id
                    print(f"[ConfigManager] Found #bot-config in {guild.name} (ID: {channel.id})")
                    return
        
        print("[ConfigManager] Could not find #bot-config in any server.")

    async def fetch_latest_config(self):
        """Fetches the most recent config message from #bot-config and updates the in-memory configuration."""
        if not self.config_channel_id:
            print("[ConfigManager] No valid config channel found. Skipping config load.")
            return

        channel = self.bot.get_channel(self.config_channel_id)
        if not channel:
            print("[ConfigManager] Could not retrieve #bot-config channel by ID.")
            return

        async for message in channel.history(limit=1):
            content = message.content.strip()

            # If the content is wrapped in triple backticks, remove them
            if content.startswith("```json") and content.endswith("```"):
                content = content[7:-3].strip()  # Remove ```json (7 chars) and ``` (3 chars)
            elif content.startswith("```") and content.endswith("```"):
                content = content[3:-3].strip()  # Remove ``` and ```

            print(f"[ConfigManager] Processed JSON content:\n{repr(content)}")  # Debugging log

            if not content:
                print("[ConfigManager] Retrieved an empty message from #bot-config.")
                return

            try:
                new_config = json.loads(content)  # Try parsing first
                self.command_config = new_config  # Replace existing config

                # Extract kite settings from JSON
                kite_config = new_config.get("kite-config", {})
                self.kite_channel = kite_config.get("kite-channel", "kite")
                self.general_role = kite_config.get("general-role", "Vetted")
                self.sensitive_role = kite_config.get("sensitive-role", "Kite flyer")

                print(f"[ConfigManager] Kite commands restricted to #{self.kite_channel}")
                print(f"[ConfigManager] General role: {self.general_role}, Sensitive role: {self.sensitive_role}")

            except json.JSONDecodeError:
                print("[ConfigManager] Invalid JSON detected. Skipping config update.")

    def get_channel_name(self):
        """Returns the authorized channel name for Kite commands."""
        return self.kite_channel

    def get_general_role(self):
        """Returns the required role for all commands."""
        return self.general_role

    def get_sensitive_role(self):
        """Returns the additional role required for sensitive commands."""
        return self.sensitive_role

async def setup(bot):
    await bot.add_cog(ConfigManager(bot))

def check_command_channel(ctx):
    """Ensures that the command is executed only in the authorized channel."""
    config = ctx.bot.get_cog("ConfigManager")
    if not config:
        return False  # ConfigManager is missing, fail safe

    authorized_channel = config.get_channel_name()
    return ctx.channel.name == authorized_channel

def has_required_roles(sensitive=False):
    """Dynamically checks if the user has the required roles.
    
    If `sensitive=True`, it also checks for the sensitive role.
    """

    async def predicate(ctx):
        config = ctx.bot.get_cog("ConfigManager")
        if not config:
            return False  # Fail-safe if ConfigManager is missing

        general_role = config.get_general_role()
        sensitive_role = config.get_sensitive_role()

        # Check for general access role
        if not any(role.name == general_role for role in ctx.author.roles):
            logger.warning(f"🚫 {ctx.command} failed: User {ctx.author} lacks `{general_role}` role.")
            return False

        # If the command requires the sensitive role, check for it
        if sensitive and not any(role.name == sensitive_role for role in ctx.author.roles):
            logger.warning(f"🚫 {ctx.command} failed: User {ctx.author} lacks `{sensitive_role}` role.")
            return False

        return True

    return commands.check(predicate)
