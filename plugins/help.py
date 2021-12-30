from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
	alpha2 = InlineKeyboardMarkup([
		[InlineKeyboardButton("⚡ Channel ", url="https://t.me/HB4All")],
		[InlineKeyboardButton("Report Bugs 🚨", url="https://t.me/HB4All1_Bot")]
                ])

	help_image = "https://telegra.ph/file/21170a66aa4733a9a4c26.jpg"
	await message.reply_photo(help_image,  caption="**💡 HELP 📃...**\n \n__• Just Send your Youtube video url 🌟__ \n__• And i will give Method list to select your choice 😋__\n,reply_markup=alpha2)
