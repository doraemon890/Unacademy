from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Ava.core.Documents import *

# Define paths for each document category
DOCUMENT_PATHS = {
    "books": "Ava/core/Documents/books/",
    "notes_akansha_mam": "Ava/core/Documents/notes_akansha_mam/",
    "notes_anupam_sir": "Ava/core/Documents/notes_anupam_sir/",
    "notes_skc_sir": "Ava/core/Documents/notes_skc_sir/",
    "handwritten_notes": "Ava/core/Documents/handwritten_notes/",
    "elps_physics": "Ava/core/Documents/elps_physics/",
    "elps_chemistry": "Ava/core/Documents/elps_chemistry/",
    "elps_biology": "Ava/core/Documents/elps_biology/",
    "modules_3_1_physics": "Ava/core/Documents/modules_3_1_physics/",
    "modules_3_1_chemistry": "Ava/core/Documents/modules_3_1_chemistry/",
    "modules_3_1_biology": "Ava/core/Documents/modules_3_1_biology/",
    "modules_4_0_physics": "Ava/core/Documents/modules_4_0_physics/",
    "modules_4_0_chemistry": "Ava/core/Documents/modules_4_0_chemistry/",
    "modules_4_0_biology": "Ava/core/Documents/modules_4_0_biology/",
    "modules_assertion_reason": "Ava/core/Documents/modules_assertion_reason/",
    "modules_qft_series": "Ava/core/Documents/modules_qft_series/",
    "modules_mindmaps": "Ava/core/Documents/modules_mindmaps/",
    "test_series_offline": "Ava/core/Documents/test_series_offline/",
    "test_series_plus_iconic": "Ava/core/Documents/test_series_plus_iconic/",
    "premium_material_prateek_sir": "Ava/core/Documents/premium_material_prateek_sir/",
    "premium_material_akm_sir": "Ava/core/Documents/premium_material_akm_sir/",
    "premium_material_seep_mam_npp": "Ava/core/Documents/premium_material_seep_mam_npp/",
    "premium_material_seep_mam_dpp": "Ava/core/Documents/premium_material_seep_mam_dpp/",
    "premium_material_seep_mam_formula_booklet": "Ava/core/Documents/premium_material_seep_mam_formula_booklet/",
    "premium_material_seep_mam_important_booklets": "Ava/core/Documents/premium_material_seep_mam_important_booklets/",
    "premium_material_akansha_mam_dpp": "Ava/core/Documents/premium_material_akansha_mam_dpp/",
    "premium_material_akansha_mam_mindmaps": "Ava/core/Documents/premium_material_akansha_mam_mindmaps/",
    "super_six_prateek_sir_class": "Ava/core/Documents/super_six_prateek_sir_class/",
    "super_six_prateek_sir_physicsalcoholics_points": "Ava/core/Documents/super_six_prateek_sir_physicsalcoholics_points/",
    "super_six_akm_sir_course": "Ava/core/Documents/super_six_akm_sir_course/",
    "super_six_akm_sir_pyq_series": "Ava/core/Documents/super_six_akm_sir_pyq_series/",
    "super_six_akm_sir_module_discussion": "Ava/core/Documents/super_six_akm_sir_module_discussion/",
    "super_six_skc_sir_course": "Ava/core/Documents/super_six_skc_sir_course/",
    "super_six_skc_sir_organic_mechanism": "Ava/core/Documents/super_six_skc_sir_organic_mechanism/",
    "super_six_skc_sir_dpp": "Ava/core/Documents/super_six_skc_sir_dpp/",
    "super_six_rs_sir_course": "Ava/core/Documents/super_six_rs_sir_course/",
    "super_six_rs_sir_dpp": "Ava/core/Documents/super_six_rs_sir_dpp/"
}

# Helper function to create inline keyboard
def create_inline_keyboard(buttons):
    return InlineKeyboardMarkup([[InlineKeyboardButton(text, url) if url.startswith("https") else InlineKeyboardButton(text, callback_data=url) for text, url in row] for row in buttons])

# Button Definitions
home_buttons = create_inline_keyboard([
    [("Support", "support_"), ("Unacademy Modules", "modes_")],
    [("Get Free Access✅", "force_")]
])

