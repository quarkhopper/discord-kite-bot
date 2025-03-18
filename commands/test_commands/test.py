from discord.ext import commands
import kitestrings  # Corrected absolute import

class TestCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx, *, args=None):
        if not args:
            await ctx.send("Please specify a test to run. Example: `!test ping`")
            return

        parts = args.split()
        test_name, *test_args = parts

        if test_name == "ping":
            result = kitestrings.ping()
            await ctx.send(result)

        elif test_name == "add":
            if len(test_args) != 2:
                await ctx.send("Usage: `!test add <int> <int>`")
                return
            try:
                a, b = int(test_args[0]), int(test_args[1])
                result = kitestrings.add_numbers(a, b)
                await ctx.send(f"Result: {result}")
            except ValueError:
                await ctx.send("Please provide two valid integers.")

        elif test_name == "echo":
            if not test_args:
                await ctx.send("Provide a message to echo. Example: `!test echo Hello`")
                return
            message = " ".join(test_args)
            result = kitestrings.echo(message=message)
            await ctx.send(result)

        else:
            await ctx.send("Unknown test command.")

async def setup(bot):
    await bot.add_cog(TestCommands(bot))
