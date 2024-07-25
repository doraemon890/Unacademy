import os
from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from Ava import app
from Ava.core import script
from Ava.core.func import subscribe, chk_user

# Define paths for each document category
DOCUMENT_PATHS = {
    "books": "Ava.core.Documents/books/",
    "notes_akansha_mam": "Ava.core.Documents/notes_akansha_mam/",
    "notes_anupam_sir": "Ava.core.Documents/notes_anupam_sir/",
    "notes_skc_sir": "Ava.core.Documents/notes_skc_sir/",
    "handwritten_notes": "Ava.core.Documents/handwritten_notes/",
    "elps_physics": "Ava.core.Documents/elps_physics/",
    "elps_chemistry": "Ava.core.Documents/elps_chemistry/",
    "elps_biology": "Ava.core.Documents/elps_biology/",
    "modules_3_1_physics": "Ava.core.Documents/modules_3_1_physics/",
    "modules_3_1_chemistry": "Ava.core.Documents/modules_3_1_chemistry/",
    "modules_3_1_biology": "Ava.core.Documents/modules_3_1_biology/",
    "modules_4_0_physics": "Ava.core.Documents/modules_4_0_physics/",
    "modules_4_0_chemistry": "Ava.core.Documents/modules_4_0_chemistry/",
    "modules_4_0_biology": "Ava.core.Documents/modules_4_0_biology/",
    "modules_assertion_reason": "Ava.core.Documents/modules_assertion_reason/",
    "modules_qft_series": "Ava.core.Documents/modules_qft_series/",
    "modules_mindmaps": "Ava.core.Documents/modules_mindmaps/",
    "test_series_offline": "Ava.core.Documents/test_series_offline/",
    "test_series_plus_iconic": "Ava.core.Documents/test_series_plus_iconic/",
    "premium_material_prateek_sir": "Ava.core.Documents/premium_material_prateek_sir/",
    "premium_material_akm_sir": "Ava.core.Documents/premium_material_akm_sir/",
    "premium_material_seep_mam_npp": "Ava.core.Documents/premium_material_seep_mam_npp/",
    "premium_material_seep_mam_dpp": "Ava.core.Documents/premium_material_seep_mam_dpp/",
    "premium_material_seep_mam_formula_booklet": "Ava.core.Documents/premium_material_seep_mam_formula_booklet/",
    "premium_material_seep_mam_important_booklets": "Ava.core.Documents/premium_material_seep_mam_important_booklets/",
    "premium_material_akansha_mam_dpp": "Ava.core.Documents/premium_material_akansha_mam_dpp/",
    "premium_material_akansha_mam_mindmaps": "Ava.core.Documents/premium_material_akansha_mam_mindmaps/",
    "super_six_prateek_sir_class": "Ava.core.Documents/super_six_prateek_sir_class/",
    "super_six_prateek_sir_physicsalcoholics_points": "Ava.core.Documents/super_six_prateek_sir_physicsalcoholics_points/",
    "super_six_akm_sir_course": "Ava.core.Documents/super_six_akm_sir_course/",
    "super_six_akm_sir_pyq_series": "Ava.core.Documents/super_six_akm_sir_pyq_series/",
    "super_six_akm_sir_module_discussion": "Ava.core.Documents/super_six_akm_sir_module_discussion/",
    "super_six_skc_sir_course": "Ava.core.Documents/super_six_skc_sir_course/",
    "super_six_skc_sir_organic_mechanism": "Ava.core.Documents/super_six_skc_sir_organic_mechanism/",
    "super_six_skc_sir_dpp": "Ava.core.Documents/super_six_skc_sir_dpp/",
    "super_six_rs_sir_course": "Ava.core.Documents/super_six_rs_sir_course/",
    "super_six_rs_sir_dpp": "Ava.core.Documents/super_six_rs_sir_dpp/"
}

# Button Definitions
home_buttons = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("Support", callback_data="support_"),
        InlineKeyboardButton("Unacademy Modules", callback_data="modes_")
    ],
    [
        InlineKeyboardButton("Get Free Access✅", callback_data="premium_")
    ]
])

modes_buttons = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("BOOKS", callback_data="books_"),
        InlineKeyboardButton("NOTES", callback_data="notes_")
    ],
    [
        InlineKeyboardButton("Modules", callback_data="modules_"),
        InlineKeyboardButton("Elps", callback_data="elps_")
    ],
    [
        InlineKeyboardButton("Queries", callback_data="query_")
    ],
    [
        InlineKeyboardButton("Super Six", callback_data="supersix_"),
        InlineKeyboardButton("Premium Materials", callback_data="premium_")
    ],
    [
        InlineKeyboardButton("Go Back ◀️", callback_data="home_")
    ]
])

