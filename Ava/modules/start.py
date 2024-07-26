import os
import asyncio
import random
from pyrogram import filters
from pyrogram.types import CallbackQuery
from Ava import app
from Ava.core import script
from Ava.core.Documents import *
from Ava.modules.structure import *

# Define category mapping
CATEGORY_MAPPING = {
    "books_": "books",
    "notes_seep_mam_": "notes_seep_mam",
    "notes_akansha_mam_": "notes_akansha_mam",
    "notes_anupam_sir_": "notes_anupam_sir",
    "notes_skc_sir_": "notes_skc_sir",
    "handwritten_notes_": "handwritten_notes",
    "elps_physics_": "elps_physics",
    "elps_chemistry_": "elps_chemistry",
    "elps_biology_": "elps_biology",
    "modules_3_1_physics_": "modules_3_1_physics",
    "modules_3_1_chemistry_": "modules_3_1_chemistry",
    "modules_3_1_biology_": "modules_3_1_biology",
    "modules_4_0_physics_": "modules_4_0_physics",
    "modules_4_0_chemistry_": "modules_4_0_chemistry",
    "modules_4_0_biology_": "modules_4_0_biology",
    "modules_assertion_reason_": "modules_assertion_reason",
    "modules_qft_series_": "modules_qft_series",
    "modules_mindmaps_": "modules_mindmaps",
    "test_series_offline_": "test_series_offline",
    "test_series_plus_iconic_": "test_series_plus_iconic",
    "premium_material_prateek_sir_": "premium_material_prateek_sir",
    "premium_material_akm_sir_": "premium_material_akm_sir",
    "premium_material_seep_mam_npp_": "premium_material_seep_mam_npp",
    "premium_material_seep_mam_dpp_": "premium_material_seep_mam_dpp",
    "premium_material_seep_mam_formula_booklet_": "premium_material_seep_mam_formula_booklet",
    "premium_material_seep_mam_important_booklets_": "premium_material_seep_mam_important_booklets",
    "premium_material_akansha_mam_dpp_": "premium_material_akansha_mam_dpp",
    "premium_material_akansha_mam_mindmaps_": "premium_material_akansha_mam_mindmaps",
    "super_six_prateek_sir_class_": "super_six_prateek_sir_class",
    "super_six_prateek_sir_physicsalcoholics_points_": "super_six_prateek_sir_physicsalcoholics_points",
    "super_six_akm_sir_course_": "super_six_akm_sir_course",
    "super_six_akm_sir_pyq_series_": "super_six_akm_sir_pyq_series",
    "super_six_akm_sir_module_discussion_": "super_six_akm_sir_module_discussion",
    "super_six_skc_sir_course_": "super_six_skc_sir_course",
    "super_six_skc_sir_organic_mechanism_": "super_six_skc_sir_organic_mechanism",
    "super_six_skc_sir_dpp_": "super_six_skc_sir_dpp",
    "super_six_rs_sir_course_": "super_six_rs_sir_course",
    "super_six_rs_sir_dpp_": "super_six_rs_sir_dpp",
}

# Dictionary to keep track of user states
user_states = {}

