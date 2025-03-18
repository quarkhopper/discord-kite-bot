import asyncio
import discord
import os
import logging
from discord.ext import commands
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("discord")

# Discord bot setup with required intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Recursive function to load all commands (cogs) from the commands directory
async def load_cogs():
    commands_dir = Path(__file__).parent / "commands"
    for cog_file in commands_dir.rglob("*.py"):
        if cog_file.name == "__init__.py":
            continue  # Skip __init__.py files

        # Convert file path to Python module path (e.g., commands.test_commands.test)
        module_path = ".".join(cog_file.relative_to(commands_dir.parent).with_suffix('').parts)
        try:
            await bot.load_extension(module_path)
            logger.info(f"✅ Loaded cog: {module_path}")
        except Exception as e:
            logger.error(f"❌ Failed to load cog {module_path}: {e}")

@bot.event
async def on_ready():
    logger.info(f"✅ Logged in as {bot.user}")
    logger.info(f"🛠 Registered commands: {[cmd.name for cmd in bot.commands]}")

# Main entry point
async def main():
    await load_cogs()  # Load all cogs recursively
    await bot.start(os.getenv("DISCORD_BOT_TOKEN"))

if __name__ == "__main__":
    asyncio.run(main())