notes_buttons = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("SEEP MAM", callback_data="notes_seep_mam_"),
        InlineKeyboardButton("AKANSHA MAM", callback_data="notes_akansha_mam_")
    ],
    [
        InlineKeyboardButton("ANUPAM SIR", callback_data="notes_anupam_sir_"),
        InlineKeyboardButton("SKC SIR", callback_data="notes_skc_sir_")
    ],
    [
        InlineKeyboardButton("HANDWRITTEN SHORT NOTES", callback_data="handwritten_notes_")
    ],
    [
        InlineKeyboardButton("Go Back ◀️", callback_data="modes_")
    ]
])

elps_buttons = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("PHYSICS", callback_data="elps_physics_"),
        InlineKeyboardButton("CHEMISTRY", callback_data="elps_chemistry_")
    ],
    [
        InlineKeyboardButton("BIOLOGY", callback_data="elps_biology_")
    ],
    [
        InlineKeyboardButton("Go Back ◀️", callback_data="modes_")
    ]
])

module_buttons = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("VERSION 3.1", callback_data="modules_3_1_"),
        InlineKeyboardButton("VERSION 4.0", callback_data="modules_4_0_")
    ],
    [
        InlineKeyboardButton("Go Back ◀️", callback_data="modes_")
    ]
])

module_buttons_3_1 = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("PHYSICS", callback_data="modules_3_1_physics_"),
        InlineKeyboardButton("CHEMISTRY", callback_data="modules_3_1_chemistry_")
    ],
    [
        InlineKeyboardButton("BIOLOGY", callback_data="modules_3_1_biology_")
    ],
    [
        InlineKeyboardButton("Go Back ◀️", callback_data="module_buttons_")
    ]
])

module_buttons_4_0 = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("PHYSICS", callback_data="modules_4_0_physics_"),
        InlineKeyboardButton("CHEMISTRY", callback_data="modules_4_0_chemistry_")
    ],
    [
        InlineKeyboardButton("BIOLOGY", callback_data="modules_4_0_biology_")
    ],
    [
        InlineKeyboardButton("Go Back ◀️", callback_data="module_buttons_")
    ]
])

query_buttons = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("ASSERTION REASON", callback_data="modules_assertion_reason_"),
        InlineKeyboardButton("QFT SERIES", callback_data="modules_qft_series_")
    ],
    [
        InlineKeyboardButton("MINDMAPS", callback_data="modules_mindmaps_"),
        InlineKeyboardButton("Test Series", callback_data="test_series_")
    ],
    [
        InlineKeyboardButton("Go Back ◀️", callback_data="modes_")
    ]
])

test_series_buttons = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("OFFLINE", callback_data="test_series_offline_"),
        InlineKeyboardButton("PLUS/ICONIC", callback_data="test_series_plus_iconic_")
    ],
    [
        InlineKeyboardButton("Go Back ◀️", callback_data="query_buttons_")
    ]
])

premium_buttons = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("SEEP MAM", callback_data="premium_material_seep_mam_"),
        InlineKeyboardButton("AKANSHA MAM", callback_data="premium_material_akansha_mam_")
    ],
    [
        InlineKeyboardButton("PRATEEK SIR", callback_data="premium_material_prateek_sir_"),
        InlineKeyboardButton("AKM SIR", callback_data="premium_material_akm_sir_")
    ],
    [
        InlineKeyboardButton("Go Back ◀️", callback_data="home_")
    ]
])

premium_buttons_seep_mam = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("NPP", callback_data="premium_material_seep_mam_npp_"),
        InlineKeyboardButton("DPP", callback_data="premium_material_seep_mam_dpp_")
    ],
    [
        InlineKeyboardButton("FORMULA BOOKLET", callback_data="premium_material_seep_mam_formula_booklet_"),
        InlineKeyboardButton("IMPORTANT BOOKLETS", callback_data="premium_material_seep_mam_important_booklets_")
    ],
    [
        InlineKeyboardButton("Go Back ◀️", callback_data="premium_buttons_")
    ]
])

premium_buttons_akansha_mam = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("DPP", callback_data="premium_material_akansha_mam_dpp_"),
        InlineKeyboardButton("MINDMAPS", callback_data="premium_material_akansha_mam_mindmaps_")
    ],
    [
        InlineKeyboardButton("Go Back ◀️", callback_data="premium_buttons_")
    ]
])

supersix_buttons = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("PRATEEK SIR", callback_data="super_six_prateek_sir_"),
        InlineKeyboardButton("AKM SIR", callback_data="super_six_akm_sir_")
    ],
    [
        InlineKeyboardButton("SKC SIR", callback_data="super_six_skc_sir_"),
        InlineKeyboardButton("RS SIR", callback_data="super_six_rs_sir_")
    ],
    [
        InlineKeyboardButton("Go Back ◀️", callback_data="home_")
    ]
])

supersix_buttons_prateek_sir = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("CLASS", callback_data="super_six_prateek_sir_class_"),
        InlineKeyboardButton("PHYSICSALCOHOLICS POINTS", callback_data="super_six_prateek_sir_physicsalcoholics_points_")
    ],
    [
        InlineKeyboardButton("Go Back ◀️", callback_data="supersix_")
    ]
])

