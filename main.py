import discord
from discord.ext import commands
import asyncio

async def run_bot(token):
    bot = commands.Bot(
        command_prefix="0000",
        self_bot=True,
        help_command=None
    )

    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user}")

    @bot.event
    async def on_message(message):
        return

    try:
        await bot.start(token, reconnect=True)
    except discord.errors.LoginFailure:
        print(f"Failed to login with token: {token}")

async def main():
    with open("tokens.txt", "r") as f:
        tokens = f.read().strip().split("\n")

    tasks = [asyncio.create_task(run_bot(token.strip())) for token in tokens]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
