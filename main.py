from discord import Client, Message

bot = Client()


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")


@bot.event
async def on_message_edit(old_message: Message, new_message: Message):
    if new_message.author.id != 526620171658330112 or len(new_message.embeds) < 1:
        return
    elif not new_message.embeds[0].description:
        return

    dec = new_message.embeds[0].description.replace('**', '').replace('**', '').replace('>>>', '')
    if not dec.endswith("の仲間にしました！"):
        return

    if new_message.embeds[0].fields[3].value.replace('**', '').replace('**', '').replace('>>>', '').startswith(' SRレア'):
        return

    await new_message.channel.send("<@714455926970777602> SR以外")


bot.run('')
