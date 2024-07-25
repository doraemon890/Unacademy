import os
import random
from pyrogram import filters
from pyrogram.types import CallbackQuery
from Ava import app
from Ava.core import script
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
            document_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
            if document_files:
                await app.send_message(
                    chat_id,
                    f"These are the materials for the category: {category.replace('_', ' ').title()}",
                    reply_markup=home_buttons
                )
                for doc in document_files:
                    try:
                        with open(os.path.join(folder_path, doc), "rb") as file:
                            await app.send_document(chat_id, file)
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
    photo = random.choice(script.IMG)  # Select a random photo from the list
    caption = script.START_TXT.format(message.from_user.mention)  # Format the caption
    await message.reply_photo(
        photo=photo,
        caption=caption,
        reply_markup=home_buttons
    )

@app.on_callback_query()
async def handle_callback(_, query: CallbackQuery):
    callback_data = query.data
    new_text = ""
    new_markup = None
    
    # Determine the new text and markup based on callback_data
    if callback_data.startswith("home_"):
        new_text = script.START_TXT
        new_markup = home_buttons
    if callback_data.startswith("support_"):
        new_text = script.SUPPORT_TXT 
        new_markup = support_buttons
    if callback_data.startswith("support_"):
        new_text = script.FORCE_MSG 
        new_markup = force_buttons
    elif callback_data.startswith("modes_"):
        new_text = script.MODES_TXT 
        new_markup = modes_buttons
    elif callback_data.startswith("notes_"):
        new_text = "Choose a notes category."
        new_markup = notes_buttons
    elif callback_data.startswith("elps_"):
        new_text = "Choose an ELPS category."
        new_markup = elps_buttons
    elif callback_data.startswith("modules_"):
        if callback_data == "modules_3_1_":
            new_text = "Choose a version 3.1 module."
            new_markup = module_buttons_3_1
        elif callback_data == "modules_4_0_":
            new_text = "Choose a version 4.0 module."
            new_markup = module_buttons_4_0
        else:
            new_text = "Choose a module category."
            new_markup = module_buttons
    elif callback_data.startswith("query_"):
        new_text = "Choose a query category."
        new_markup = query_buttons
    elif callback_data.startswith("test_series_"):
        new_text = "Choose a test series."
        new_markup = test_series_buttons
    elif callback_data.startswith("premium_"):
        if callback_data == "premium_material_seep_mam_":
            new_text = "Choose a SEEP MAM premium material."
            new_markup = premium_buttons_seep_mam
        elif callback_data == "premium_material_akansha_mam_":
            new_text = "Choose an AKANSHA MAM premium material."
            new_markup = premium_buttons_akansha_mam
        else:
            new_text = "Choose a premium material."
            new_markup = premium_buttons
    elif callback_data.startswith("supersix_"):
        if callback_data == "super_six_prateek_sir_":
            new_text = "Choose a PRATEEK SIR Super Six material."
            new_markup = supersix_buttons_prateek_sir
        elif callback_data == "super_six_akm_sir_":
            new_text = "Choose an AKM SIR Super Six material."
            new_markup = supersix_buttons_akm_sir
        elif callback_data == "super_six_skc_sir_":
            new_text = "Choose an SKC SIR Super Six material."
            new_markup = supersix_buttons_skc_sir
        elif callback_data == "super_six_rs_sir_":
            new_text = "Choose an RS SIR Super Six material."
            new_markup = supersix_buttons_rs_sir
        else:
            new_text = "Choose a Super Six category."
            new_markup = supersix_buttons
    else:
        category = CATEGORY_MAPPING.get(callback_data, None)
        if category:
            await send_documents(app, query.message.chat.id, category)
            return  # Skip message edit if sending documents
        new_text = "Invalid selection. Please try again."
        new_markup = home_buttons
    
    # Edit the message if there's new text or markup
    if new_text and (query.message.text != new_text or query.message.reply_markup != new_markup):
        await query.message.edit_text(new_text, reply_markup=new_markup)
