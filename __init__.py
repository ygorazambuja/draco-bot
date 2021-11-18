import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from features.cat import getCatImage

from features.coin import convertDracoToBRL, getDolarCotationInBrl

PORT = int(os.environ.get("PORT", 5000))
TOKEN = "2060838246:AAG3VqXAq-SBLz_6MXARuY22dwyF8rWF-XA"


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"Hello {update.effective_user.first_name}")


def draco(update: Update, context: CallbackContext) -> None:
    draco_quantity = 1
    try:
        draco_quantity = int(update.message.text.split(" ")[1])
    except Exception:
        draco_quantity = 1

    dracoInBRL = convertDracoToBRL()
    dolarCotation = getDolarCotationInBrl()
    if draco_quantity > 1:
        update.message.reply_text(
            f"{int(draco_quantity)} Draco = {dracoInBRL * int(draco_quantity)} BRL"
            + f"\n1 Dolar = 1 R${dolarCotation}"
        )
    else:
        update.message.reply_text(f"{int(draco_quantity)} Draco = {dracoInBRL}")


def cat(update: Update, context: CallbackContext) -> None:
    catImage = getCatImage()
    update.message.reply_photo(catImage, "Meow!")
    pass


def main():
    updater = Updater(TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler("hello", hello))
    updater.dispatcher.add_handler(CommandHandler("draco", draco))
    updater.dispatcher.add_handler(CommandHandler("cat", cat))

    updater.start_webhook(
        listen="0.0.0.0",
        port=int(PORT),
        url_path=TOKEN,
        webhook_url=f"https://draco-but.herokuapp.com/{TOKEN}",
    )
    # updater.bot.set_webhook(f"https://draco-but.herokuapp.com/{TOKEN}")

    updater.idle()


if __name__ == "__main__":
    main()
