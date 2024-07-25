import os
import random
from pyrogram import filters
from pyrogram.types import CallbackQuery
from Ava import app
from Ava.core import script
from Ava.core.Documents import DOCUMENT_PATHS
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
                    f"These are the materials for the category: {category.replace('_', ' ').title()}"
                )
                for doc in document_files:
                    try:
                        file_path = os.path.join(folder_path, doc)
                        with open(file_path, "rb") as file:
                            await app.send_document(chat_id, file, file_name=doc)
                    except Exception as e:
                        print(f"Failed to send document {doc}: {e}")
                        await app.send_message(chat_id, "Failed to send some documents.")
            else:
                await app.send_message(chat_id, "No documents found in this category.")
        else:
            await app.send_message(chat_id, "Category folder not found.")
    else:
        await app.send_message(chat_id, "Invalid category.")

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
    callback_data = query.data
    new_text, new_markup = await get_new_text_and_markup(callback_data)
    
    category = CATEGORY_MAPPING.get(callback_data)
    if category:
        await send_documents(app, query.message.chat.id, category)
        return
    
    if new_text and (query.message.text != new_text or query.message.reply_markup != new_markup):
        await query.message.edit_text(new_text, reply_markup=new_markup)

async def get_new_text_and_markup(callback_data):
    if callback_data.startswith("home_"):
        return script.START_TXT, home_buttons
    elif callback_data.startswith("support_"):
        return script.SUPPORT_TXT, support_buttons
    elif callback_data.startswith("force_"):
        return script.FORCE_MSG, force_buttons
    elif callback_data.startswith("modes_"):
        return script.MODES_TXT, modes_buttons
    elif callback_data.startswith("notes_"):
        return "Choose a notes category.", notes_buttons
    elif callback_data.startswith("elps_"):
        return "Choose an ELPS category.", elps_buttons
    elif callback_data.startswith("modules_"):
        return await get_module_buttons(callback_data)
    elif callback_data.startswith("query_"):
        return "Choose a query category.", query_buttons
    elif callback_data.startswith("test_series_"):
        return "Choose a test series.", test_series_buttons
    elif callback_data.startswith("premium_"):
        return await get_premium_buttons(callback_data)
    else:
        return "Invalid selection. Please try again.", home_buttons

async def get_module_buttons(callback_data):
    if callback_data == "modules_3_1_":
        return "Choose a version 3.1 module.", module_buttons_3_1
    elif callback_data == "modules_4_0_":
        return "Choose a version 4.0 module.", module_buttons_4_0
    else:
        return "Choose a module category.", module_buttons

async def get_premium_buttons(callback_data):
    if callback_data == "premium_material_seep_mam_":
        return "Choose a SEEP MAM premium material.", premium_buttons_seep_mam
    elif callback_data == "premium_material_akansha_mam_":
        return "Choose an AKANSHA MAM premium material.", premium_buttons_akansha_mam
    else:
        return "Choose a premium material.", premium_buttons