supersix_buttons_akm_sir = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("COURSE", callback_data="super_six_akm_sir_course_"),
        InlineKeyboardButton("PYQ SERIES", callback_data="super_six_akm_sir_pyq_series_")
    ],
    [
        InlineKeyboardButton("MODULE DISCUSSION", callback_data="super_six_akm_sir_module_discussion_")
    ],
    [
        InlineKeyboardButton("Go Back ◀️", callback_data="supersix_")
    ]
])

supersix_buttons_skc_sir = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("COURSE", callback_data="super_six_skc_sir_course_"),
        InlineKeyboardButton("ORGANIC MECHANISM", callback_data="super_six_skc_sir_organic_mechanism_")
    ],
    [
        InlineKeyboardButton("DPP", callback_data="super_six_skc_sir_dpp_")
    ],
    [
        InlineKeyboardButton("Go Back ◀️", callback_data="supersix_")
    ]
])

supersix_buttons_rs_sir = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("COURSE", callback_data="super_six_rs_sir_course_"),
        InlineKeyboardButton("DPP", callback_data="super_six_rs_sir_dpp_")
    ],
    [
        InlineKeyboardButton("Go Back ◀️", callback_data="supersix_")
    ]
])

# Mapping of callback data to category paths
CATEGORY_MAPPING = {
    "books_": "books",
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
    "super_six_rs_sir_dpp_": "super_six_rs_sir_dpp"
}

async def send_documents(app, chat_id, category):
    if category in DOCUMENT_PATHS:
        folder_path = DOCUMENT_PATHS[category]
        if os.path.exists(folder_path):
            document_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
            if document_files:
                await app.send_message(
                    chat_id,
                    f"These Are the Materials For this Category: {category.replace('_', ' ').title()}",
                    reply_markup=home_buttons
                )
                for doc in document_files:
                    with open(os.path.join(folder_path, doc), "rb") as file:
                        await app.send_document(chat_id, file)
            else:
                await app.send_message(chat_id, "No documents found in this category.")
        else:
            await app.send_message(chat_id, "Category folder not found.")
    else:
        await app.send_message(chat_id, "Invalid category.")

@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply(
        "Welcome! Choose an option below.",
        reply_markup=home_buttons
    )

@app.on_callback_query()
async def handle_callback(_, query):
    callback_data = query.data
    if callback_data.startswith("home_"):
        await query.message.edit_text("Welcome! Choose an option below.", reply_markup=home_buttons)
    elif callback_data.startswith("modes_"):
        await query.message.edit_text("Choose a mode.", reply_markup=modes_buttons)
    elif callback_data.startswith("notes_"):
        await query.message.edit_text("Choose a notes category.", reply_markup=notes_buttons)
    elif callback_data.startswith("elps_"):
        await query.message.edit_text("Choose an ELPS category.", reply_markup=elps_buttons)
    elif callback_data.startswith("modules_"):
        if callback_data == "modules_3_1_":
            await query.message.edit_text("Choose a version 3.1 module.", reply_markup=module_buttons_3_1)
        elif callback_data == "modules_4_0_":
            await query.message.edit_text("Choose a version 4.0 module.", reply_markup=module_buttons_4_0)
        else:
            await query.message.edit_text("Choose a module.", reply_markup=module_buttons)
    elif callback_data.startswith("query_"):
        await query.message.edit_text("Choose a query category.", reply_markup=query_buttons)
    elif callback_data.startswith("test_series_"):
        await query.message.edit_text("Choose a test series.", reply_markup=test_series_buttons)
    elif callback_data.startswith("premium_"):
        if callback_data == "premium_material_seep_mam_":
            await query.message.edit_text("Choose a SEEP MAM premium material.", reply_markup=premium_buttons_seep_mam)
        elif callback_data == "premium_material_akansha_mam_":
            await query.message.edit_text("Choose an AKANSHA MAM premium material.", reply_markup=premium_buttons_akansha_mam)
        else:
            await query.message.edit_text("Choose a premium material.", reply_markup=premium_buttons)
    elif callback_data.startswith("supersix_"):
        if callback_data == "super_six_prateek_sir_":
            await query.message.edit_text("Choose a PRATEEK SIR Super Six material.", reply_markup=supersix_buttons_prateek_sir)
        elif callback_data == "super_six_akm_sir_":
            await query.message.edit_text("Choose an AKM SIR Super Six material.", reply_markup=supersix_buttons_akm_sir)
        elif callback_data == "super_six_skc_sir_":
            await query.message.edit_text("Choose an SKC SIR Super Six material.", reply_markup=supersix_buttons_skc_sir)
        elif callback_data == "super_six_rs_sir_":
            await query.message.edit_text("Choose an RS SIR Super Six material.", reply_markup=supersix_buttons_rs_sir)
        else:
            await query.message.edit_text("Choose a Super Six category.", reply_markup=supersix_buttons)
    else:
        category = CATEGORY_MAPPING.get(callback_data, None)
        if category:
            await send_documents(app, query.message.chat.id, category)
        else:
            await query.message.edit_text("Invalid selection. Please try again.", reply_markup=home_buttons)


