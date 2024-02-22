from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import uuid

TOKEN = "7009538858:AAGUTQCy9h7nwe91KQj_OSdBx3pEw_-X_gI"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("مرحبًا! قم بإرسال أي نص لوضعه في ملف بايثون.")

def save_text_to_file(update: Update, context: CallbackContext) -> None:
    # إذا كان النص غير فارغ
    if update.message.text:
        # إنشاء اسم فريد للملف باستخدام وحدة uuid
        file_name = str(uuid.uuid4()) + ".py"
        
        # حفظ النص في الملف
        with open(file_name, "w") as file:
            file.write(update.message.text)
        
        # إرسال الملف مباشرة
        update.message.reply_document(document=open(file_name, "rb"))
        
    else:
        update.message.reply_text("الرجاء إرسال نص قبل تنفيذ الأمر.")

def main() -> None:
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, save_text_to_file))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()