from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = 'Use Your Token'
YOUR_USER_ID = 123456789  # Replace this with your actual Telegram user ID

conversation_store = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the /start command."""
    await update.message.reply_text("Welcome! Your messages will be forwarded to the admin.")

async def receive_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles incoming text messages from users and forwards them to the admin."""
    user_id = update.message.from_user.id
    username = update.message.from_user.username or update.message.from_user.first_name
    message_text = update.message.text

    conversation_id = f"{user_id}"
    if conversation_id not in conversation_store:
        conversation_store[conversation_id] = {'user_id': user_id, 'username': username, 'messages': []}

    conversation_store[conversation_id]['messages'].append({'from_user': True, 'text': message_text})

    await context.bot.send_message(chat_id=YOUR_USER_ID, text=f"@{username}")
    forwarded_message = await context.bot.send_message(chat_id=YOUR_USER_ID, text=message_text)
    conversation_store[forwarded_message.message_id] = conversation_id

async def receive_sticker(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles incoming sticker messages from users and forwards them to the admin."""
    user_id = update.message.from_user.id
    username = update.message.from_user.username or update.message.from_user.first_name
    sticker = update.message.sticker

    conversation_id = f"{user_id}"
    if conversation_id not in conversation_store:
        conversation_store[conversation_id] = {'user_id': user_id, 'username': username, 'messages': []}

    conversation_store[conversation_id]['messages'].append({'from_user': True, 'sticker': sticker.file_id})

    await context.bot.send_message(chat_id=YOUR_USER_ID, text=f"@{username}")
    forwarded_message = await context.bot.send_sticker(chat_id=YOUR_USER_ID, sticker=sticker.file_id)
    conversation_store[forwarded_message.message_id] = conversation_id

async def receive_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles incoming photo messages from users and forwards them to the admin."""
    user_id = update.message.from_user.id
    username = update.message.from_user.username or update.message.from_user.first_name
    photo = update.message.photo[-1].file_id

    conversation_id = f"{user_id}"
    if conversation_id not in conversation_store:
        conversation_store[conversation_id] = {'user_id': user_id, 'username': username, 'messages': []}

    conversation_store[conversation_id]['messages'].append({'from_user': True, 'photo': photo})

    await context.bot.send_message(chat_id=YOUR_USER_ID, text=f"@{username}")
    forwarded_message = await context.bot.send_photo(chat_id=YOUR_USER_ID, photo=photo)
    conversation_store[forwarded_message.message_id] = conversation_id

async def receive_audio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles incoming audio messages from users and forwards them to the admin."""
    user_id = update.message.from_user.id
    username = update.message.from_user.username or update.message.from_user.first_name
    audio = update.message.audio.file_id

    conversation_id = f"{user_id}"
    if conversation_id not in conversation_store:
        conversation_store[conversation_id] = {'user_id': user_id, 'username': username, 'messages': []}

    conversation_store[conversation_id]['messages'].append({'from_user': True, 'audio': audio})

    await context.bot.send_message(chat_id=YOUR_USER_ID, text=f"@{username}")
    forwarded_message = await context.bot.send_audio(chat_id=YOUR_USER_ID, audio=audio)
    conversation_store[forwarded_message.message_id] = conversation_id

async def receive_voice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    username = update.message.from_user.username or update.message.from_user.first_name
    voice = update.message.voice.file_id

    conversation_id = f"{user_id}"
    if conversation_id not in conversation_store:
        conversation_store[conversation_id] = {'user_id': user_id, 'username': username, 'messages': []}

    conversation_store[conversation_id]['messages'].append({'from_user': True, 'voice': voice})

    await context.bot.send_message(chat_id=YOUR_USER_ID, text=f"@{username}")
    forwarded_message = await context.bot.send_voice(chat_id=YOUR_USER_ID, voice=voice)
    conversation_store[forwarded_message.message_id] = conversation_id

async def receive_video(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    username = update.message.from_user.username or update.message.from_user.first_name
    video = update.message.video.file_id

    conversation_id = f"{user_id}"
    if conversation_id not in conversation_store:
        conversation_store[conversation_id] = {'user_id': user_id, 'username': username, 'messages': []}

    conversation_store[conversation_id]['messages'].append({'from_user': True, 'video': video})

    await context.bot.send_message(chat_id=YOUR_USER_ID, text=f"@{username}")
    forwarded_message = await context.bot.send_video(chat_id=YOUR_USER_ID, video=video)
    conversation_store[forwarded_message.message_id] = conversation_id

async def receive_video_note(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    username = update.message.from_user.username or update.message.from_user.first_name
    video_note = update.message.video_note.file_id

    conversation_id = f"{user_id}"
    if conversation_id not in conversation_store:
        conversation_store[conversation_id] = {'user_id': user_id, 'username': username, 'messages': []}
    
    conversation_store[conversation_id]['messages'].append({'from_user': True, 'video_note': video_note})

    await context.bot.send_message(chat_id=YOUR_USER_ID, text=f"@{username}")
    forwarded_message = await context.bot.send_video_note(chat_id=YOUR_USER_ID, video_note=video_note)
    conversation_store[forwarded_message.message_id] = conversation_id

async def receive_gif(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    username = update.message.from_user.username or update.message.from_user.first_name
    gif = update.message.animation.file_id  # Telegram treats GIFs as animations

    conversation_id = f"{user_id}"
    if conversation_id not in conversation_store:
        conversation_store[conversation_id] = {'user_id': user_id, 'username': username, 'messages': []}

    conversation_store[conversation_id]['messages'].append({'from_user': True, 'gif': gif})

    await context.bot.send_message(chat_id=YOUR_USER_ID, text=f"@{username}")
    forwarded_message = await context.bot.send_animation(chat_id=YOUR_USER_ID, animation=gif)
    conversation_store[forwarded_message.message_id] = conversation_id

async def receive_file(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    username = update.message.from_user.username or update.message.from_user.first_name
    file = update.message.document.file_id  # Extract the file ID
    file_name = update.message.document.file_name  # Extract file name

    conversation_id = f"{user_id}"
    if conversation_id not in conversation_store:
        conversation_store[conversation_id] = {'user_id': user_id, 'username': username, 'messages': []}
 
    conversation_store[conversation_id]['messages'].append({'from_user': True, 'file': file, 'file_name': file_name})

    await context.bot.send_message(chat_id=YOUR_USER_ID, text=f"@{username}")
    forwarded_message = await context.bot.send_document(chat_id=YOUR_USER_ID, document=file)
    conversation_store[forwarded_message.message_id] = conversation_id


async def handle_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles replies from both admin and users for text, stickers, photos, and audio."""
    if update.message.reply_to_message:
        original_message_id = update.message.reply_to_message.message_id

        if original_message_id in conversation_store:
            conversation_id = conversation_store[original_message_id]
            conversation = conversation_store[conversation_id]
            user_id = conversation['user_id']
            username = conversation['username']

            if update.message.chat_id == YOUR_USER_ID:  # Admin replying
                if update.message.text:
                    response_text = update.message.text
                    conversation['messages'].append({'from_user': False, 'text': response_text})
                    reply_message = await context.bot.send_message(chat_id=user_id, text=response_text)
                elif update.message.sticker:
                    sticker = update.message.sticker
                    conversation['messages'].append({'from_user': False, 'sticker': sticker.file_id})
                    reply_message = await context.bot.send_sticker(chat_id=user_id, sticker=sticker.file_id)
                elif update.message.photo:
                    photo = update.message.photo[-1].file_id
                    conversation['messages'].append({'from_user': False, 'photo': photo})
                    reply_message = await context.bot.send_photo(chat_id=user_id, photo=photo)
                elif update.message.audio:
                    audio = update.message.audio.file_id
                    conversation['messages'].append({'from_user': False, 'audio': audio})
                    reply_message = await context.bot.send_audio(chat_id=user_id, audio=audio)
                elif update.message.voice:
                    voice = update.message.voice.file_id
                    conversation['messages'].append({'from_user': False, 'voice': voice})
                    reply_message = await context.bot.send_voice(chat_id=user_id, voice=voice)
                elif update.message.video:
                    video = update.message.video.file_id
                    conversation['messages'].append({'from_user': False, 'video': video})
                    reply_message = await context.bot.send_video(chat_id=user_id, video=video)
                elif update.message.video_note:
                    video_note = update.message.video_note.file_id
                    conversation['messages'].append({'from_user': False, 'video_note': video_note})
                    reply_message = await context.bot.send_video_note(chat_id=user_id, video_note=video_note)
                elif update.message.animation:
                    gif = update.message.animation.file_id
                    conversation['messages'].append({'from_user': False, 'gif': gif})
                    reply_message = await context.bot.send_animation(chat_id=user_id, animation=gif)
                elif update.message.document:
                    file = update.message.document.file_id
                    file_name = update.message.document.file_name
                    conversation['messages'].append({'from_user': False, 'file': file, 'file_name': file_name})
                    reply_message = await context.bot.send_document(chat_id=user_id, document=file)

                conversation_store[reply_message.message_id] = conversation_id

            elif update.message.chat_id == user_id:  # User replying to the admin
                if update.message.text:
                    message_text = update.message.text
                    conversation['messages'].append({'from_user': True, 'text': message_text})
                    await context.bot.send_message(chat_id=YOUR_USER_ID, text=f"@{username} replied")
                    forwarded_message = await context.bot.send_message(chat_id=YOUR_USER_ID, text=message_text)
                elif update.message.sticker:
                    sticker = update.message.sticker
                    conversation['messages'].append({'from_user': True, 'sticker': sticker.file_id})
                    await context.bot.send_message(chat_id=YOUR_USER_ID, text=f"@{username} replied")
                    forwarded_message = await context.bot.send_sticker(chat_id=YOUR_USER_ID, sticker=sticker.file_id)
                elif update.message.photo:
                    photo = update.message.photo[-1].file_id
                    conversation['messages'].append({'from_user': True, 'photo': photo})
                    await context.bot.send_message(chat_id=YOUR_USER_ID, text=f"@{username} replied")
                    forwarded_message = await context.bot.send_photo(chat_id=YOUR_USER_ID, photo=photo)
                elif update.message.audio:
                    audio = update.message.audio.file_id
                    conversation['messages'].append({'from_user': True, 'audio': audio})
                    await context.bot.send_message(chat_id=YOUR_USER_ID, text=f"@{username} replied")
                    forwarded_message = await context.bot.send_audio(chat_id=YOUR_USER_ID, audio=audio)
                elif update.message.voice:
                    voice = update.message.voice.file_id
                    conversation['messages'].append({'from_user': True, 'voice': voice})
                    await context.bot.send_message(chat_id=YOUR_USER_ID, text=f"@{username} replied")
                    forwarded_message = await context.bot.send_voice(chat_id=YOUR_USER_ID, voice=voice)
                elif update.message.video:
                    video = update.message.video.file_id
                    conversation['messages'].append({'from_user': True, 'video': video})
                    await context.bot.send_message(chat_id=YOUR_USER_ID, text=f"@{username} replied")
                    forwarded_message = await context.bot.send_video(chat_id=YOUR_USER_ID, video=video)
                elif update.message.video_note:
                    video_note = update.message.video_note.file_id
                    conversation['messages'].append({'from_user': True, 'video_note': video_note})
                    await context.bot.send_message(chat_id=YOUR_USER_ID, text=f"@{username} replied")
                    forwarded_message = await context.bot.send_video_note(chat_id=YOUR_USER_ID, video_note=video_note)
                elif update.message.animation:
                    gif = update.message.animation.file_id
                    conversation['messages'].append({'from_user': True, 'gif': gif})
                    await context.bot.send_message(chat_id=YOUR_USER_ID, text=f"@{username} replied")
                    forwarded_message = await context.bot.send_animation(chat_id=YOUR_USER_ID, animation=gif)
                elif update.message.document:
                    file = update.message.document.file_id
                    file_name = update.message.document.file_name
                    conversation['messages'].append({'from_user': True, 'file': file, 'file_name': file_name})
                    await context.bot.send_message(chat_id=YOUR_USER_ID, text=f"@{username} replied")
                    forwarded_message = await context.bot.send_document(chat_id=YOUR_USER_ID, document=file)

                conversation_store[forwarded_message.message_id] = conversation_id
        else:
            await update.message.reply_text("Could not find the original conversation.")
    else:
        if update.message.text:
            await receive_message(update, context)
        elif update.message.sticker:
            await receive_sticker(update, context)
        elif update.message.photo:
            await receive_photo(update, context)
        elif update.message.audio:
            await receive_audio(update, context)
        elif update.message.voice:
            await receive_voice(update, context)
        elif update.message.video:
            await receive_video(update, context)
        elif update.message.video_note:
            await receive_video_note(update, context)
        elif update.message.animation:
            await receive_gif(update, context)
        elif update.message.document:
            await receive_file(update, context)

def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.ALL, handle_reply))

    application.run_polling()

if __name__ == '__main__':
    main()

