import discord
from googletrans import Translator, LANGUAGES

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/ts'):
        args = message.content.split(' ')
        if len(args) < 4:
            await message.channel.send('Неверное количество аргументов. Используйте формат `/ts <язык_исходного_текста> <язык_перевода> <текст>`')
            return

        source_lang = args[1]
        dest_lang = args[2]
        text = ' '.join(args[3:])
        translator = Translator()

        if source_lang not in LANGUAGES.values():
            await message.channel.send('Не удалось распознать язык исходного текста')
            return
        if dest_lang not in LANGUAGES.values():
            await message.channel.send('Не удалось распознать язык перевода')
            return

        try:
            translated = translator.translate(text, src=source_lang, dest=dest_lang)
            await message.channel.send(f'Перевод с {translated.src} на {translated.dest}: {translated.text}')
        except:
            await message.channel.send('Ошибка при переводе текста')

    elif message.content.startswith('/unts'):
        args = message.content.split(' ')
        if len(args) < 3:
            await message.channel.send('Неверное количество аргументов. Используйте формат `/unts <язык_перевода> <текст>`')
            return

        dest_lang = args[1]
        text = ' '.join(args[2:])
        translator = Translator()

        if dest_lang not in LANGUAGES.values():
            await message.channel.send('Не удалось распознать язык перевода')
            return

        try:
            translated = translator.detect(text)
            translated_text = translator.translate(text, dest=dest_lang)
            await message.channel.send(f'Перевод с {translated.lang} на {dest_lang}: {translated_text.text}')
        except:
            await message.channel.send('Ошибка при переводе текста')


client.run('INPUTYTOKENHERE')



