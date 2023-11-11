from loader  import bot, dp
from asyncio import run

mtadmins = [
    1154989456
]

async def main():
    try:
        for mtadmin in mtadmins:
            await bot.send_message(mtadmin, "Bot is running")
        
        # await bot.set_my_commands()
        await dp.start_polling()
    
    except Exception as exc:
        print(f"{'-'*20}\n{exc}\n{'-'*20}")
    
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()

if __name__ == "__main__":
    run(main())