support_buttons = create_inline_keyboard([
    [("ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ", "https://t.me/JARVIS_V_SUPPORT"), ("ᴅᴇᴠᴇʟᴏᴘᴇʀ", "https://t.me/JARVIS_V2")],
    [("Go Back ◀️", "home_")]
])

force_buttons = create_inline_keyboard([
    [("ᴊᴏɪɴ", "https://t.me/JARVIS_V_SUPPORT"), ("Verify ✅", "home_")]
])

modes_buttons = create_inline_keyboard([
    [("BOOKS", "books_"), ("NOTES", "notes_")],
    [("Modules", "modules_"), ("Elps", "elps_")],
    [("Queries", "query_")],
    [("Super Six", "supersix_"), ("Premium Materials", "premium_")],
    [("Go Back ◀️", "home_")]
])

notes_buttons = create_inline_keyboard([
    [("SEEP MAM", "notes_seep_mam_"), ("AKANSHA MAM", "notes_akansha_mam_")],
    [("ANUPAM SIR", "notes_anupam_sir_"), ("SKC SIR", "notes_skc_sir_")],
    [("HANDWRITTEN SHORT NOTES", "handwritten_notes_")],
    [("Go Back ◀️", "modes_")]
])

elps_buttons = create_inline_keyboard([
    [("PHYSICS", "elps_physics_"), ("CHEMISTRY", "elps_chemistry_")],
    [("BIOLOGY", "elps_biology_")],
    [("Go Back ◀️", "modes_")]
])

module_buttons = create_inline_keyboard([
    [("VERSION 3.1", "modules_3_1_"), ("VERSION 4.0", "modules_4_0_")],
    [("Go Back ◀️", "modes_")]
])

module_buttons_3_1 = create_inline_keyboard([
    [("PHYSICS", "modules_3_1_physics_"), ("CHEMISTRY", "modules_3_1_chemistry_")],
    [("BIOLOGY", "modules_3_1_biology_")],
    [("Go Back ◀️", "modules_")]
])

module_buttons_4_0 = create_inline_keyboard([
    [("PHYSICS", "modules_4_0_physics_"), ("CHEMISTRY", "modules_4_0_chemistry_")],
    [("BIOLOGY", "modules_4_0_biology_")],
    [("Go Back ◀️", "modules_")]
])

query_buttons = create_inline_keyboard([
    [("ASSERTION REASON", "modules_assertion_reason_"), ("QFT SERIES", "modules_qft_series_")],
    [("MINDMAPS", "modules_mindmaps_"), ("Test Series", "test_series_")],
    [("Go Back ◀️", "modes_")]
])

test_series_buttons = create_inline_keyboard([
    [("OFFLINE", "test_series_offline_"), ("PLUS/ICONIC", "test_series_plus_iconic_")],
    [("Go Back ◀️", "query_buttons_")]
])

premium_buttons = create_inline_keyboard([
    [("SEEP MAM", "premium_material_seep_mam_"), ("AKANSHA MAM", "premium_material_akansha_mam_")],
    [("PRATEEK SIR", "premium_material_prateek_sir_"), ("AKM SIR", "premium_material_akm_sir_")],
    [("Go Back ◀️", "modes_")]
])

premium_buttons_seep_mam = create_inline_keyboard([
    [("NPP", "premium_material_seep_mam_npp_"), ("DPP", "premium_material_seep_mam_dpp_")],
    [("FORMULA BOOKLET", "premium_material_seep_mam_formula_booklet_"), ("IMPORTANT BOOKLETS", "premium_material_seep_mam_important_booklets_")],
    [("Go Back ◀️", "premium_buttons_")]
])

premium_buttons_akansha_mam = create_inline_keyboard([
    [("DPP", "premium_material_akansha_mam_dpp_"), ("MINDMAPS", "premium_material_akansha_mam_mindmaps_")],
    [("Go Back ◀️", "premium_buttons_")]
])

premium_buttons_prateek_sir = create_inline_keyboard([
    [("Go Back ◀️", "premium_buttons_")]
])

premium_buttons_akm_sir = create_inline_keyboard([
    [("Go Back ◀️", "premium_buttons_")]
])
