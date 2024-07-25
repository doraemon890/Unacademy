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

# Button Definitions
home_buttons = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", callback_data="support_"),
        InlineKeyboardButton("ᴜɴᴀᴄᴀᴅᴇᴍʏ ᴍᴏᴅᴜʟᴇs", callback_data="modes_")
    ],
    [
        InlineKeyboardButton("ɢᴇᴛ ғʀᴇᴇ ᴀᴄᴄᴇss✅", callback_data="force_")
    ]
])


support_buttons = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ", url="https://t.me/JARVIS_V_SUPPORT"),
        InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/JARVIS_V2")
    ],
    [
        InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ ◀️", callback_data="home_")
    ]
])


force_buttons = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("ᴊᴏɪɴ", url="https://t.me/JARVIS_V_SUPPORT"),
        InlineKeyboardButton("ᴠᴇʀɪғʏ ✅", callback_data="home_")
    ],
])


modes_buttons = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("ʙᴏᴏᴋs", callback_data="books_"),
        InlineKeyboardButton("ɴᴏᴛᴇs", callback_data="notes_")
    ],
    [
        InlineKeyboardButton("ᴍᴏᴅᴜʟᴇs", callback_data="modules_"),
        InlineKeyboardButton("ᴇʟᴘs", callback_data="elps_")
    ],
    [
        InlineKeyboardButton("ǫᴜᴇʀɪᴇs", callback_data="query_")
    ],
    [
        InlineKeyboardButton("sᴜᴘᴇʀ sɪx ", callback_data="supersix_"),
        InlineKeyboardButton("ᴘʀᴇᴍɪᴜᴍ ᴍᴀᴛᴇʀɪᴀʟs", callback_data="premium_")
    ],
    [
        InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ ◀️", callback_data="home_")
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
        InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ ◀️", callback_data="modes_")
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
        InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ ◀️", callback_data="modes_")
    ]
])

module_buttons = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("VERSION 3.1", callback_data="modules_3_1_"),
        InlineKeyboardButton("VERSION 4.0", callback_data="modules_4_0_")
    ],
    [
        InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ ◀️", callback_data="modes_")
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
        InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ ◀️", callback_data="modules_")
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
        InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ ◀️", callback_data="modules_")
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
        InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ ◀️", callback_data="modes_")
    ]
])

test_series_buttons = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("OFFLINE", callback_data="test_series_offline_"),
        InlineKeyboardButton("PLUS/ICONIC", callback_data="test_series_plus_iconic_")
    ],
    [
        InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ ◀️", callback_data="query_buttons_")
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
        InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ ◀️", callback_data="modes_")
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
        InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ ◀️", callback_data="premium_buttons_")
    ]
])

premium_buttons_akansha_mam = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("DPP", callback_data="premium_material_akansha_mam_dpp_"),
        InlineKeyboardButton("MINDMAPS", callback_data="premium_material_akansha_mam_mindmaps_")
    ],
    [
        InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ ◀️", callback_data="premium_buttons_")
    ]
])

premium_buttons_prateek_sir = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ ◀️", callback_data="premium_buttons_")
    ]
])

premium_buttons_akm_sir = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ ◀️", callback_data="premium_buttons_")
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
        InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ ◀️", callback_data="modes_")
    ]
])

supersix_buttons_prateek_sir = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("CLASS", callback_data="super_six_prateek_sir_class_"),
        InlineKeyboardButton("PHYSICSALCOHOLICS POINTS", callback_data="super_six_prateek_sir_physicsalcoholics_points_")
    ],
    [
        InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ ◀️", callback_data="supersix_")
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
        InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ ◀️", callback_data="supersix_")
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
        InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ ◀️", callback_data="supersix_")
    ]
])

supersix_buttons_rs_sir = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("COURSE", callback_data="super_six_rs_sir_course_"),
        InlineKeyboardButton("DPP", callback_data="super_six_rs_sir_dpp_")
    ],
    [
        InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ ◀️", callback_data="supersix_")
    ]
])