async def send_documents(app, chat_id, category):
    if category in DOCUMENT_PATHS:
        folder_path = DOCUMENT_PATHS[category]
        if os.path.exists(folder_path):
            document_files = [
                f for f in os.listdir(folder_path) 
                if os.path.isfile(os.path.join(folder_path, f))
            ]
            if document_files:
                await app.send_message(
                    chat_id,
                    f"`ᴛʜᴇsᴇ ᴀʀᴇ ᴛʜᴇ ᴍᴀᴛᴇʀɪᴀʟs ғᴏʀ ᴛʜᴇ : {category.replace('_', ' ').title()}`"
                )
                for doc in document_files:
                    try:
                        file_path = os.path.join(folder_path, doc)
                        with open(file_path, "rb") as file:
                            sent_message = await app.send_document(chat_id, file, file_name=doc, caption=doc)
                            # Debug output to check the attributes of sent_message
                            print(f"Sent message attributes: {dir(sent_message)}")
                            if sent_message:
                                message_id = getattr(sent_message, 'message_id', None)
                                if message_id:
                                    asyncio.create_task(delete_message_after_delay(app, chat_id, message_id, 240))
                                else:
                                    print(f"Failed to get message_id for document: {doc}")
                    except Exception as e:
                        print(f"Failed to send document {doc}: {e}")
                        await app.send_message(chat_id, "Failed to send some documents.")
                
                # Send the notification message
                await app.send_message(
                    chat_id,
                    "📜 ᴘʟᴇᴀsᴇ ғᴏʀᴡᴀʀᴅ ᴛʜɪs ᴍᴀᴛᴇʀɪᴀʟ ᴛᴏ ᴀɴʏ ᴏᴛʜᴇʀ ᴄʜᴀᴛ ᴏʀ sᴀᴠᴇᴅ ᴍᴇssᴀɢᴇ ᴡɪᴛʜɪɴ 4 ᴍɪɴᴜᴛᴇs ᴀs ɪᴛ ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ ᴛᴏ ᴀᴠᴏɪᴅ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs."
                )
            else:
                await app.send_message(chat_id, "No documents found in this category.")
        else:
            await app.send_message(chat_id, "Category folder not found.")
    else:
        await app.send_message(chat_id, "Invalid category.")
    
    # Clear the user state after sending documents
    user_states[chat_id] = None

async def delete_message_after_delay(app, chat_id, message_id, delay):
    await asyncio.sleep(delay)
    try:
        await app.delete_messages(chat_id, message_id)
    except Exception as e:
        print(f"Failed to delete message {message_id}: {e}")

@app.on_message(filters.command("start"))
async def start(_, message):
    photo = random.choice(script.IMG)
    caption = script.START_TXT.format(message.from_user.mention)
    await message.reply_photo(
        photo=photo,
        caption=caption,
        reply_markup=home_buttons
    )

@app.on_callback_query()
async def handle_callback(_, query: CallbackQuery):
    chat_id = query.message.chat.id
    callback_data = query.data
    new_text, new_markup = await get_new_text_and_markup(query, callback_data)
    
    # Handle category requests
    category = CATEGORY_MAPPING.get(callback_data)
    if category:
        if user_states.get(chat_id):
            await app.send_message(chat_id, "ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜsᴇ ᴛᴡᴏ ᴏᴘᴛɪᴏɴs sɪᴍᴜʟᴛᴀɴᴇᴏᴜsʟʏ. ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴜɴᴛɪʟ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴏᴘᴇʀᴀᴛɪᴏɴ ɪs ғɪɴɪsʜᴇᴅ.")
            return
        
        user_states[chat_id] = category
        await send_documents(app, chat_id, category)
        return

    # Handle other callback types
    if new_text and (query.message.text != new_text or query.message.reply_markup != new_markup):
        await query.message.edit_text(new_text, reply_markup=new_markup)

async def get_new_text_and_markup(query: CallbackQuery, callback_data: str):
    if callback_data.startswith("home_"):
        return script.START_TXT.format(query.from_user.mention), home_buttons
    elif callback_data.startswith("support_"):
        return script.SUPPORT_TXT, support_buttons
    elif callback_data.startswith("force_"):
        return script.FORCE_MSG.format(query.from_user.mention), force_buttons
    elif callback_data.startswith("modes_"):
        return script.MODES_TXT, modes_buttons
    elif callback_data.startswith("notes_"):
        return "•➥ ᴄʜᴏᴏsᴇ ᴀ ɴᴏᴛᴇs ᴄᴀᴛᴇɢᴏʀʏ.", notes_buttons
    elif callback_data.startswith("elps_"):
        return "•➥ ᴄʜᴏᴏsᴇ ᴀɴ ᴇʟᴘs ᴄᴀᴛᴇɢᴏʀʏ.", elps_buttons
    elif callback_data.startswith("modules_"):
        return await get_module_buttons(callback_data)
    elif callback_data.startswith("query_"):
        return "•➥ ᴄʜᴏᴏsᴇ ᴀ ǫᴜᴇʀʏ ᴄᴀᴛᴇɢᴏʀʏ.", query_buttons
    elif callback_data.startswith("test_series_"):
        return "•➥ ᴄʜᴏᴏsᴇ ᴀ ᴛᴇsᴛ sᴇʀɪᴇs.", test_series_buttons
    elif callback_data.startswith("supersix_"):
        return "•➥ ᴄʜᴏᴏsᴇ ᴀ sᴜᴘᴇʀ sɪx ᴄᴀᴛᴇɢᴏʀʏ.", supersix_buttons
    elif callback_data.startswith("super_six_prateek_sir_"):
        return "•➥ ᴄʜᴏᴏsᴇ ᴀ ᴘʀᴀᴛᴇᴇᴋ sɪʀ sᴜᴘᴇʀ sɪx material.", supersix_buttons_prateek_sir
    elif callback_data.startswith("super_six_akm_sir_"):
        return "•➥ ᴄʜᴏᴏsᴇ ᴀɴ ᴀᴋᴍ sɪʀ sᴜᴘᴇʀ sɪx material.", supersix_buttons_akm_sir
    elif callback_data.startswith("super_six_skc_sir_"):
        return "•➥ ᴄʜᴏᴏsᴇ ᴀɴ sᴋᴄ sɪʀ sᴜᴘᴇʀ sɪx material.", supersix_buttons_skc_sir
    elif callback_data.startswith("super_six_rs_sir_"):
        return "•➥ ᴄʜᴏᴏsᴇ ᴀɴ ʀs sɪʀ sᴜᴘᴇʀ sɪx material.", supersix_buttons_rs_sir
    elif callback_data.startswith("premium_"):
        return await get_premium_buttons(callback_data)
    else:
        return "ɪɴᴠᴀʟɪᴅ sᴇʟᴇᴄᴛɪᴏɴ. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.📛", home_buttons

async def get_module_buttons(callback_data):
    if callback_data == "modules_3_1_":
        return "•➥ ᴄʜᴏᴏsᴇ ᴀ ᴠᴇʀsɪᴏɴ 3.1 ᴍᴏᴅᴜʟᴇ.", module_buttons_3_1
    elif callback_data == "modules_4_0_":
        return "•➥ ᴄʜᴏᴏsᴇ ᴀ ᴠᴇʀsɪᴏɴ 4.0 ᴍᴏᴅᴜʟᴇ.", module_buttons_4_0
    else:
        return "•➥ ᴄʜᴏᴏsᴇ ᴀ ᴍᴏᴅᴜʟᴇ ᴄᴀᴛᴇɢᴏʀʏ.", module_buttons

async def get_premium_buttons(callback_data):
    if callback_data == "premium_material_seep_mam_":
        return "•➥ ᴄʜᴏᴏsᴇ ᴀ sᴇᴇᴘ ᴍᴀᴍ ᴘʀᴇᴍɪᴜᴍ ᴍᴀᴛᴇʀɪᴀʟ.", premium_buttons_seep_mam
    elif callback_data == "premium_material_akansha_mam_":
        return "•➥ ᴄʜᴏᴏsᴇ ᴀɴ ᴀᴋᴀɴsʜᴀ ᴍᴀᴍ ᴘʀᴇᴍɪᴜᴍ ᴍᴀᴛᴇʀɪᴀʟ.", premium_buttons_akansha_mam
    else:
        return "•➥ ᴄʜᴏᴏsᴇ ᴀ ᴘʀᴇᴍɪᴜᴍ ᴍᴀᴛᴇʀɪᴀʟ.", premium_buttons
