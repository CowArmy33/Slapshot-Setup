from os.path import normpath, join, isdir
from os import listdir
import time

template = """
{{
    "current_scene": "The Desk",
    "current_program_scene": "The Desk",
    "scene_order": [
        {{
            "name": "Game"
        }},
        {{
            "name": "Stats"
        }},
        {{
            "name": "The Desk"
        }},
        {{
            "name": "Matchup"
        }},
        {{
            "name": "Right Team"
        }},
        {{
            "name": "Left Team"
        }},
        {{
            "name": "Ladder"
        }},
        {{
            "name": "Schedule PostGame"
        }},
        {{
            "name": "---------- Post-Intro ^ ---------"
        }},
        {{
            "name": "Right Team Intro"
        }},
        {{
            "name": "Left Team Intro"
        }},
        {{
            "name": "Schedule PreGame"
        }},
        {{
            "name": "Intro"
        }},
        {{
            "name": "Loading"
        }},
        {{
            "name": "[NS] Game Score"
        }},
        {{
            "name": "[NS] Statboard"
        }},
        {{
            "name": "[NS] Casters"
        }},
        {{
            "name": "[NS] Background"
        }},
        {{
            "name": "[NS] Replay"
        }},
        {{
            "name": "[NS] Overlays"
        }},
        {{
            "name": "[NS] Background Left"
        }},
        {{
            "name": "[NS] Background Right"
        }},
        {{
            "name": "Display Cap"
        }},
        {{
            "name": "Scene 2 2"
        }},
        {{
            "name": "Temp"
        }}
    ],
    "name": "Slapshot Casting - OSL",
    "sources": [
        {{
            "prev_ver": 503382018,
            "name": "Matchup graph",
            "uuid": "9fd5a572-d440-4f0f-b8bc-1297e1359a26",
            "id": "browser_source",
            "versioned_id": "browser_source",
            "settings": {{
                "is_local_file": true,
                "local_file": "{pathin}/general-stats.html",
                "width": 1200,
                "height": 1080,
                "shutdown": true,
                "restart_when_active": true
            }},
            "mixers": 255,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.mute": [],
                "libobs.unmute": [],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": [],
                "ObsBrowser.Refresh": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Matchup",
            "uuid": "5a408915-6c9d-4585-b40c-f2bd9f6b0718",
            "id": "scene",
            "versioned_id": "scene",
            "settings": {{
                "custom_size": false,
                "id_counter": 12,
                "items": [
                    {{
                        "name": "[NS] Background",
                        "source_uuid": "f3da34e6-1ba4-4980-a925-2639f7bda1cc",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 1,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Stats and Teams",
                        "source_uuid": "0d0df9bf-873f-4135-afdb-32839f403aee",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 2,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "[NS] Overlays",
                        "source_uuid": "040479cf-960d-42a7-abd2-d0c0999568a8",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 3,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Caster Frame",
                        "source_uuid": "efe75205-f7f9-4f0f-9206-47408bf5ef08",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1461.0,
                            "y": 406.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 13,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Casters",
                        "source_uuid": "8d5d9598-e3c9-42d4-b072-8ecc0c0e89db",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1520.0,
                            "y": 531.0
                        }},
                        "scale": {{
                            "x": 1.0885714292526245,
                            "y": 1.0880000591278076
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 18,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Caster Setup",
                        "source_uuid": "4bb05f72-5ed2-4465-bf77-b7c92c741c46",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1461.0,
                            "y": 406.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 4,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "[NS] Overlays",
                        "source_uuid": "040479cf-960d-42a7-abd2-d0c0999568a8",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 6,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Matchup graph",
                        "source_uuid": "9fd5a572-d440-4f0f-b8bc-1297e1359a26",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 0.85500001907348633,
                            "y": 0.85462963581085205
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1424.0,
                            "y": 994.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 8,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "test",
                        "source_uuid": "b2f8ed2e-b1ad-47c2-8b25-97c93b4d18f7",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1468.0,
                            "y": 25.0
                        }},
                        "scale": {{
                            "x": 0.60857141017913818,
                            "y": 0.60810810327529907
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 9,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord",
                        "source_uuid": "a526dbdc-0cb6-4cdb-ac11-2e4828bde919",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 10,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Microphone",
                        "source_uuid": "3b69d9d9-97ea-4347-a7c1-3346e7dc542c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 11,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "TickerBG",
                        "source_uuid": "c3b1a8ca-9df6-4ebc-84bf-5decc9b249e4",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 30,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Ticker Text",
                        "source_uuid": "50bcd47d-7a30-4206-bc09-732f141e585c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 199.39999389648438,
                            "y": 1019.0
                        }},
                        "scale": {{
                            "x": 0.85850000381469727,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 32,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Ticker",
                        "source_uuid": "03531d4f-e2b0-4503-b2c0-8e0c2db3c9b6",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 12,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "OBSBasic.SelectScene": [],
                "libobs.show_scene_item.1": [],
                "libobs.hide_scene_item.1": [],
                "libobs.show_scene_item.2": [],
                "libobs.hide_scene_item.2": [],
                "libobs.show_scene_item.3": [],
                "libobs.hide_scene_item.3": [],
                "libobs.show_scene_item.4": [],
                "libobs.hide_scene_item.4": [],
                "libobs.show_scene_item.6": [],
                "libobs.hide_scene_item.6": [],
                "libobs.show_scene_item.8": [],
                "libobs.hide_scene_item.8": [],
                "libobs.show_scene_item.9": [],
                "libobs.hide_scene_item.9": [],
                "libobs.show_scene_item.10": [],
                "libobs.hide_scene_item.10": [],
                "libobs.show_scene_item.11": [],
                "libobs.hide_scene_item.11": [],
                "libobs.show_scene_item.12": [],
                "libobs.hide_scene_item.12": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{
                "transition": ""
            }}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Window Capture",
            "uuid": "daf8dd9f-e04b-4233-8ec4-42568156467f",
            "id": "window_capture",
            "versioned_id": "window_capture",
            "settings": {{
                "window": "hot stats - Google Sheets — Mozilla Firefox:MozillaWindowClass:firefox.exe"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.mute": [],
                "libobs.unmute": [],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Scene 2 2",
            "uuid": "ed58db7a-15b3-47b9-8355-eb6ec7dda395",
            "id": "scene",
            "versioned_id": "scene",
            "settings": {{
                "custom_size": false,
                "id_counter": 8,
                "items": [
                    {{
                        "name": "Window Capture",
                        "source_uuid": "daf8dd9f-e04b-4233-8ec4-42568156467f",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1920.0,
                            "y": 1080.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 4,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Microphone",
                        "source_uuid": "3b69d9d9-97ea-4347-a7c1-3346e7dc542c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 5,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Lofi",
                        "source_uuid": "556fe34e-e49d-48e0-8a68-ba2d83c3b8bb",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 6,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord",
                        "source_uuid": "a526dbdc-0cb6-4cdb-ac11-2e4828bde919",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 7,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Microphone",
                        "source_uuid": "3b69d9d9-97ea-4347-a7c1-3346e7dc542c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 8,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "OBSBasic.SelectScene": [],
                "libobs.show_scene_item.4": [],
                "libobs.hide_scene_item.4": [],
                "libobs.show_scene_item.5": [],
                "libobs.hide_scene_item.5": [],
                "libobs.show_scene_item.6": [],
                "libobs.hide_scene_item.6": [],
                "libobs.show_scene_item.7": [],
                "libobs.hide_scene_item.7": [],
                "libobs.show_scene_item.8": [],
                "libobs.hide_scene_item.8": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Roster",
            "uuid": "c40c1da6-03a9-4c06-839d-1b99a1aad22a",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "drop_shadow": true,
                "text": "Roster",
                "font": {{
                    "face": "Century Gothic",
                    "flags": 1,
                    "size": 120,
                    "style": "Bold"
                }}
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Left Team",
            "uuid": "def84486-ea1c-4193-96e8-85855d90d038",
            "id": "scene",
            "versioned_id": "scene",
            "settings": {{
                "custom_size": false,
                "id_counter": 16,
                "items": [
                    {{
                        "name": "Stats and Teams",
                        "source_uuid": "0d0df9bf-873f-4135-afdb-32839f403aee",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 2,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "[NS] Background Left",
                        "source_uuid": "9d0b3f6a-2570-403e-a70e-1d57293bdc07",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 1,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Left Logo",
                        "source_uuid": "b31bc3c2-c8f8-4a0d-a423-04fdbabaa8c0",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 37.0,
                            "y": 45.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 964.0,
                            "y": 423.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 3,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Caster Frame",
                        "source_uuid": "efe75205-f7f9-4f0f-9206-47408bf5ef08",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 622.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 13,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Casters",
                        "source_uuid": "8d5d9598-e3c9-42d4-b072-8ecc0c0e89db",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 59.0,
                            "y": 747.0
                        }},
                        "scale": {{
                            "x": 1.0885714292526245,
                            "y": 1.0880000591278076
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 18,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Caster Setup",
                        "source_uuid": "4bb05f72-5ed2-4465-bf77-b7c92c741c46",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 622.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 5,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{
                            "collapsed": true
                        }}
                    }},
                    {{
                        "name": "Roster",
                        "source_uuid": "c40c1da6-03a9-4c06-839d-1b99a1aad22a",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1276.0,
                            "y": 61.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 6,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Left Roster",
                        "source_uuid": "27ae541f-e26d-477c-bb3f-19da5b6e26a4",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1139.0,
                            "y": 249.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 631.0,
                            "y": 630.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 10,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Left Text",
                        "source_uuid": "b99d0e62-4d9a-40d6-a619-95df24f1f639",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 37.0,
                            "y": 468.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 8,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 964.0,
                            "y": 101.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 7,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "[NS] Overlays",
                        "source_uuid": "040479cf-960d-42a7-abd2-d0c0999568a8",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 11,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord",
                        "source_uuid": "a526dbdc-0cb6-4cdb-ac11-2e4828bde919",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 13,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Microphone",
                        "source_uuid": "3b69d9d9-97ea-4347-a7c1-3346e7dc542c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 14,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "TickerBG",
                        "source_uuid": "c3b1a8ca-9df6-4ebc-84bf-5decc9b249e4",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 30,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Ticker Text",
                        "source_uuid": "50bcd47d-7a30-4206-bc09-732f141e585c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 199.39999389648438,
                            "y": 1019.0
                        }},
                        "scale": {{
                            "x": 0.85850000381469727,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 32,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Ticker",
                        "source_uuid": "03531d4f-e2b0-4503-b2c0-8e0c2db3c9b6",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 15,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "test",
                        "source_uuid": "b2f8ed2e-b1ad-47c2-8b25-97c93b4d18f7",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 572.0,
                            "y": 729.0
                        }},
                        "scale": {{
                            "x": 0.65142858028411865,
                            "y": 0.65135133266448975
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 16,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "OBSBasic.SelectScene": [],
                "libobs.show_scene_item.2": [],
                "libobs.hide_scene_item.2": [],
                "libobs.show_scene_item.1": [],
                "libobs.hide_scene_item.1": [],
                "libobs.show_scene_item.3": [],
                "libobs.hide_scene_item.3": [],
                "libobs.show_scene_item.5": [],
                "libobs.hide_scene_item.5": [],
                "libobs.show_scene_item.6": [],
                "libobs.hide_scene_item.6": [],
                "libobs.show_scene_item.10": [],
                "libobs.hide_scene_item.10": [],
                "libobs.show_scene_item.7": [],
                "libobs.hide_scene_item.7": [],
                "libobs.show_scene_item.11": [],
                "libobs.hide_scene_item.11": [],
                "libobs.show_scene_item.13": [],
                "libobs.hide_scene_item.13": [],
                "libobs.show_scene_item.14": [],
                "libobs.hide_scene_item.14": [],
                "libobs.show_scene_item.15": [],
                "libobs.hide_scene_item.15": [],
                "libobs.show_scene_item.16": [],
                "libobs.hide_scene_item.16": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "[NS] Background Right",
            "uuid": "aa673de4-763d-4cb8-a47d-65e2c6e157b0",
            "id": "scene",
            "versioned_id": "scene",
            "settings": {{
                "custom_size": false,
                "id_counter": 3,
                "items": [
                    {{
                        "name": "Shimmer",
                        "source_uuid": "4aabbb42-00c7-468d-89c1-c4f62e6eb377",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 1,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "New BG",
                        "source_uuid": "69e55fee-56ee-46b9-9fa4-8867d477d124",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 2,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "[NS] Replay",
                        "source_uuid": "0e959ed9-27a0-41f0-9215-ea77e658c791",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.3171232938766479,
                            "y": 1.3170732259750366
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 238,
                        "crop_top": 141,
                        "crop_right": 222,
                        "crop_bottom": 119,
                        "id": 3,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "OBSBasic.SelectScene": [],
                "libobs.show_scene_item.1": [],
                "libobs.hide_scene_item.1": [],
                "libobs.show_scene_item.2": [],
                "libobs.hide_scene_item.2": [],
                "libobs.show_scene_item.3": [],
                "libobs.hide_scene_item.3": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}},
            "filters": [
                {{
                    "prev_ver": 503382018,
                    "name": "Image Mask/Blend",
                    "uuid": "59add09b-61ad-45e1-9bb1-4f55a622615c",
                    "id": "mask_filter",
                    "versioned_id": "mask_filter_v2",
                    "settings": {{
                        "image_path": "{colourAway}",
                        "type": "blend_mul_filter.effect",
                        "opacity": 1
                    }},
                    "mixers": 0,
                    "sync": 0,
                    "flags": 0,
                    "volume": 1.0,
                    "balance": 0.5,
                    "enabled": true,
                    "muted": false,
                    "push-to-mute": false,
                    "push-to-mute-delay": 0,
                    "push-to-talk": false,
                    "push-to-talk-delay": 0,
                    "hotkeys": {{}},
                    "deinterlace_mode": 0,
                    "deinterlace_field_order": 0,
                    "monitoring_type": 0,
                    "private_settings": {{}}
                }}
            ]
        }},
        {{
            "prev_ver": 503382018,
            "name": "[NS] Background Left",
            "uuid": "9d0b3f6a-2570-403e-a70e-1d57293bdc07",
            "id": "scene",
            "versioned_id": "scene",
            "settings": {{
                "custom_size": false,
                "id_counter": 3,
                "items": [
                    {{
                        "name": "Shimmer",
                        "source_uuid": "4aabbb42-00c7-468d-89c1-c4f62e6eb377",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 1,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "New BG",
                        "source_uuid": "69e55fee-56ee-46b9-9fa4-8867d477d124",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 2,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "[NS] Replay",
                        "source_uuid": "0e959ed9-27a0-41f0-9215-ea77e658c791",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.3171232938766479,
                            "y": 1.3170732259750366
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 238,
                        "crop_top": 141,
                        "crop_right": 222,
                        "crop_bottom": 119,
                        "id": 3,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "OBSBasic.SelectScene": [],
                "libobs.show_scene_item.1": [],
                "libobs.hide_scene_item.1": [],
                "libobs.show_scene_item.2": [],
                "libobs.hide_scene_item.2": [],
                "libobs.show_scene_item.3": [],
                "libobs.hide_scene_item.3": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}},
            "filters": [
                {{
                    "prev_ver": 503382018,
                    "name": "Image Mask/Blend",
                    "uuid": "8ae64e43-11ef-4c08-a34e-7f79d464ea75",
                    "id": "mask_filter",
                    "versioned_id": "mask_filter_v2",
                    "settings": {{
                        "image_path": "{colourHome}",
                        "type": "blend_mul_filter.effect",
                        "opacity": 1
                    }},
                    "mixers": 0,
                    "sync": 0,
                    "flags": 0,
                    "volume": 1.0,
                    "balance": 0.5,
                    "enabled": true,
                    "muted": false,
                    "push-to-mute": false,
                    "push-to-mute-delay": 0,
                    "push-to-talk": false,
                    "push-to-talk-delay": 0,
                    "hotkeys": {{}},
                    "deinterlace_mode": 0,
                    "deinterlace_field_order": 0,
                    "monitoring_type": 0,
                    "private_settings": {{}}
                }}
            ]
        }},
        {{
            "prev_ver": 503382018,
            "name": "ScoreFront",
            "uuid": "b9d25a44-5905-4a2f-a156-b7315330424a",
            "id": "image_source",
            "versioned_id": "image_source",
            "settings": {{
                "file": "{pathin}/ScoreFront.png"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}},
            "filters": [
                {{
                    "prev_ver": 503382018,
                    "name": "Image Mask/Blend",
                    "uuid": "40ddcb21-c872-40d9-bf82-31298ba0ec64",
                    "id": "mask_filter",
                    "versioned_id": "mask_filter_v2",
                    "settings": {{
                        "image_path": "{gradient}",
                        "type": "blend_mul_filter.effect"
                    }},
                    "mixers": 0,
                    "sync": 0,
                    "flags": 0,
                    "volume": 1.0,
                    "balance": 0.5,
                    "enabled": true,
                    "muted": false,
                    "push-to-mute": false,
                    "push-to-mute-delay": 0,
                    "push-to-talk": false,
                    "push-to-talk-delay": 0,
                    "hotkeys": {{}},
                    "deinterlace_mode": 0,
                    "deinterlace_field_order": 0,
                    "monitoring_type": 0,
                    "private_settings": {{}}
                }}
            ]
        }},
        {{
            "prev_ver": 503382018,
            "name": "ScoreBack",
            "uuid": "90c73104-8759-475a-a52f-11dc626da959",
            "id": "image_source",
            "versioned_id": "image_source",
            "settings": {{
                "file": "{pathin}/ScoreBack.png"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Team Name L 3",
            "uuid": "3673d563-b2f7-418e-b810-60fcf8f22e85",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "text": "Sydney Gafs",
                "font": {{
                    "face": "Century Gothic",
                    "flags": 0,
                    "size": 72,
                    "style": "Regular"
                }},
                "align": "center"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Team Name R 3",
            "uuid": "da485504-9d08-4342-a533-5ee96a230019",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "text": "South Sydney Sugargliders",
                "font": {{
                    "face": "Century Gothic",
                    "flags": 0,
                    "size": 72,
                    "style": "Regular"
                }},
                "align": "center"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Team Name L 2",
            "uuid": "0e104feb-6409-4a4d-a4e7-15823ff1bae6",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "text": "Spice Boys",
                "font": {{
                    "face": "Century Gothic",
                    "flags": 0,
                    "size": 72,
                    "style": "Regular"
                }},
                "align": "center"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Team Name R 2",
            "uuid": "ef0ac7ef-8655-4b39-9365-121776c00f9c",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "text": "Adelaide Saints",
                "font": {{
                    "face": "Century Gothic",
                    "flags": 0,
                    "size": 72,
                    "style": "Regular"
                }},
                "align": "center"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Team Name R 1",
            "uuid": "158d5e1e-bb1e-4158-8485-cccde9547879",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "text": "Thomas Shoubi",
                "font": {{
                    "face": "Century Gothic",
                    "flags": 0,
                    "size": 72,
                    "style": "Regular"
                }},
                "align": "center"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Team Name L 1",
            "uuid": "a51aa3e3-048c-432f-8eaf-6ca817ffa80d",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "text": "South Sydney Sugargliders",
                "font": {{
                    "face": "Century Gothic",
                    "flags": 0,
                    "size": 72,
                    "style": "Regular"
                }},
                "align": "center"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Game Time 3",
            "uuid": "dcecabec-939e-4e02-86a4-ca5c291bd2cb",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "text": "9:00pm",
                "font": {{
                    "face": "Century Gothic",
                    "flags": 0,
                    "size": 72,
                    "style": "Regular"
                }},
                "align": "center"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Game Time 2",
            "uuid": "3275f904-4ffc-4104-b944-06a85e5f5277",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "text": "10:00pm",
                "font": {{
                    "face": "Century Gothic",
                    "flags": 0,
                    "size": 72,
                    "style": "Regular"
                }},
                "align": "center"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Game Time 1",
            "uuid": "648a9ef9-263b-41ab-91fc-013110f154f0",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "text": "8:00pm",
                "font": {{
                    "face": "Century Gothic",
                    "flags": 0,
                    "size": 72,
                    "style": "Regular"
                }},
                "align": "center"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Match Logo Right 1",
            "uuid": "409c7aeb-1981-4f08-9375-529721ae03aa",
            "id": "image_source",
            "versioned_id": "image_source",
            "settings": {{
                "file": "{pathin}/Thomas Shoubi.png"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Match Logo Right 3",
            "uuid": "81618301-32d0-43f4-a207-da371f025c4f",
            "id": "image_source",
            "versioned_id": "image_source",
            "settings": {{
                "file": "{pathin}/South Sydney Sugargliders.png"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Match Logo Right 2",
            "uuid": "18348e45-ea23-4f92-aa76-65b710dc62be",
            "id": "image_source",
            "versioned_id": "image_source",
            "settings": {{
                "file": "{pathin}/Adelaide Saints.png"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Match Logo Left 3",
            "uuid": "fd7fa8fa-3bbb-472a-9e5c-dc1bf35b33c5",
            "id": "image_source",
            "versioned_id": "image_source",
            "settings": {{
                "file": "{pathin}/Sydney Gafs.png"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Match Logo Left 2",
            "uuid": "b8f05595-200d-4aed-aa3b-5278916a3fd9",
            "id": "image_source",
            "versioned_id": "image_source",
            "settings": {{
                "file": "{pathin}/Spice Boys.png"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Match Logo Left 1",
            "uuid": "3a6e3fd8-68d7-40be-b797-5aa89a12a176",
            "id": "image_source",
            "versioned_id": "image_source",
            "settings": {{
                "file": "{pathin}/South Sydney Sugargliders.png"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Game Num 2",
            "uuid": "574f7b32-d69a-438f-a8b7-a4c2987ef35f",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "text": "IM SF",
                "font": {{
                    "face": "Century Gothic",
                    "flags": 0,
                    "size": 72,
                    "style": "Regular"
                }},
                "align": "center"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Game Num 1",
            "uuid": "70b4dda3-9a9e-4e4b-932f-9f9cb80b18a2",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "text": "PRO SF",
                "font": {{
                    "face": "Century Gothic",
                    "flags": 0,
                    "size": 72,
                    "style": "Regular"
                }},
                "align": "center"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Game Num 3",
            "uuid": "87a7928c-4d29-4344-a0ac-c6657e4e6878",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "text": "",
                "font": {{
                    "face": "Century Gothic",
                    "flags": 0,
                    "size": 72,
                    "style": "Regular"
                }},
                "align": "center"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Schedule BG",
            "uuid": "3a7f77d5-dc40-44c8-9538-403167511477",
            "id": "image_source",
            "versioned_id": "image_source",
            "settings": {{
                "file": "{pathin}/Schedule.png"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Schedule PreGame",
            "uuid": "c60a535d-f7fe-425e-b999-d73ba59d7baa",
            "id": "scene",
            "versioned_id": "scene",
            "settings": {{
                "custom_size": false,
                "id_counter": 39,
                "items": [
                    {{
                        "name": "Intro Music",
                        "source_uuid": "e1aa771d-fa87-43e1-badc-d9bdec868521",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 33,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "[NS] Background",
                        "source_uuid": "f3da34e6-1ba4-4980-a925-2639f7bda1cc",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 1,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Schedule BG",
                        "source_uuid": "3a7f77d5-dc40-44c8-9538-403167511477",
                        "visible": false,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 2,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Caster Frame",
                        "source_uuid": "efe75205-f7f9-4f0f-9206-47408bf5ef08",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1504.0,
                            "y": 721.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 13,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Casters",
                        "source_uuid": "8d5d9598-e3c9-42d4-b072-8ecc0c0e89db",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1563.0,
                            "y": 846.0
                        }},
                        "scale": {{
                            "x": 1.0885714292526245,
                            "y": 1.0880000591278076
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 18,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Caster Setup",
                        "source_uuid": "4bb05f72-5ed2-4465-bf77-b7c92c741c46",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1504.0,
                            "y": 721.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 3,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{
                            "collapsed": false
                        }}
                    }},
                    {{
                        "name": "Discord Box Back",
                        "source_uuid": "f1c6105f-819f-442e-bc9f-23d1bed3be98",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 20.0,
                            "y": 912.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 16,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord Invite Link",
                        "source_uuid": "056ad710-8177-4fe4-ab8e-2e33c5cf7759",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 30.0,
                            "y": 923.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 17,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord Box Frame",
                        "source_uuid": "17b335cb-ddd9-43bf-8cd3-6b017b716816",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 20.0,
                            "y": 912.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 15,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord Link",
                        "source_uuid": "f2f5e807-beb9-4e3d-9d45-a287984599e9",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 20.0,
                            "y": 912.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 4,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{
                            "collapsed": true
                        }}
                    }},
                    {{
                        "name": "Game Time 3",
                        "source_uuid": "dcecabec-939e-4e02-86a4-ca5c291bd2cb",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1653.0,
                            "y": 574.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 267.0,
                            "y": 183.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 25,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Match Logo Right 3",
                        "source_uuid": "81618301-32d0-43f4-a207-da371f025c4f",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1379.0,
                            "y": 585.0
                        }},
                        "scale": {{
                            "x": 0.30236220359802246,
                            "y": 0.30206379294395447
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 273.0,
                            "y": 158.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 18,
                        "group_item_backup": true,
                        "scale_filter": "bilinear",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Team Name R 3",
                        "source_uuid": "da485504-9d08-4342-a533-5ee96a230019",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1004.0,
                            "y": 573.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 364.0,
                            "y": 183.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 31,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Team Name L 3",
                        "source_uuid": "3673d563-b2f7-418e-b810-60fcf8f22e85",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 552.0,
                            "y": 574.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 364.0,
                            "y": 183.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 32,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Match Logo Left 3",
                        "source_uuid": "fd7fa8fa-3bbb-472a-9e5c-dc1bf35b33c5",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 267.0,
                            "y": 585.0
                        }},
                        "scale": {{
                            "x": 0.30236220359802246,
                            "y": 0.30206379294395447
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 273.0,
                            "y": 158.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 16,
                        "group_item_backup": true,
                        "scale_filter": "bilinear",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Game Num 3",
                        "source_uuid": "87a7928c-4d29-4344-a0ac-c6657e4e6878",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 574.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 267.0,
                            "y": 183.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 7,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Game #3",
                        "source_uuid": "e42d976c-9dc6-4f84-b21f-df7ce6a84fb7",
                        "visible": false,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 573.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 12,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{
                            "collapsed": true
                        }}
                    }},
                    {{
                        "name": "Game Time 2",
                        "source_uuid": "3275f904-4ffc-4104-b944-06a85e5f5277",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1652.0,
                            "y": 384.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 267.0,
                            "y": 183.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 24,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Match Logo Right 2",
                        "source_uuid": "18348e45-ea23-4f92-aa76-65b710dc62be",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1379.0,
                            "y": 396.0
                        }},
                        "scale": {{
                            "x": 0.30236220359802246,
                            "y": 0.30206379294395447
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 273.0,
                            "y": 158.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 17,
                        "group_item_backup": true,
                        "scale_filter": "bilinear",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Team Name R 2",
                        "source_uuid": "ef0ac7ef-8655-4b39-9365-121776c00f9c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1004.0,
                            "y": 384.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 364.0,
                            "y": 183.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 29,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Team Name L 2",
                        "source_uuid": "0e104feb-6409-4a4d-a4e7-15823ff1bae6",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 552.0,
                            "y": 385.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 364.0,
                            "y": 183.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 30,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Match Logo Left 2",
                        "source_uuid": "b8f05595-200d-4aed-aa3b-5278916a3fd9",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 267.0,
                            "y": 396.0
                        }},
                        "scale": {{
                            "x": 0.30236220359802246,
                            "y": 0.30206379294395447
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 273.0,
                            "y": 158.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 15,
                        "group_item_backup": true,
                        "scale_filter": "bilinear",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Game Num 2",
                        "source_uuid": "574f7b32-d69a-438f-a8b7-a4c2987ef35f",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 384.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 267.0,
                            "y": 183.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 10,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Game #2",
                        "source_uuid": "a1b7ce7d-abbf-410e-b73e-160675ed1a72",
                        "visible": false,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 384.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 11,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{
                            "collapsed": false
                        }}
                    }},
                    {{
                        "name": "Game Time 1",
                        "source_uuid": "648a9ef9-263b-41ab-91fc-013110f154f0",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1653.0,
                            "y": 194.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 267.0,
                            "y": 183.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 23,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Match Logo Right 1",
                        "source_uuid": "409c7aeb-1981-4f08-9375-529721ae03aa",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1379.0,
                            "y": 206.0
                        }},
                        "scale": {{
                            "x": 0.30236220359802246,
                            "y": 0.30206379294395447
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 274.0,
                            "y": 158.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 19,
                        "group_item_backup": true,
                        "scale_filter": "bilinear",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Team Name R 1",
                        "source_uuid": "158d5e1e-bb1e-4158-8485-cccde9547879",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1004.0,
                            "y": 194.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 364.0,
                            "y": 183.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 28,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Team Name L 1",
                        "source_uuid": "a51aa3e3-048c-432f-8eaf-6ca817ffa80d",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 552.0,
                            "y": 195.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 364.0,
                            "y": 183.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 27,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Match Logo Left 1",
                        "source_uuid": "3a6e3fd8-68d7-40be-b797-5aa89a12a176",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 267.0,
                            "y": 206.0
                        }},
                        "scale": {{
                            "x": 0.30236220359802246,
                            "y": 0.30206379294395447
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 274.0,
                            "y": 158.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 14,
                        "group_item_backup": true,
                        "scale_filter": "bilinear",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Game Num 1",
                        "source_uuid": "70b4dda3-9a9e-4e4b-932f-9f9cb80b18a2",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 201.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 267.0,
                            "y": 183.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 9,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Game #1",
                        "source_uuid": "09d5d84f-c1da-40cd-aa96-8cdc7215d853",
                        "visible": false,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 194.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 5,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{
                            "collapsed": true
                        }}
                    }},
                    {{
                        "name": "[NS] Overlays",
                        "source_uuid": "040479cf-960d-42a7-abd2-d0c0999568a8",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 34,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord",
                        "source_uuid": "a526dbdc-0cb6-4cdb-ac11-2e4828bde919",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 35,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Microphone",
                        "source_uuid": "3b69d9d9-97ea-4347-a7c1-3346e7dc542c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 36,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Browser",
                        "source_uuid": "22c6eb60-8391-48a1-807c-d0a5d1ece151",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 213.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 38,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Schedule BG",
                        "source_uuid": "3a7f77d5-dc40-44c8-9538-403167511477",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 907,
                        "id": 39,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "OBSBasic.SelectScene": [],
                "libobs.show_scene_item.33": [],
                "libobs.hide_scene_item.33": [],
                "libobs.show_scene_item.1": [],
                "libobs.hide_scene_item.1": [],
                "libobs.show_scene_item.2": [],
                "libobs.hide_scene_item.2": [],
                "libobs.show_scene_item.3": [],
                "libobs.hide_scene_item.3": [],
                "libobs.show_scene_item.4": [],
                "libobs.hide_scene_item.4": [],
                "libobs.show_scene_item.12": [],
                "libobs.hide_scene_item.12": [],
                "libobs.show_scene_item.11": [],
                "libobs.hide_scene_item.11": [],
                "libobs.show_scene_item.5": [],
                "libobs.hide_scene_item.5": [],
                "libobs.show_scene_item.34": [],
                "libobs.hide_scene_item.34": [],
                "libobs.show_scene_item.35": [],
                "libobs.hide_scene_item.35": [],
                "libobs.show_scene_item.36": [],
                "libobs.hide_scene_item.36": [],
                "libobs.show_scene_item.38": [],
                "libobs.hide_scene_item.38": [],
                "libobs.show_scene_item.39": [],
                "libobs.hide_scene_item.39": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{
                "transition": "Slapshot Transition"
            }}
        }},
        {{
            "prev_ver": 503382018,
            "name": "New BG",
            "uuid": "69e55fee-56ee-46b9-9fa4-8867d477d124",
            "id": "image_source",
            "versioned_id": "image_source",
            "settings": {{
                "file": "{pathin}/BG.png"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}},
            "filters": [
                {{
                    "prev_ver": 503382018,
                    "name": "Colour Correction",
                    "uuid": "9c17f0fb-2658-4cf4-b2ec-89511591a8f5",
                    "id": "color_filter",
                    "versioned_id": "color_filter_v2",
                    "settings": {{
                        "gamma": 0.60999999999999999,
                        "contrast": 1.8500000000000001,
                        "brightness": -0.0229,
                        "saturation": -1,
                        "opacity": 0.95279999999999998
                    }},
                    "mixers": 0,
                    "sync": 0,
                    "flags": 0,
                    "volume": 1.0,
                    "balance": 0.5,
                    "enabled": true,
                    "muted": false,
                    "push-to-mute": false,
                    "push-to-mute-delay": 0,
                    "push-to-talk": false,
                    "push-to-talk-delay": 0,
                    "hotkeys": {{}},
                    "deinterlace_mode": 0,
                    "deinterlace_field_order": 0,
                    "monitoring_type": 0,
                    "private_settings": {{}}
                }},
                {{
                    "prev_ver": 503382018,
                    "name": "Scroll",
                    "uuid": "06b16e67-89c4-43a8-bec2-9320c72fb487",
                    "id": "scroll_filter",
                    "versioned_id": "scroll_filter",
                    "settings": {{
                        "limit_cx": false,
                        "speed_x": 27
                    }},
                    "mixers": 0,
                    "sync": 0,
                    "flags": 0,
                    "volume": 1.0,
                    "balance": 0.5,
                    "enabled": true,
                    "muted": false,
                    "push-to-mute": false,
                    "push-to-mute-delay": 0,
                    "push-to-talk": false,
                    "push-to-talk-delay": 0,
                    "hotkeys": {{}},
                    "deinterlace_mode": 0,
                    "deinterlace_field_order": 0,
                    "monitoring_type": 0,
                    "private_settings": {{}}
                }}
            ]
        }},
        {{
            "prev_ver": 503382018,
            "name": "Statboard Base",
            "uuid": "47cf8808-e82a-4d24-ba0c-a8fbd219a5e0",
            "id": "image_source",
            "versioned_id": "image_source",
            "settings": {{
                "file": "{pathin}/Scoreboard Slap.png"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Donos",
            "uuid": "9e9e21e9-ae18-4acf-9b70-e2db08e2d3a6",
            "id": "browser_source",
            "versioned_id": "browser_source",
            "settings": {{
                "url": "https://streamelements.com/overlay/6324647667d2d2d7d03eb05f/8Ki994YhazshOBR44Gsv2GNzNsxOS8d2ex3mZGDlGZPufZUW",
                "width": 1920,
                "height": 1080,
                "fps": 30,
                "fps_custom": false,
                "shutdown": true,
                "restart_when_active": false,
                "webpage_control_level": 1,
                "css": "body {{ background-color: rgba(0, 0, 0, 0); margin: 0px auto; overflow: hidden; }}",
                "reroute_audio": true
            }},
            "mixers": 241,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.mute": [],
                "libobs.unmute": [],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": [],
                "ObsBrowser.Refresh": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "[NS] Overlays",
            "uuid": "040479cf-960d-42a7-abd2-d0c0999568a8",
            "id": "scene",
            "versioned_id": "scene",
            "settings": {{
                "custom_size": false,
                "id_counter": 1,
                "items": [
                    {{
                        "name": "Donos",
                        "source_uuid": "9e9e21e9-ae18-4acf-9b70-e2db08e2d3a6",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 1,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "OBSBasic.SelectScene": [],
                "libobs.show_scene_item.1": [],
                "libobs.hide_scene_item.1": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Lofi",
            "uuid": "556fe34e-e49d-48e0-8a68-ba2d83c3b8bb",
            "id": "vlc_source",
            "versioned_id": "vlc_source",
            "settings": {{
                "playlist": [
                    {{
                        "hidden": false,
                        "selected": false,
                        "value": "{pathin}/lofi-study-112191.mp3"
                    }},
                    {{
                        "hidden": false,
                        "selected": false,
                        "value": "{pathin}/notion-102693.mp3"
                    }}
                ],
                "loop": true,
                "shuffle": true,
                "playback_behavior": "stop_restart",
                "network_caching": 400,
                "track": 1,
                "subtitle_enable": false,
                "subtitle": 1
            }},
            "mixers": 241,
            "sync": 0,
            "flags": 0,
            "volume": 0.017516162246465683,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.mute": [],
                "libobs.unmute": [],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": [],
                "VLCSource.PlayPause": [],
                "VLCSource.Restart": [],
                "VLCSource.Stop": [],
                "VLCSource.PlaylistNext": [],
                "VLCSource.PlaylistPrev": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Shimmer",
            "uuid": "4aabbb42-00c7-468d-89c1-c4f62e6eb377",
            "id": "vlc_source",
            "versioned_id": "vlc_source",
            "settings": {{
                "playlist": [],
                "loop": true,
                "shuffle": false,
                "playback_behavior": "stop_restart",
                "network_caching": 400,
                "track": 1,
                "subtitle_enable": false,
                "subtitle": 1
            }},
            "mixers": 241,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.mute": [],
                "libobs.unmute": [],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": [],
                "VLCSource.PlayPause": [],
                "VLCSource.Restart": [],
                "VLCSource.Stop": [],
                "VLCSource.PlaylistNext": [],
                "VLCSource.PlaylistPrev": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{
                "mixer_hidden": true
            }},
            "filters": [
                {{
                    "prev_ver": 503382018,
                    "name": "Image Mask/Blend",
                    "uuid": "cdfa832f-3473-42dd-a24e-fd4e2e8f593b",
                    "id": "mask_filter",
                    "versioned_id": "mask_filter_v2",
                    "settings": {{
                        "image_path": "E:/!Videos Or Streaming/Streaming Stuff/OSL Stats/Statsheet/teams/gradient.png",
                        "stretch": false,
                        "type": "blend_mul_filter.effect",
                        "opacity": 1
                    }},
                    "mixers": 0,
                    "sync": 0,
                    "flags": 0,
                    "volume": 1.0,
                    "balance": 0.5,
                    "enabled": true,
                    "muted": false,
                    "push-to-mute": false,
                    "push-to-mute-delay": 0,
                    "push-to-talk": false,
                    "push-to-talk-delay": 0,
                    "hotkeys": {{}},
                    "deinterlace_mode": 0,
                    "deinterlace_field_order": 0,
                    "monitoring_type": 0,
                    "private_settings": {{}}
                }},
                {{
                    "prev_ver": 503382018,
                    "name": "Colour Correction",
                    "uuid": "9b3ed39d-2fc9-4987-90a7-dc3b6ec4bc1b",
                    "id": "color_filter",
                    "versioned_id": "color_filter_v2",
                    "settings": {{
                        "contrast": 0.19,
                        "saturation": -0.089999999999999997
                    }},
                    "mixers": 0,
                    "sync": 0,
                    "flags": 0,
                    "volume": 1.0,
                    "balance": 0.5,
                    "enabled": true,
                    "muted": false,
                    "push-to-mute": false,
                    "push-to-mute-delay": 0,
                    "push-to-talk": false,
                    "push-to-talk-delay": 0,
                    "hotkeys": {{}},
                    "deinterlace_mode": 0,
                    "deinterlace_field_order": 0,
                    "monitoring_type": 0,
                    "private_settings": {{}}
                }}
            ]
        }},
        {{
            "prev_ver": 503382018,
            "name": "[NS] Background",
            "uuid": "f3da34e6-1ba4-4980-a925-2639f7bda1cc",
            "id": "scene",
            "versioned_id": "scene",
            "settings": {{
                "custom_size": false,
                "id_counter": 11,
                "items": [
                    {{
                        "name": "New BG",
                        "source_uuid": "69e55fee-56ee-46b9-9fa4-8867d477d124",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 10,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "[NS] Replay",
                        "source_uuid": "0e959ed9-27a0-41f0-9215-ea77e658c791",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.3171232938766479,
                            "y": 1.3170732259750366
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 238,
                        "crop_top": 141,
                        "crop_right": 222,
                        "crop_bottom": 119,
                        "id": 9,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "OBSBasic.SelectScene": [],
                "libobs.show_scene_item.10": [],
                "libobs.hide_scene_item.10": [],
                "libobs.show_scene_item.9": [],
                "libobs.hide_scene_item.9": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}},
            "filters": [
                {{
                    "prev_ver": 503382018,
                    "name": "Image Mask/Blend",
                    "uuid": "2d490b43-56c7-401e-b0c5-ae492a2e7c85",
                    "id": "mask_filter",
                    "versioned_id": "mask_filter_v2",
                    "settings": {{
                        "image_path": "{gradient}",
                        "type": "blend_mul_filter.effect",
                        "opacity": 1
                    }},
                    "mixers": 0,
                    "sync": 0,
                    "flags": 0,
                    "volume": 1.0,
                    "balance": 0.5,
                    "enabled": true,
                    "muted": false,
                    "push-to-mute": false,
                    "push-to-mute-delay": 0,
                    "push-to-talk": false,
                    "push-to-talk-delay": 0,
                    "hotkeys": {{}},
                    "deinterlace_mode": 0,
                    "deinterlace_field_order": 0,
                    "monitoring_type": 0,
                    "private_settings": {{}}
                }}
            ]
        }},
        {{
            "prev_ver": 503382018,
            "name": "The Desk",
            "uuid": "b28f57f6-e365-4770-bd38-463c4110a120",
            "id": "scene",
            "versioned_id": "scene",
            "settings": {{
                "custom_size": false,
                "id_counter": 36,
                "items": [
                    {{
                        "name": "[NS] Background",
                        "source_uuid": "f3da34e6-1ba4-4980-a925-2639f7bda1cc",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 4,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Long score lol",
                        "source_uuid": "9542250f-bd68-4e80-a5c8-c34ab0924e76",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": -332.0,
                            "y": -69.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 9,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{
                            "collapsed": false
                        }}
                    }},
                    {{
                        "name": "Lofi",
                        "source_uuid": "556fe34e-e49d-48e0-8a68-ba2d83c3b8bb",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 12,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "[NS] Overlays",
                        "source_uuid": "040479cf-960d-42a7-abd2-d0c0999568a8",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 13,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "test",
                        "source_uuid": "b2f8ed2e-b1ad-47c2-8b25-97c93b4d18f7",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 759.0,
                            "y": 885.0
                        }},
                        "scale": {{
                            "x": 0.82988506555557251,
                            "y": 0.82999998331069946
                        }},
                        "align": 0,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 835.0,
                            "y": 276.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 14,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Frame Stack",
                        "source_uuid": "5ed26216-2d35-4f9f-b6f3-f70e18f66f83",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 15,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Caster Frame",
                        "source_uuid": "efe75205-f7f9-4f0f-9206-47408bf5ef08",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1446.0,
                            "y": 475.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 13,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Casters",
                        "source_uuid": "8d5d9598-e3c9-42d4-b072-8ecc0c0e89db",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1505.0,
                            "y": 600.0
                        }},
                        "scale": {{
                            "x": 1.0885714292526245,
                            "y": 1.0880000591278076
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 18,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Caster Setup",
                        "source_uuid": "4bb05f72-5ed2-4465-bf77-b7c92c741c46",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1446.0,
                            "y": 475.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 16,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{
                            "collapsed": false
                        }}
                    }},
                    {{
                        "name": "Discord Box Back",
                        "source_uuid": "f1c6105f-819f-442e-bc9f-23d1bed3be98",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1305.0,
                            "y": 921.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 16,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord Invite Link",
                        "source_uuid": "056ad710-8177-4fe4-ab8e-2e33c5cf7759",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1315.0,
                            "y": 932.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 17,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord Box Frame",
                        "source_uuid": "17b335cb-ddd9-43bf-8cd3-6b017b716816",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1305.0,
                            "y": 921.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 15,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord Link",
                        "source_uuid": "f2f5e807-beb9-4e3d-9d45-a287984599e9",
                        "visible": false,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1305.0,
                            "y": 921.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 17,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{
                            "collapsed": true
                        }}
                    }},
                    {{
                        "name": "Left Score",
                        "source_uuid": "81e2c3c8-eac6-416e-a2db-07aea7730030",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 515.0,
                            "y": 443.93701171875
                        }},
                        "scale": {{
                            "x": 0.7107195258140564,
                            "y": 0.70979022979736328
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 3,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Right Score",
                        "source_uuid": "680b1eed-2ea6-4111-ac9f-73838907eeb8",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 902.342041015625,
                            "y": 443.93701171875
                        }},
                        "scale": {{
                            "x": 0.7107195258140564,
                            "y": 0.70979022979736328
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 5,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Middle",
                        "source_uuid": "bee309be-495b-4a20-ad5e-fb4646875001",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 751.669677734375,
                            "y": 443.93701171875
                        }},
                        "scale": {{
                            "x": 0.7107195258140564,
                            "y": 0.70979022979736328
                        }},
                        "align": 4,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 6,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Best Of",
                        "source_uuid": "7139dd99-b8e9-4533-b13b-754ca06f72be",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 752.50897216796875,
                            "y": 433.99996948242188
                        }},
                        "scale": {{
                            "x": 0.7107195258140564,
                            "y": 0.70979022979736328
                        }},
                        "align": 0,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 21,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Scores",
                        "source_uuid": "07086113-4b0d-444a-bf60-40a5458b3677",
                        "visible": false,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 515.0,
                            "y": 390.7027587890625
                        }},
                        "scale": {{
                            "x": 0.7107195258140564,
                            "y": 0.70979022979736328
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 20,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{
                            "collapsed": false
                        }}
                    }},
                    {{
                        "name": "Right Logo",
                        "source_uuid": "96e8db6f-2029-460f-973e-aee47e99fc7c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1038.0,
                            "y": 267.0
                        }},
                        "scale": {{
                            "x": 0.4924999475479126,
                            "y": 0.49250000715255737
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 408.0,
                            "y": 374.5
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 21,
                        "group_item_backup": false,
                        "scale_filter": "bilinear",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Left Text",
                        "source_uuid": "b99d0e62-4d9a-40d6-a619-95df24f1f639",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 387.0,
                            "y": 692.0
                        }},
                        "scale": {{
                            "x": 3.8743946552276611,
                            "y": 3.875
                        }},
                        "align": 0,
                        "bounds_type": 6,
                        "bounds_align": 9,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 664.0,
                            "y": 110.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 22,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Right Text",
                        "source_uuid": "0367b2db-b567-44ce-8c90-1a4ca8850aca",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 804.0,
                            "y": 642.0
                        }},
                        "scale": {{
                            "x": 3.874394416809082,
                            "y": 3.875
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 10,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 621.45050048828125,
                            "y": 110.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 23,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Left Logo",
                        "source_uuid": "b31bc3c2-c8f8-4a0d-a423-04fdbabaa8c0",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 47.0,
                            "y": 269.5
                        }},
                        "scale": {{
                            "x": 0.38222211599349976,
                            "y": 0.3831990659236908
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 399.0,
                            "y": 367.5
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 24,
                        "group_item_backup": false,
                        "scale_filter": "bilinear",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "[NS] Overlays",
                        "source_uuid": "040479cf-960d-42a7-abd2-d0c0999568a8",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 25,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord",
                        "source_uuid": "a526dbdc-0cb6-4cdb-ac11-2e4828bde919",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 26,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Microphone",
                        "source_uuid": "3b69d9d9-97ea-4347-a7c1-3346e7dc542c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 27,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Super Saturday Ad",
                        "source_uuid": "658082aa-678c-4f5b-bf81-cd87c40fd6be",
                        "visible": false,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 469.5,
                            "y": 886.0
                        }},
                        "scale": {{
                            "x": 0.49583333730697632,
                            "y": 0.49532711505889893
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 36,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "id": "slide_transition",
                            "versioned_id": "slide_transition",
                            "name": "Super Saturday Ad Show Transition",
                            "transition": {{
                                "direction": "up"
                            }},
                            "duration": 500
                        }},
                        "hide_transition": {{
                            "id": "slide_transition",
                            "versioned_id": "slide_transition",
                            "name": "Super Saturday Ad Hide Transition",
                            "transition": {{
                                "direction": "down"
                            }},
                            "duration": 500
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "TickerBG",
                        "source_uuid": "c3b1a8ca-9df6-4ebc-84bf-5decc9b249e4",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 30,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Ticker Text",
                        "source_uuid": "50bcd47d-7a30-4206-bc09-732f141e585c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 199.39999389648438,
                            "y": 1019.0
                        }},
                        "scale": {{
                            "x": 0.85850000381469727,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 32,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Ticker",
                        "source_uuid": "03531d4f-e2b0-4503-b2c0-8e0c2db3c9b6",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 28,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{
                            "collapsed": false
                        }}
                    }},
                    {{
                        "name": "Audio Output Capture",
                        "source_uuid": "d52a078b-9ed9-44f5-b01b-646b27b77768",
                        "visible": false,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 33,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Display Capture 2",
                        "source_uuid": "940fb243-3f08-42a4-804f-ffdee50a21df",
                        "visible": false,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1920.0,
                            "y": 1080.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 34,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "OBSBasic.SelectScene": [
                    {{
                        "key": "OBS_KEY_NUM1"
                    }}
                ],
                "libobs.show_scene_item.4": [],
                "libobs.hide_scene_item.4": [],
                "libobs.show_scene_item.9": [],
                "libobs.hide_scene_item.9": [],
                "libobs.show_scene_item.12": [],
                "libobs.hide_scene_item.12": [],
                "libobs.show_scene_item.13": [],
                "libobs.hide_scene_item.13": [],
                "libobs.show_scene_item.14": [],
                "libobs.hide_scene_item.14": [],
                "libobs.show_scene_item.15": [],
                "libobs.hide_scene_item.15": [],
                "libobs.show_scene_item.16": [],
                "libobs.hide_scene_item.16": [],
                "libobs.show_scene_item.17": [],
                "libobs.hide_scene_item.17": [],
                "libobs.show_scene_item.20": [],
                "libobs.hide_scene_item.20": [],
                "libobs.show_scene_item.21": [],
                "libobs.hide_scene_item.21": [],
                "libobs.show_scene_item.22": [],
                "libobs.hide_scene_item.22": [],
                "libobs.show_scene_item.23": [],
                "libobs.hide_scene_item.23": [],
                "libobs.show_scene_item.24": [],
                "libobs.hide_scene_item.24": [],
                "libobs.show_scene_item.25": [],
                "libobs.hide_scene_item.25": [],
                "libobs.show_scene_item.26": [],
                "libobs.hide_scene_item.26": [],
                "libobs.show_scene_item.27": [],
                "libobs.hide_scene_item.27": [],
                "libobs.show_scene_item.28": [],
                "libobs.hide_scene_item.28": [],
                "libobs.show_scene_item.33": [],
                "libobs.hide_scene_item.33": [],
                "libobs.show_scene_item.34": [],
                "libobs.hide_scene_item.34": [],
                "libobs.show_scene_item.36": [],
                "libobs.hide_scene_item.36": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Stats",
            "uuid": "2f7d8054-2c49-4c8c-b516-e30420c58504",
            "id": "scene",
            "versioned_id": "scene",
            "settings": {{
                "custom_size": false,
                "id_counter": 36,
                "items": [
                    {{
                        "name": "Stats and Teams",
                        "source_uuid": "0d0df9bf-873f-4135-afdb-32839f403aee",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 29,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "[NS] Background",
                        "source_uuid": "f3da34e6-1ba4-4980-a925-2639f7bda1cc",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 6,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Nested",
                        "source_uuid": "20af7571-0bed-4550-a3f8-77ae99188b0f",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 8,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{
                            "collapsed": false
                        }}
                    }},
                    {{
                        "name": "[NS] Overlays",
                        "source_uuid": "040479cf-960d-42a7-abd2-d0c0999568a8",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 14,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Left Logo",
                        "source_uuid": "b31bc3c2-c8f8-4a0d-a423-04fdbabaa8c0",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 20.0,
                            "y": 20.0
                        }},
                        "scale": {{
                            "x": 0.29555556178092957,
                            "y": 0.29574224352836609
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 418.0,
                            "y": 271.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 21,
                        "group_item_backup": false,
                        "scale_filter": "bilinear",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Right Logo",
                        "source_uuid": "96e8db6f-2029-460f-973e-aee47e99fc7c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1482.0,
                            "y": 20.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 418.0,
                            "y": 271.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 22,
                        "group_item_backup": false,
                        "scale_filter": "bilinear",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "StatBoardBrowser",
                        "source_uuid": "7154e16e-f452-452e-abd0-9a547bb34d00",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 210.0,
                            "y": 190.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 35,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Left Score",
                        "source_uuid": "81e2c3c8-eac6-416e-a2db-07aea7730030",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 804.24737548828125,
                            "y": 51.139850616455078
                        }},
                        "scale": {{
                            "x": 0.46842879056930542,
                            "y": 0.46853145956993103
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 3,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Right Score",
                        "source_uuid": "680b1eed-2ea6-4111-ac9f-73838907eeb8",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1059.541015625,
                            "y": 51.139850616455078
                        }},
                        "scale": {{
                            "x": 0.46842879056930542,
                            "y": 0.46853145956993103
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 5,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Middle",
                        "source_uuid": "bee309be-495b-4a20-ad5e-fb4646875001",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 960.2342529296875,
                            "y": 51.139850616455078
                        }},
                        "scale": {{
                            "x": 0.46842879056930542,
                            "y": 0.46853145956993103
                        }},
                        "align": 4,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 6,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Best Of",
                        "source_uuid": "7139dd99-b8e9-4533-b13b-754ca06f72be",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 960.787353515625,
                            "y": 44.580413818359375
                        }},
                        "scale": {{
                            "x": 0.46842879056930542,
                            "y": 0.46853145956993103
                        }},
                        "align": 0,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 21,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Scores",
                        "source_uuid": "07086113-4b0d-444a-bf60-40a5458b3677",
                        "visible": false,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 804.24737548828125,
                            "y": 15.999992370605469
                        }},
                        "scale": {{
                            "x": 0.46842879056930542,
                            "y": 0.46853145956993103
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 25,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{
                            "collapsed": false
                        }}
                    }},
                    {{
                        "name": "[NS] Overlays",
                        "source_uuid": "040479cf-960d-42a7-abd2-d0c0999568a8",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 30,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord",
                        "source_uuid": "a526dbdc-0cb6-4cdb-ac11-2e4828bde919",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 33,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Microphone",
                        "source_uuid": "3b69d9d9-97ea-4347-a7c1-3346e7dc542c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 32,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "TickerBG",
                        "source_uuid": "c3b1a8ca-9df6-4ebc-84bf-5decc9b249e4",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 30,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Ticker Text",
                        "source_uuid": "50bcd47d-7a30-4206-bc09-732f141e585c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 199.39999389648438,
                            "y": 1019.0
                        }},
                        "scale": {{
                            "x": 0.85850000381469727,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 32,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Ticker",
                        "source_uuid": "03531d4f-e2b0-4503-b2c0-8e0c2db3c9b6",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 36,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "OBSBasic.SelectScene": [
                    {{
                        "key": "OBS_KEY_NUM3"
                    }}
                ],
                "libobs.show_scene_item.29": [],
                "libobs.hide_scene_item.29": [],
                "libobs.show_scene_item.8": [],
                "libobs.hide_scene_item.8": [],
                "libobs.show_scene_item.14": [],
                "libobs.hide_scene_item.14": [],
                "libobs.show_scene_item.21": [],
                "libobs.hide_scene_item.21": [],
                "libobs.show_scene_item.22": [],
                "libobs.hide_scene_item.22": [],
                "libobs.show_scene_item.35": [],
                "libobs.hide_scene_item.35": [],
                "libobs.show_scene_item.25": [],
                "libobs.hide_scene_item.25": [],
                "libobs.show_scene_item.30": [],
                "libobs.hide_scene_item.30": [],
                "libobs.show_scene_item.33": [],
                "libobs.hide_scene_item.33": [],
                "libobs.show_scene_item.32": [],
                "libobs.hide_scene_item.32": [],
                "libobs.show_scene_item.36": [],
                "libobs.hide_scene_item.36": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{
                "transition": ""
            }}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Loading",
            "uuid": "05ea4073-6efc-4708-a1f6-c178c80b1f74",
            "id": "scene",
            "versioned_id": "scene",
            "settings": {{
                "custom_size": false,
                "id_counter": 18,
                "items": [
                    {{
                        "name": "Lofi",
                        "source_uuid": "556fe34e-e49d-48e0-8a68-ba2d83c3b8bb",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 7,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Slap load",
                        "source_uuid": "369ff9dd-149f-463c-8f67-bcb919613b85",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 11,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "[NS] Overlays",
                        "source_uuid": "040479cf-960d-42a7-abd2-d0c0999568a8",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 15,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Countdown",
                        "source_uuid": "6bb6d370-92d0-4b2e-a400-783c5f623e38",
                        "visible": false,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 748.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 16,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "OBSBasic.SelectScene": [],
                "libobs.show_scene_item.7": [],
                "libobs.hide_scene_item.7": [],
                "libobs.show_scene_item.11": [],
                "libobs.hide_scene_item.11": [],
                "libobs.show_scene_item.15": [],
                "libobs.hide_scene_item.15": [],
                "libobs.show_scene_item.16": [],
                "libobs.hide_scene_item.16": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "[NS] Game Score",
            "uuid": "cfdc3784-b6ea-45f3-af15-cbadd4e75836",
            "id": "scene",
            "versioned_id": "scene",
            "settings": {{
                "custom_size": false,
                "id_counter": 32,
                "items": [
                    {{
                        "name": "ScoreBack",
                        "source_uuid": "90c73104-8759-475a-a52f-11dc626da959",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 506.000244140625,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 27,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "ScoreFront",
                        "source_uuid": "b9d25a44-5905-4a2f-a156-b7315330424a",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 506.000244140625,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 28,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Background",
                        "source_uuid": "c090dfd8-4311-495c-8cff-13571d009647",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 506.000244140625,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.8010417222976685,
                            "y": 1.8012346029281616
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 12,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{
                            "collapsed": false
                        }}
                    }},
                    {{
                        "name": "Left Logo",
                        "source_uuid": "b31bc3c2-c8f8-4a0d-a423-04fdbabaa8c0",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 740.86895751953125,
                            "y": 6.4516129493713379
                        }},
                        "scale": {{
                            "x": 0.098653338849544525,
                            "y": 0.098890095949172974
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 399.0,
                            "y": 365.625
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 1,
                        "group_item_backup": true,
                        "scale_filter": "bilinear",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Right Logo",
                        "source_uuid": "96e8db6f-2029-460f-973e-aee47e99fc7c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1074.598388671875,
                            "y": 5.9354839324951172
                        }},
                        "scale": {{
                            "x": 0.12711659073829651,
                            "y": 0.12709677219390869
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 408.0,
                            "y": 351.625
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 2,
                        "group_item_backup": true,
                        "scale_filter": "bilinear",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Left Text",
                        "source_uuid": "b99d0e62-4d9a-40d6-a619-95df24f1f639",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 790.1669921875,
                            "y": 113.03225708007812
                        }},
                        "scale": {{
                            "x": 0.99999964237213135,
                            "y": 1.0
                        }},
                        "align": 0,
                        "bounds_type": 6,
                        "bounds_align": 8,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1230.130615234375,
                            "y": 110.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 29,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Right Text",
                        "source_uuid": "0367b2db-b567-44ce-8c90-1a4ca8850aca",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 971.098388671875,
                            "y": 99.096771240234375
                        }},
                        "scale": {{
                            "x": 0.99999958276748657,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 8,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1235.551025390625,
                            "y": 110.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 30,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Elements",
                        "source_uuid": "096ecadd-bef5-4341-8bf3-190ad7384771",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 631.43255615234375,
                            "y": 5.9354839324951172
                        }},
                        "scale": {{
                            "x": 0.25810474157333374,
                            "y": 0.25806450843811035
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 9,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{
                            "collapsed": false
                        }}
                    }},
                    {{
                        "name": "Left Score",
                        "source_uuid": "81e2c3c8-eac6-416e-a2db-07aea7730030",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 868.0,
                            "y": 32.716781616210938
                        }},
                        "scale": {{
                            "x": 0.2760646641254425,
                            "y": 0.27622374892234802
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 3,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Right Score",
                        "source_uuid": "680b1eed-2ea6-4111-ac9f-73838907eeb8",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1018.4552001953125,
                            "y": 32.716781616210938
                        }},
                        "scale": {{
                            "x": 0.2760646641254425,
                            "y": 0.27622374892234802
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 5,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Middle",
                        "source_uuid": "bee309be-495b-4a20-ad5e-fb4646875001",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 959.9295654296875,
                            "y": 32.716781616210938
                        }},
                        "scale": {{
                            "x": 0.2760646641254425,
                            "y": 0.27622374892234802
                        }},
                        "align": 4,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 6,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Best Of",
                        "source_uuid": "7139dd99-b8e9-4533-b13b-754ca06f72be",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 960.25555419921875,
                            "y": 28.849649429321289
                        }},
                        "scale": {{
                            "x": 0.2760646641254425,
                            "y": 0.27622374892234802
                        }},
                        "align": 0,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 21,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Scores",
                        "source_uuid": "07086113-4b0d-444a-bf60-40a5458b3677",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 868.0,
                            "y": 12.0
                        }},
                        "scale": {{
                            "x": 0.2760646641254425,
                            "y": 0.27622374892234802
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 10,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{
                            "collapsed": false
                        }}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "OBSBasic.SelectScene": [],
                "libobs.show_scene_item.12": [],
                "libobs.hide_scene_item.12": [],
                "libobs.show_scene_item.9": [],
                "libobs.hide_scene_item.9": [],
                "libobs.show_scene_item.10": [],
                "libobs.hide_scene_item.10": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Left Logo",
            "uuid": "b31bc3c2-c8f8-4a0d-a423-04fdbabaa8c0",
            "id": "image_source",
            "versioned_id": "image_source",
            "settings": {{
                "file": "{pathin}/logoHome.png",
                "unload": false,
                "linear_alpha": false
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Right Logo",
            "uuid": "96e8db6f-2029-460f-973e-aee47e99fc7c",
            "id": "image_source",
            "versioned_id": "image_source",
            "settings": {{
                "file": "{pathin}/logoAway.png",
                "unload": false,
                "linear_alpha": false
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Left Score",
            "uuid": "81e2c3c8-eac6-416e-a2db-07aea7730030",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "outline": false,
                "read_from_file": true,
                "text": "2",
                "undo_sname": "Left Score",
                "file": "{pathin}/scoreHome.txt",
                "font": {{
                    "face": "Century Gothic",
                    "flags": 0,
                    "size": 256,
                    "style": "Regular"
                }},
                "outline_size": 7,
                "outline_color": 4278190080
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Right Score",
            "uuid": "680b1eed-2ea6-4111-ac9f-73838907eeb8",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "chatlog": false,
                "extents": false,
                "outline": false,
                "read_from_file": true,
                "text": "10000",
                "undo_sname": "Right Score",
                "file": "{pathin}/scoreAway.txt",
                "font": {{
                    "face": "Century Gothic",
                    "flags": 0,
                    "size": 256,
                    "style": "Regular"
                }},
                "outline_size": 7,
                "outline_color": 4278190080,
                "antialiasing": true
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Middle",
            "uuid": "bee309be-495b-4a20-ad5e-fb4646875001",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "outline": false,
                "text": "-",
                "font": {{
                    "face": "Century Gothic",
                    "flags": 0,
                    "size": 256,
                    "style": "Regular"
                }},
                "outline_size": 7,
                "outline_color": 4278190080
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "[NS] Statboard",
            "uuid": "ca1c3607-49dd-45f6-8576-c55ac527c651",
            "id": "scene",
            "versioned_id": "scene",
            "settings": {{
                "custom_size": false,
                "id_counter": 36,
                "items": [
                    {{
                        "name": "Statboard Base",
                        "source_uuid": "47cf8808-e82a-4d24-ba0c-a8fbd219a5e0",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 665.97308349609375,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 666,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 14,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "StatBoardBrowser",
                        "source_uuid": "7154e16e-f452-452e-abd0-9a547bb34d00",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 210.0,
                            "y": 255.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 36,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "OBSBasic.SelectScene": [],
                "libobs.show_scene_item.14": [],
                "libobs.hide_scene_item.14": [],
                "libobs.show_scene_item.36": [],
                "libobs.hide_scene_item.36": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "[NS] Casters",
            "uuid": "dd2384f2-73e0-4962-a381-e5c0202097d1",
            "id": "scene",
            "versioned_id": "scene",
            "settings": {{
                "custom_size": false,
                "id_counter": 19,
                "items": [
                    {{
                        "name": "Caster Frame",
                        "source_uuid": "efe75205-f7f9-4f0f-9206-47408bf5ef08",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 32.0,
                            "y": 591.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 13,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Casters",
                        "source_uuid": "8d5d9598-e3c9-42d4-b072-8ecc0c0e89db",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 91.0,
                            "y": 716.0
                        }},
                        "scale": {{
                            "x": 1.0885714292526245,
                            "y": 1.0880000591278076
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 18,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Caster Setup",
                        "source_uuid": "4bb05f72-5ed2-4465-bf77-b7c92c741c46",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 32.0,
                            "y": 591.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 12,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{
                            "collapsed": false
                        }}
                    }},
                    {{
                        "name": "Discord Box Back",
                        "source_uuid": "f1c6105f-819f-442e-bc9f-23d1bed3be98",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 16,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord Invite Link",
                        "source_uuid": "056ad710-8177-4fe4-ab8e-2e33c5cf7759",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 10.0,
                            "y": 11.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 17,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord Box Frame",
                        "source_uuid": "17b335cb-ddd9-43bf-8cd3-6b017b716816",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 15,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord Link",
                        "source_uuid": "f2f5e807-beb9-4e3d-9d45-a287984599e9",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 14,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{
                            "collapsed": true
                        }}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "OBSBasic.SelectScene": [],
                "libobs.show_scene_item.12": [],
                "libobs.hide_scene_item.12": [],
                "libobs.show_scene_item.14": [],
                "libobs.hide_scene_item.14": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Highlights",
            "uuid": "cf79c840-b86f-4b49-9612-1bbf51659cf3",
            "id": "vlc_source",
            "versioned_id": "vlc_source",
            "settings": {{
                "playlist": [
                    {{
                        "hidden": false,
                        "selected": false,
                        "value": "{pathin}/BG01.mp4"
                    }},
                    {{
                        "hidden": false,
                        "selected": false,
                        "value": "{pathin}/BG02.mp4"
                    }},
                    {{
                        "hidden": false,
                        "selected": false,
                        "value": "{pathin}/BG03.mp4"
                    }},
                    {{
                        "hidden": false,
                        "selected": false,
                        "value": "{pathin}/BG04.mp4"
                    }},
                    {{
                        "hidden": false,
                        "selected": false,
                        "value": "{pathin}/BG05.mp4"
                    }},
                    {{
                        "hidden": false,
                        "selected": false,
                        "value": "{pathin}/BG06.mp4"
                    }},
                    {{
                        "hidden": false,
                        "selected": false,
                        "value": "{pathin}/BG07.mp4"
                    }},
                    {{
                        "hidden": false,
                        "selected": false,
                        "value": "{pathin}/BG08.mp4"
                    }},
                    {{
                        "hidden": false,
                        "selected": false,
                        "value": "{pathin}/BG09.mp4"
                    }},
                    {{
                        "hidden": false,
                        "selected": false,
                        "value": "{pathin}/BG10.mp4"
                    }}
                ],
                "loop": true,
                "shuffle": true,
                "playback_behavior": "stop_restart",
                "network_caching": 400,
                "track": 1,
                "subtitle_enable": false,
                "subtitle": 1
            }},
            "mixers": 241,
            "sync": 0,
            "flags": 0,
            "volume": 0.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.mute": [],
                "libobs.unmute": [],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": [],
                "VLCSource.PlayPause": [],
                "VLCSource.Restart": [],
                "VLCSource.Stop": [],
                "VLCSource.PlaylistNext": [],
                "VLCSource.PlaylistPrev": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{
                "mixer_hidden": false
            }}
        }},
        {{
            "prev_ver": 503382018,
            "name": "[NS] Replay",
            "uuid": "0e959ed9-27a0-41f0-9215-ea77e658c791",
            "id": "scene",
            "versioned_id": "scene",
            "settings": {{
                "custom_size": false,
                "id_counter": 1,
                "items": [
                    {{
                        "name": "Highlights",
                        "source_uuid": "cf79c840-b86f-4b49-9612-1bbf51659cf3",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 1,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "OBSBasic.SelectScene": [],
                "libobs.show_scene_item.1": [],
                "libobs.hide_scene_item.1": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}},
            "filters": [
                {{
                    "prev_ver": 503382018,
                    "name": "Colour Correction",
                    "uuid": "648faeb0-392e-4642-95a4-888f0c149657",
                    "id": "color_filter",
                    "versioned_id": "color_filter_v2",
                    "settings": {{
                        "saturation": -1,
                        "opacity": 0.31979999999999997
                    }},
                    "mixers": 0,
                    "sync": 0,
                    "flags": 0,
                    "volume": 1.0,
                    "balance": 0.5,
                    "enabled": true,
                    "muted": false,
                    "push-to-mute": false,
                    "push-to-mute-delay": 0,
                    "push-to-talk": false,
                    "push-to-talk-delay": 0,
                    "hotkeys": {{}},
                    "deinterlace_mode": 0,
                    "deinterlace_field_order": 0,
                    "monitoring_type": 0,
                    "private_settings": {{}}
                }}
            ]
        }},
        {{
            "prev_ver": 503382018,
            "name": "Best Of",
            "uuid": "7139dd99-b8e9-4533-b13b-754ca06f72be",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "outline": false,
                "text": "BO3",
                "undo_sname": "Best Of",
                "font": {{
                    "face": "Century Gothic",
                    "flags": 0,
                    "size": 120,
                    "style": "Regular"
                }},
                "align": "left",
                "valign": "top",
                "color": 16777215,
                "opacity": 100,
                "gradient_color": 16777215,
                "gradient_opacity": 100,
                "gradient_dir": 90,
                "bk_color": 0,
                "bk_opacity": 0,
                "outline_size": 7,
                "outline_color": 4278190080,
                "outline_opacity": 100,
                "chatlog_lines": 6,
                "extents_wrap": true,
                "extents_cx": 100,
                "extents_cy": 100,
                "transform": 0,
                "antialiasing": true
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Slap load",
            "uuid": "369ff9dd-149f-463c-8f67-bcb919613b85",
            "id": "ffmpeg_source",
            "versioned_id": "ffmpeg_source",
            "settings": {{
                "local_file": "{pathin}/Loading Screen.mp4",
                "is_local_file": true,
                "looping": true,
                "clear_on_media_end": true,
                "restart_on_activate": true,
                "linear_alpha": false,
                "reconnect_delay_sec": 10,
                "buffering_mb": 2,
                "speed_percent": 100
            }},
            "mixers": 241,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.mute": [],
                "libobs.unmute": [],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": [],
                "MediaSource.Restart": [],
                "MediaSource.Play": [],
                "MediaSource.Pause": [],
                "MediaSource.Stop": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{
                "mixer_hidden": false
            }}
        }},
        {{
            "prev_ver": 503382018,
            "name": "test",
            "uuid": "b2f8ed2e-b1ad-47c2-8b25-97c93b4d18f7",
            "id": "browser_source",
            "versioned_id": "browser_source",
            "settings": {{
                "url": "https://streamlabs.com/widgets/poll/97271910EE3485805C6D",
                "width": 700,
                "height": 370
            }},
            "mixers": 241,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.mute": [],
                "libobs.unmute": [],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": [],
                "ObsBrowser.Refresh": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Display Cap",
            "uuid": "c282f0fc-bd1d-4708-bf26-6a9e89e59243",
            "id": "scene",
            "versioned_id": "scene",
            "settings": {{
                "custom_size": false,
                "id_counter": 4,
                "items": [
                    {{
                        "name": "Display Capture",
                        "source_uuid": "b65a11bb-84f1-4ff8-be42-94bd0704117f",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1920.0,
                            "y": 1080.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 1,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "[NS] Overlays",
                        "source_uuid": "040479cf-960d-42a7-abd2-d0c0999568a8",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 2,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord",
                        "source_uuid": "a526dbdc-0cb6-4cdb-ac11-2e4828bde919",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 3,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Microphone",
                        "source_uuid": "3b69d9d9-97ea-4347-a7c1-3346e7dc542c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 4,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "OBSBasic.SelectScene": [],
                "libobs.show_scene_item.1": [],
                "libobs.hide_scene_item.1": [],
                "libobs.show_scene_item.2": [],
                "libobs.hide_scene_item.2": [],
                "libobs.show_scene_item.3": [],
                "libobs.hide_scene_item.3": [],
                "libobs.show_scene_item.4": [],
                "libobs.hide_scene_item.4": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Display Capture",
            "uuid": "b65a11bb-84f1-4ff8-be42-94bd0704117f",
            "id": "monitor_capture",
            "versioned_id": "monitor_capture",
            "settings": {{
                "monitor": 1,
                "monitor_id": "\\\\?\\DISPLAY#AOC2702#5&d4bdda8&0&UID176389#{{e6f07b5f-ee97-4a90-b076-33f57bf4eaa7}}"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Caster Frame",
            "uuid": "efe75205-f7f9-4f0f-9206-47408bf5ef08",
            "id": "image_source",
            "versioned_id": "image_source",
            "settings": {{
                "file": "{pathin}/Caster Box.png"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Discord Box Frame",
            "uuid": "17b335cb-ddd9-43bf-8cd3-6b017b716816",
            "id": "image_source",
            "versioned_id": "image_source",
            "settings": {{
                "file": "{pathin}/OSL Discord Border.png"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Discord Box Back",
            "uuid": "f1c6105f-819f-442e-bc9f-23d1bed3be98",
            "id": "image_source",
            "versioned_id": "image_source",
            "settings": {{
                "file": "{pathin}/OSL Discord Back.png"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Discord Invite Link",
            "uuid": "056ad710-8177-4fe4-ab8e-2e33c5cf7759",
            "id": "browser_source",
            "versioned_id": "browser_source",
            "settings": {{
                "url": "https://streamkit.discord.com/overlay/status/555292959516393482?icon=true&online=true&logo=white&text_color=%23ffffff&text_size=14&text_outline_color=%23000000&text_outline_size=0&text_shadow_color=%23000000&text_shadow_size=0&bg_color=%231e2124&bg_opacity=0&bg_shadow_color=%23000000&bg_shadow_size=0&invite_code=osl&limit_speaking=false&small_avatars=false&hide_names=false&fade_chat=0",
                "width": 312,
                "height": 64
            }},
            "mixers": 241,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.mute": [],
                "libobs.unmute": [],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": [],
                "ObsBrowser.Refresh": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Casters",
            "uuid": "8d5d9598-e3c9-42d4-b072-8ecc0c0e89db",
            "id": "browser_source",
            "versioned_id": "browser_source",
            "settings": {{
                "url": "https://streamkit.discord.com/overlay/voice/555292959516393482/709943422248550401?icon=true&online=true&logo=white&text_color=%23ffffff&text_size=14&text_outline_color=%23000000&text_outline_size=0&text_shadow_color=%23000000&text_shadow_size=0&bg_color=%231e2124&bg_opacity=0.95&bg_shadow_color=%23000000&bg_shadow_size=0&invite_code=osl&limit_speaking=false&small_avatars=false&hide_names=false&fade_chat=0",
                "width": 350,
                "height": 500,
                "css": ".voice-container .voice-states .voice-state .avatar{{\nli.voice-state:not([data-reactid=\"\"]) {{ display:none; }}\n;\n  height: 50px;\n  width: 50px;\n  border-radius:15% !important;\n  filter: brightness(50%); \n/Change brightness to 100%, if you don’t want the image to dim/\n}}\n.speaking {{\n  border-color:rgba(100,255,100,255) !important;\n  position:relative;\n  animation-name: speak-now;\n  animation-duration: 1s;\n  animation-timing-function: ease;\n  animation-fill-mode:both;\n  filter: brightness(100%) !important;\n}}\n.voice-container {{position: fixed; height: 100%;}}\n.voice-states {{position: absolute; width: 600px;}}\n.voice-container .voice-states .voice-state .user {{\n    padding-top: 20px;\n}}\n.voice-container .voice-states .voice-state {{ height: 40px; margin-bottom: 28px}}\n@keyframes speak-now {{\n  0% {{ bottom:0px;  }}\n  100% {{ Transform:translateX(3%);}}\nli.voice-state{{ position: static; }}\ndiv.user{{ position: static;}}\nbody {{ background-color: rgba(0, 0, 0, 0); margin: 0px auto; overflow: hidden; }}\n\n"
            }},
            "mixers": 192,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.mute": [],
                "libobs.unmute": [],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": [],
                "ObsBrowser.Refresh": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Frame Stack",
            "uuid": "5ed26216-2d35-4f9f-b6f3-f70e18f66f83",
            "id": "image_source",
            "versioned_id": "image_source",
            "settings": {{
                "file": "{pathin}/Frame Banner.png"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Left Text",
            "uuid": "b99d0e62-4d9a-40d6-a619-95df24f1f639",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "drop_shadow": true,
                "file": "{pathin}/nameHome.txt",
                "from_file": true,
                "outline": false,
                "read_from_file": true,
                "text": "",
                "text_file": "E:/!Videos Or Streaming/Streaming Stuff/OSL Stats/Statsheet/teams/leftTeam/teamName.txt",
                "font": {{
                    "face": "Century Gothic",
                    "flags": 0,
                    "size": 100,
                    "style": "Regular"
                }}
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}},
            "filters": [
                {{
                    "prev_ver": 503382018,
                    "name": "Image Mask/Blend",
                    "uuid": "a2534877-c433-4e0e-8a8a-81b8f841aa9e",
                    "id": "mask_filter",
                    "versioned_id": "mask_filter_v2",
                    "settings": {{
                        "image_path": "{colourHome}",
                        "type": "blend_mul_filter.effect"
                    }},
                    "mixers": 0,
                    "sync": 0,
                    "flags": 0,
                    "volume": 1.0,
                    "balance": 0.5,
                    "enabled": true,
                    "muted": false,
                    "push-to-mute": false,
                    "push-to-mute-delay": 0,
                    "push-to-talk": false,
                    "push-to-talk-delay": 0,
                    "hotkeys": {{}},
                    "deinterlace_mode": 0,
                    "deinterlace_field_order": 0,
                    "monitoring_type": 0,
                    "private_settings": {{}}
                }}
            ]
        }},
        {{
            "prev_ver": 503382018,
            "name": "Right Text",
            "uuid": "0367b2db-b567-44ce-8c90-1a4ca8850aca",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "drop_shadow": true,
                "file": "{pathin}/nameAway.txt",
                "from_file": true,
                "outline": false,
                "read_from_file": true,
                "text_file": "E:/!Videos Or Streaming/Streaming Stuff/OSL Stats/Statsheet/teams/rightTeam/teamName.txt",
                "text": "",
                "undo_sname": "Right Text",
                "font": {{
                    "face": "Century Gothic",
                    "flags": 0,
                    "size": 100,
                    "style": "Regular"
                }}
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}},
            "filters": [
                {{
                    "prev_ver": 503382018,
                    "name": "Image Mask/Blend",
                    "uuid": "2b4eda3f-2ffb-456a-b3a3-9513f2752e4f",
                    "id": "mask_filter",
                    "versioned_id": "mask_filter_v2",
                    "settings": {{
                        "image_path": "{colourAway}",
                        "type": "blend_mul_filter.effect"
                    }},
                    "mixers": 0,
                    "sync": 0,
                    "flags": 0,
                    "volume": 1.0,
                    "balance": 0.5,
                    "enabled": true,
                    "muted": false,
                    "push-to-mute": false,
                    "push-to-mute-delay": 0,
                    "push-to-talk": false,
                    "push-to-talk-delay": 0,
                    "hotkeys": {{}},
                    "deinterlace_mode": 0,
                    "deinterlace_field_order": 0,
                    "monitoring_type": 0,
                    "private_settings": {{}}
                }}
            ]
        }},
        {{
            "prev_ver": 503382018,
            "name": "Stats and Teams",
            "uuid": "0d0df9bf-873f-4135-afdb-32839f403aee",
            "id": "vlc_source",
            "versioned_id": "vlc_source",
            "settings": {{
                "playlist": [
                    {{
                        "value": "{pathin}/Bunger Verse Loop.mp3",
                        "selected": false,
                        "hidden": false
                    }}
                ],
                "shuffle": true
            }},
            "mixers": 241,
            "sync": 0,
            "flags": 0,
            "volume": 0.078556627035140991,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.mute": [],
                "libobs.unmute": [],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": [],
                "VLCSource.PlayPause": [],
                "VLCSource.Restart": [],
                "VLCSource.Stop": [],
                "VLCSource.PlaylistNext": [],
                "VLCSource.PlaylistPrev": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Schedule PostGame",
            "uuid": "d46b5746-cf73-41da-aed4-4e0468690021",
            "id": "scene",
            "versioned_id": "scene",
            "settings": {{
                "custom_size": false,
                "id_counter": 13,
                "items": [
                    {{
                        "name": "Stats and Teams",
                        "source_uuid": "0d0df9bf-873f-4135-afdb-32839f403aee",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 8,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "[NS] Background",
                        "source_uuid": "f3da34e6-1ba4-4980-a925-2639f7bda1cc",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 1,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Schedule BG",
                        "source_uuid": "3a7f77d5-dc40-44c8-9538-403167511477",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 907,
                        "id": 2,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Caster Frame",
                        "source_uuid": "efe75205-f7f9-4f0f-9206-47408bf5ef08",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1504.0,
                            "y": 721.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 13,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Casters",
                        "source_uuid": "8d5d9598-e3c9-42d4-b072-8ecc0c0e89db",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1563.0,
                            "y": 846.0
                        }},
                        "scale": {{
                            "x": 1.0885714292526245,
                            "y": 1.0880000591278076
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 18,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Caster Setup",
                        "source_uuid": "4bb05f72-5ed2-4465-bf77-b7c92c741c46",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1504.0,
                            "y": 721.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 3,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{
                            "collapsed": true
                        }}
                    }},
                    {{
                        "name": "Discord Box Back",
                        "source_uuid": "f1c6105f-819f-442e-bc9f-23d1bed3be98",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 20.0,
                            "y": 912.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 16,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord Invite Link",
                        "source_uuid": "056ad710-8177-4fe4-ab8e-2e33c5cf7759",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 30.0,
                            "y": 923.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 17,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord Box Frame",
                        "source_uuid": "17b335cb-ddd9-43bf-8cd3-6b017b716816",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 20.0,
                            "y": 912.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 15,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord Link",
                        "source_uuid": "f2f5e807-beb9-4e3d-9d45-a287984599e9",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 20.0,
                            "y": 912.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 4,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{
                            "collapsed": true
                        }}
                    }},
                    {{
                        "name": "[NS] Overlays",
                        "source_uuid": "040479cf-960d-42a7-abd2-d0c0999568a8",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 9,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "test",
                        "source_uuid": "b2f8ed2e-b1ad-47c2-8b25-97c93b4d18f7",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 743.0,
                            "y": 820.0
                        }},
                        "scale": {{
                            "x": 0.65142858028411865,
                            "y": 0.65135133266448975
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 10,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord",
                        "source_uuid": "a526dbdc-0cb6-4cdb-ac11-2e4828bde919",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 11,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Microphone",
                        "source_uuid": "3b69d9d9-97ea-4347-a7c1-3346e7dc542c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 12,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Browser",
                        "source_uuid": "22c6eb60-8391-48a1-807c-d0a5d1ece151",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 213.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 13,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "OBSBasic.SelectScene": [],
                "libobs.show_scene_item.8": [],
                "libobs.hide_scene_item.8": [],
                "libobs.show_scene_item.1": [],
                "libobs.hide_scene_item.1": [],
                "libobs.show_scene_item.2": [],
                "libobs.hide_scene_item.2": [],
                "libobs.show_scene_item.3": [],
                "libobs.hide_scene_item.3": [],
                "libobs.show_scene_item.4": [],
                "libobs.hide_scene_item.4": [],
                "libobs.show_scene_item.9": [],
                "libobs.hide_scene_item.9": [],
                "libobs.show_scene_item.10": [],
                "libobs.hide_scene_item.10": [],
                "libobs.show_scene_item.11": [],
                "libobs.hide_scene_item.11": [],
                "libobs.show_scene_item.12": [],
                "libobs.hide_scene_item.12": [],
                "libobs.show_scene_item.13": [],
                "libobs.hide_scene_item.13": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Intro Music",
            "uuid": "e1aa771d-fa87-43e1-badc-d9bdec868521",
            "id": "vlc_source",
            "versioned_id": "vlc_source",
            "settings": {{
                "playlist": [
                    {{
                        "value": "{pathin}/Bung Proper Extended.mp3",
                        "selected": false,
                        "hidden": false
                    }}
                ],
                "shuffle": true
            }},
            "mixers": 241,
            "sync": 0,
            "flags": 0,
            "volume": 0.14116281270980835,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.mute": [],
                "libobs.unmute": [],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": [],
                "VLCSource.PlayPause": [],
                "VLCSource.Restart": [],
                "VLCSource.Stop": [],
                "VLCSource.PlaylistNext": [],
                "VLCSource.PlaylistPrev": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Right Team",
            "uuid": "e9668af6-e20b-43a1-b4be-72dbd008bd22",
            "id": "scene",
            "versioned_id": "scene",
            "settings": {{
                "custom_size": false,
                "id_counter": 19,
                "items": [
                    {{
                        "name": "Stats and Teams",
                        "source_uuid": "0d0df9bf-873f-4135-afdb-32839f403aee",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 1,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "[NS] Background Right",
                        "source_uuid": "aa673de4-763d-4cb8-a47d-65e2c6e157b0",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 13,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Right Logo",
                        "source_uuid": "96e8db6f-2029-460f-973e-aee47e99fc7c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 37.0,
                            "y": 45.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 964.0,
                            "y": 423.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 12,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Caster Frame",
                        "source_uuid": "efe75205-f7f9-4f0f-9206-47408bf5ef08",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 622.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 13,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Casters",
                        "source_uuid": "8d5d9598-e3c9-42d4-b072-8ecc0c0e89db",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 59.0,
                            "y": 747.0
                        }},
                        "scale": {{
                            "x": 1.0885714292526245,
                            "y": 1.0880000591278076
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 18,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Caster Setup",
                        "source_uuid": "4bb05f72-5ed2-4465-bf77-b7c92c741c46",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 622.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 5,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{
                            "collapsed": true
                        }}
                    }},
                    {{
                        "name": "Roster",
                        "source_uuid": "c40c1da6-03a9-4c06-839d-1b99a1aad22a",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1276.0,
                            "y": 61.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 6,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Right Roster",
                        "source_uuid": "428c791e-faa5-4c73-b37f-ffc2ed3fd619",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1139.0,
                            "y": 249.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 631.0,
                            "y": 630.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 14,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Right Text",
                        "source_uuid": "0367b2db-b567-44ce-8c90-1a4ca8850aca",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 37.0,
                            "y": 468.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 8,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 964.0,
                            "y": 101.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 11,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "[NS] Overlays",
                        "source_uuid": "040479cf-960d-42a7-abd2-d0c0999568a8",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 15,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord",
                        "source_uuid": "a526dbdc-0cb6-4cdb-ac11-2e4828bde919",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 16,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Microphone",
                        "source_uuid": "3b69d9d9-97ea-4347-a7c1-3346e7dc542c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 17,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "TickerBG",
                        "source_uuid": "c3b1a8ca-9df6-4ebc-84bf-5decc9b249e4",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 30,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Ticker Text",
                        "source_uuid": "50bcd47d-7a30-4206-bc09-732f141e585c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 199.39999389648438,
                            "y": 1019.0
                        }},
                        "scale": {{
                            "x": 0.85850000381469727,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 32,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Ticker",
                        "source_uuid": "03531d4f-e2b0-4503-b2c0-8e0c2db3c9b6",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 18,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "test",
                        "source_uuid": "b2f8ed2e-b1ad-47c2-8b25-97c93b4d18f7",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 572.0,
                            "y": 729.0
                        }},
                        "scale": {{
                            "x": 0.65142858028411865,
                            "y": 0.65135133266448975
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 19,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "OBSBasic.SelectScene": [],
                "libobs.show_scene_item.1": [],
                "libobs.hide_scene_item.1": [],
                "libobs.show_scene_item.13": [],
                "libobs.hide_scene_item.13": [],
                "libobs.show_scene_item.12": [],
                "libobs.hide_scene_item.12": [],
                "libobs.show_scene_item.5": [],
                "libobs.hide_scene_item.5": [],
                "libobs.show_scene_item.6": [],
                "libobs.hide_scene_item.6": [],
                "libobs.show_scene_item.14": [],
                "libobs.hide_scene_item.14": [],
                "libobs.show_scene_item.11": [],
                "libobs.hide_scene_item.11": [],
                "libobs.show_scene_item.15": [],
                "libobs.hide_scene_item.15": [],
                "libobs.show_scene_item.16": [],
                "libobs.hide_scene_item.16": [],
                "libobs.show_scene_item.17": [],
                "libobs.hide_scene_item.17": [],
                "libobs.show_scene_item.18": [],
                "libobs.hide_scene_item.18": [],
                "libobs.show_scene_item.19": [],
                "libobs.hide_scene_item.19": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Right Roster",
            "uuid": "428c791e-faa5-4c73-b37f-ffc2ed3fd619",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "read_from_file": true,
                "file": "{pathin}/playersAway.txt",
                "text": "Dwarf\nPicasso Dior\nkaidan\nkubix",
                "font": {{
                    "face": "Century Gothic",
                    "flags": 0,
                    "size": 70,
                    "style": "Regular"
                }},
                "align": "center"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Left Roster",
            "uuid": "27ae541f-e26d-477c-bb3f-19da5b6e26a4",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "read_from_file": true,
                "chatlog": false,
                "outline": false,
                "file": "{pathin}/playersHome.txt",
                "text": "ARC-5555 Fives\nwillzz\nhalios_\nLiebe\nLausiie",
                "font": {{
                    "face": "Century Gothic",
                    "flags": 0,
                    "size": 70,
                    "style": "Regular"
                }},
                "align": "center"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "---------- Post-Intro ^ ---------",
            "uuid": "902d8066-2398-4a0c-98ff-ad58a86f242d",
            "id": "scene",
            "versioned_id": "scene",
            "settings": {{
                "custom_size": false,
                "id_counter": 0,
                "items": []
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "OBSBasic.SelectScene": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Right Team Intro",
            "uuid": "a6963073-9a7e-4d46-82fb-a118d34753b3",
            "id": "scene",
            "versioned_id": "scene",
            "settings": {{
                "custom_size": false,
                "id_counter": 14,
                "items": [
                    {{
                        "name": "Intro Music",
                        "source_uuid": "e1aa771d-fa87-43e1-badc-d9bdec868521",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 10,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "[NS] Background Right",
                        "source_uuid": "aa673de4-763d-4cb8-a47d-65e2c6e157b0",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 2,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Right Logo",
                        "source_uuid": "96e8db6f-2029-460f-973e-aee47e99fc7c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 37.0,
                            "y": 45.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 964.0,
                            "y": 423.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 3,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "test",
                        "source_uuid": "b2f8ed2e-b1ad-47c2-8b25-97c93b4d18f7",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 572.0,
                            "y": 729.0
                        }},
                        "scale": {{
                            "x": 0.65142858028411865,
                            "y": 0.65135133266448975
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 4,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Caster Frame",
                        "source_uuid": "efe75205-f7f9-4f0f-9206-47408bf5ef08",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 622.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 13,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Casters",
                        "source_uuid": "8d5d9598-e3c9-42d4-b072-8ecc0c0e89db",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 59.0,
                            "y": 747.0
                        }},
                        "scale": {{
                            "x": 1.0885714292526245,
                            "y": 1.0880000591278076
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 18,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Caster Setup",
                        "source_uuid": "4bb05f72-5ed2-4465-bf77-b7c92c741c46",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 622.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 5,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{
                            "collapsed": true
                        }}
                    }},
                    {{
                        "name": "Roster",
                        "source_uuid": "c40c1da6-03a9-4c06-839d-1b99a1aad22a",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1276.0,
                            "y": 61.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 6,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Right Roster",
                        "source_uuid": "428c791e-faa5-4c73-b37f-ffc2ed3fd619",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1139.0,
                            "y": 249.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 631.0,
                            "y": 630.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 7,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Right Text",
                        "source_uuid": "0367b2db-b567-44ce-8c90-1a4ca8850aca",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 37.0,
                            "y": 468.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 8,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 964.0,
                            "y": 101.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 8,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "[NS] Overlays",
                        "source_uuid": "040479cf-960d-42a7-abd2-d0c0999568a8",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 11,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord",
                        "source_uuid": "a526dbdc-0cb6-4cdb-ac11-2e4828bde919",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 12,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Microphone",
                        "source_uuid": "3b69d9d9-97ea-4347-a7c1-3346e7dc542c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 13,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "TickerBG",
                        "source_uuid": "c3b1a8ca-9df6-4ebc-84bf-5decc9b249e4",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 30,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Ticker Text",
                        "source_uuid": "50bcd47d-7a30-4206-bc09-732f141e585c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 199.39999389648438,
                            "y": 1019.0
                        }},
                        "scale": {{
                            "x": 0.85850000381469727,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 32,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Ticker",
                        "source_uuid": "03531d4f-e2b0-4503-b2c0-8e0c2db3c9b6",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 14,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "OBSBasic.SelectScene": [],
                "libobs.show_scene_item.10": [],
                "libobs.hide_scene_item.10": [],
                "libobs.show_scene_item.2": [],
                "libobs.hide_scene_item.2": [],
                "libobs.show_scene_item.3": [],
                "libobs.hide_scene_item.3": [],
                "libobs.show_scene_item.4": [],
                "libobs.hide_scene_item.4": [],
                "libobs.show_scene_item.5": [],
                "libobs.hide_scene_item.5": [],
                "libobs.show_scene_item.6": [],
                "libobs.hide_scene_item.6": [],
                "libobs.show_scene_item.7": [],
                "libobs.hide_scene_item.7": [],
                "libobs.show_scene_item.8": [],
                "libobs.hide_scene_item.8": [],
                "libobs.show_scene_item.11": [],
                "libobs.hide_scene_item.11": [],
                "libobs.show_scene_item.12": [],
                "libobs.hide_scene_item.12": [],
                "libobs.show_scene_item.13": [],
                "libobs.hide_scene_item.13": [],
                "libobs.show_scene_item.14": [],
                "libobs.hide_scene_item.14": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Left Team Intro",
            "uuid": "92ac9300-6bc3-4b78-bb95-910f0f7d652d",
            "id": "scene",
            "versioned_id": "scene",
            "settings": {{
                "custom_size": false,
                "id_counter": 14,
                "items": [
                    {{
                        "name": "Intro Music",
                        "source_uuid": "e1aa771d-fa87-43e1-badc-d9bdec868521",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 10,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "[NS] Background Left",
                        "source_uuid": "9d0b3f6a-2570-403e-a70e-1d57293bdc07",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 2,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Left Logo",
                        "source_uuid": "b31bc3c2-c8f8-4a0d-a423-04fdbabaa8c0",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 37.0,
                            "y": 45.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 964.0,
                            "y": 423.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 3,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "test",
                        "source_uuid": "b2f8ed2e-b1ad-47c2-8b25-97c93b4d18f7",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 572.0,
                            "y": 729.0
                        }},
                        "scale": {{
                            "x": 0.65142858028411865,
                            "y": 0.65135133266448975
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 4,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Caster Frame",
                        "source_uuid": "efe75205-f7f9-4f0f-9206-47408bf5ef08",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 622.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 13,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Casters",
                        "source_uuid": "8d5d9598-e3c9-42d4-b072-8ecc0c0e89db",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 59.0,
                            "y": 747.0
                        }},
                        "scale": {{
                            "x": 1.0885714292526245,
                            "y": 1.0880000591278076
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 18,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Caster Setup",
                        "source_uuid": "4bb05f72-5ed2-4465-bf77-b7c92c741c46",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 622.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 5,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Roster",
                        "source_uuid": "c40c1da6-03a9-4c06-839d-1b99a1aad22a",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1276.0,
                            "y": 61.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 6,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Left Roster",
                        "source_uuid": "27ae541f-e26d-477c-bb3f-19da5b6e26a4",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1139.0,
                            "y": 249.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 631.0,
                            "y": 630.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 7,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Left Text",
                        "source_uuid": "b99d0e62-4d9a-40d6-a619-95df24f1f639",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 37.0,
                            "y": 468.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 8,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 964.0,
                            "y": 101.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 8,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "[NS] Overlays",
                        "source_uuid": "040479cf-960d-42a7-abd2-d0c0999568a8",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 11,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord",
                        "source_uuid": "a526dbdc-0cb6-4cdb-ac11-2e4828bde919",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 12,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Microphone",
                        "source_uuid": "3b69d9d9-97ea-4347-a7c1-3346e7dc542c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 13,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "TickerBG",
                        "source_uuid": "c3b1a8ca-9df6-4ebc-84bf-5decc9b249e4",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 30,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Ticker Text",
                        "source_uuid": "50bcd47d-7a30-4206-bc09-732f141e585c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 199.39999389648438,
                            "y": 1019.0
                        }},
                        "scale": {{
                            "x": 0.85850000381469727,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 32,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Ticker",
                        "source_uuid": "03531d4f-e2b0-4503-b2c0-8e0c2db3c9b6",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 14,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "OBSBasic.SelectScene": [],
                "libobs.show_scene_item.10": [],
                "libobs.hide_scene_item.10": [],
                "libobs.show_scene_item.2": [],
                "libobs.hide_scene_item.2": [],
                "libobs.show_scene_item.3": [],
                "libobs.hide_scene_item.3": [],
                "libobs.show_scene_item.4": [],
                "libobs.hide_scene_item.4": [],
                "libobs.show_scene_item.5": [],
                "libobs.hide_scene_item.5": [],
                "libobs.show_scene_item.6": [],
                "libobs.hide_scene_item.6": [],
                "libobs.show_scene_item.7": [],
                "libobs.hide_scene_item.7": [],
                "libobs.show_scene_item.8": [],
                "libobs.hide_scene_item.8": [],
                "libobs.show_scene_item.11": [],
                "libobs.hide_scene_item.11": [],
                "libobs.show_scene_item.12": [],
                "libobs.hide_scene_item.12": [],
                "libobs.show_scene_item.13": [],
                "libobs.hide_scene_item.13": [],
                "libobs.show_scene_item.14": [],
                "libobs.hide_scene_item.14": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Intro",
            "uuid": "3fb777c0-a98f-453f-a101-9f4be526363e",
            "id": "scene",
            "versioned_id": "scene",
            "settings": {{
                "custom_size": false,
                "id_counter": 2,
                "items": [
                    {{
                        "name": "Slap Intro",
                        "source_uuid": "0b8d1a4e-9906-4f98-b364-710dd1e84018",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 2,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "OBSBasic.SelectScene": [],
                "libobs.show_scene_item.2": [],
                "libobs.hide_scene_item.2": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{
                "transition": ""
            }}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Slap Intro",
            "uuid": "0b8d1a4e-9906-4f98-b364-710dd1e84018",
            "id": "ffmpeg_source",
            "versioned_id": "ffmpeg_source",
            "settings": {{
                "local_file": "{pathin}/Cresus Intro.mp4",
                "close_when_inactive": true
            }},
            "mixers": 241,
            "sync": 0,
            "flags": 0,
            "volume": 0.50118720531463623,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.mute": [],
                "libobs.unmute": [],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": [],
                "MediaSource.Restart": [],
                "MediaSource.Play": [],
                "MediaSource.Pause": [],
                "MediaSource.Stop": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{
                "mixer_hidden": false
            }}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Countdown",
            "uuid": "6bb6d370-92d0-4b2e-a400-783c5f623e38",
            "id": "browser_source",
            "versioned_id": "browser_source",
            "settings": {{
                "url": "https://ecard.enter-media.org/widgets/2206056/?title=Simple+3min+-+3hours+countdown&layer1=&color0=272.2&size1=10&color1=BAFFF5&font1=2162535&offset1=-50&width=400&height=200&css=2162559&timer5=3&sound=NO&volume=100%25&dots=No&treload=N&frame=1",
                "width": 400,
                "height": 200
            }},
            "mixers": 192,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.mute": [],
                "libobs.unmute": [],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": [],
                "ObsBrowser.Refresh": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Ladder",
            "uuid": "01e97596-58c1-42ff-8404-f7c215c9da4d",
            "id": "scene",
            "versioned_id": "scene",
            "settings": {{
                "custom_size": false,
                "id_counter": 17,
                "items": [
                    {{
                        "name": "[NS] Background",
                        "source_uuid": "f3da34e6-1ba4-4980-a925-2639f7bda1cc",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 13,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Stats and Teams",
                        "source_uuid": "0d0df9bf-873f-4135-afdb-32839f403aee",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 1,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "[NS] Overlays",
                        "source_uuid": "040479cf-960d-42a7-abd2-d0c0999568a8",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 3,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Caster Frame",
                        "source_uuid": "efe75205-f7f9-4f0f-9206-47408bf5ef08",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1446.0,
                            "y": 173.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 13,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Casters",
                        "source_uuid": "8d5d9598-e3c9-42d4-b072-8ecc0c0e89db",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1505.0,
                            "y": 298.0
                        }},
                        "scale": {{
                            "x": 1.0885714292526245,
                            "y": 1.0880000591278076
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 18,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Caster Setup",
                        "source_uuid": "4bb05f72-5ed2-4465-bf77-b7c92c741c46",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1446.0,
                            "y": 173.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 4,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{
                            "collapsed": true
                        }}
                    }},
                    {{
                        "name": "Discord Box Back",
                        "source_uuid": "f1c6105f-819f-442e-bc9f-23d1bed3be98",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1540.0,
                            "y": 823.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 16,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord Invite Link",
                        "source_uuid": "056ad710-8177-4fe4-ab8e-2e33c5cf7759",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1550.0,
                            "y": 834.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 17,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord Box Frame",
                        "source_uuid": "17b335cb-ddd9-43bf-8cd3-6b017b716816",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1540.0,
                            "y": 823.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 15,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord Link",
                        "source_uuid": "f2f5e807-beb9-4e3d-9d45-a287984599e9",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1540.0,
                            "y": 823.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 5,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{
                            "collapsed": true
                        }}
                    }},
                    {{
                        "name": "[NS] Overlays",
                        "source_uuid": "040479cf-960d-42a7-abd2-d0c0999568a8",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 11,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Live Ladder",
                        "source_uuid": "23dd6a77-5784-4a64-a69b-cb9fb9d8e090",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 12,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "test",
                        "source_uuid": "b2f8ed2e-b1ad-47c2-8b25-97c93b4d18f7",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1447.0,
                            "y": 598.0
                        }},
                        "scale": {{
                            "x": 0.60857141017913818,
                            "y": 0.60810810327529907
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 14,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord",
                        "source_uuid": "a526dbdc-0cb6-4cdb-ac11-2e4828bde919",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 15,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Microphone",
                        "source_uuid": "3b69d9d9-97ea-4347-a7c1-3346e7dc542c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 16,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "TickerBG",
                        "source_uuid": "c3b1a8ca-9df6-4ebc-84bf-5decc9b249e4",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 30,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Ticker Text",
                        "source_uuid": "50bcd47d-7a30-4206-bc09-732f141e585c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 199.39999389648438,
                            "y": 1019.0
                        }},
                        "scale": {{
                            "x": 0.85850000381469727,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 32,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Ticker",
                        "source_uuid": "03531d4f-e2b0-4503-b2c0-8e0c2db3c9b6",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 17,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "OBSBasic.SelectScene": [],
                "libobs.show_scene_item.13": [],
                "libobs.hide_scene_item.13": [],
                "libobs.show_scene_item.1": [],
                "libobs.hide_scene_item.1": [],
                "libobs.show_scene_item.3": [],
                "libobs.hide_scene_item.3": [],
                "libobs.show_scene_item.4": [],
                "libobs.hide_scene_item.4": [],
                "libobs.show_scene_item.5": [],
                "libobs.hide_scene_item.5": [],
                "libobs.show_scene_item.11": [],
                "libobs.hide_scene_item.11": [],
                "libobs.show_scene_item.12": [],
                "libobs.hide_scene_item.12": [],
                "libobs.show_scene_item.14": [],
                "libobs.hide_scene_item.14": [],
                "libobs.show_scene_item.15": [],
                "libobs.hide_scene_item.15": [],
                "libobs.show_scene_item.16": [],
                "libobs.hide_scene_item.16": [],
                "libobs.show_scene_item.17": [],
                "libobs.hide_scene_item.17": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{
                "transition": ""
            }}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Live Ladder",
            "uuid": "23dd6a77-5784-4a64-a69b-cb9fb9d8e090",
            "id": "browser_source",
            "versioned_id": "browser_source",
            "settings": {{
                "is_local_file": true,
                "local_file": "{pathin}/ladder.html",
                "url": "https://www.google.com/",
                "width": 1500,
                "height": 1080,
                "shutdown": true,
                "restart_when_active": true,
                "webpage_control_level": 1,
                "css": "body {{ background-color: rgba(0, 0, 0, 0); margin: 0px auto; overflow: hidden; }}"
            }},
            "mixers": 255,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.mute": [],
                "libobs.unmute": [],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": [],
                "ObsBrowser.Refresh": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Game",
            "uuid": "d461a850-6ac3-4888-ab43-95a68f2f0b22",
            "id": "scene",
            "versioned_id": "scene",
            "settings": {{
                "custom_size": false,
                "id_counter": 18,
                "items": [
                    {{
                        "name": "Discord",
                        "source_uuid": "a526dbdc-0cb6-4cdb-ac11-2e4828bde919",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 1,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Slapshot",
                        "source_uuid": "09fa4428-a6c5-47f6-b31c-aaa4b421e158",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 2,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Microphone",
                        "source_uuid": "3b69d9d9-97ea-4347-a7c1-3346e7dc542c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 3,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "[NS] Overlays",
                        "source_uuid": "040479cf-960d-42a7-abd2-d0c0999568a8",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 5,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Game Capture",
                        "source_uuid": "bddf043c-3316-41e3-b034-f623600074aa",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1920.0,
                            "y": 1080.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 6,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "[NS] Game Score",
                        "source_uuid": "cfdc3784-b6ea-45f3-af15-cbadd4e75836",
                        "visible": false,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1920.0,
                            "y": 1080.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 7,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Super Saturday Ad",
                        "source_uuid": "658082aa-678c-4f5b-bf81-cd87c40fd6be",
                        "visible": false,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 662.5,
                            "y": 883.0
                        }},
                        "scale": {{
                            "x": 0.49583333730697632,
                            "y": 0.49532711505889893
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 18,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "id": "slide_transition",
                            "versioned_id": "slide_transition",
                            "name": "Super Saturday Ad Show Transition",
                            "transition": {{
                                "direction": "up"
                            }},
                            "duration": 500
                        }},
                        "hide_transition": {{
                            "id": "slide_transition",
                            "versioned_id": "slide_transition",
                            "name": "Super Saturday Ad Hide Transition",
                            "transition": {{
                                "direction": "down"
                            }},
                            "duration": 500
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "TickerBG",
                        "source_uuid": "c3b1a8ca-9df6-4ebc-84bf-5decc9b249e4",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 30,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Ticker Text",
                        "source_uuid": "50bcd47d-7a30-4206-bc09-732f141e585c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 199.39999389648438,
                            "y": 1019.0
                        }},
                        "scale": {{
                            "x": 0.85850000381469727,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 32,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Ticker",
                        "source_uuid": "03531d4f-e2b0-4503-b2c0-8e0c2db3c9b6",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 8,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{
                            "collapsed": false
                        }}
                    }},
                    {{
                        "name": "SC2",
                        "source_uuid": "51e9ddfd-cf12-4440-8863-071e5275946b",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 11,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Left Text 2",
                        "source_uuid": "fc6bdd2a-26f1-44fd-bc48-60bb5c93136e",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 685.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 193.0,
                            "y": 86.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 14,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Right Text 3",
                        "source_uuid": "07070643-cf4a-4cbd-bdfe-f27acd6c82a4",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1042.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 193.0,
                            "y": 86.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 15,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Left Score 2",
                        "source_uuid": "f7742ed6-c8b1-4db7-8627-b6b33f2e9dd7",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 878.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 47.0,
                            "y": 86.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 16,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Right Score 2",
                        "source_uuid": "820be9c0-cc29-4dc7-9f25-7c55cfeccb12",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 996.0,
                            "y": 1.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 47.0,
                            "y": 85.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 17,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Middle 2",
                        "source_uuid": "bbd196f5-047d-4c06-ac6e-7b8ba6fead86",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 924.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 72.0,
                            "y": 86.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 18,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Best Of 2",
                        "source_uuid": "04f344af-879e-41f7-ab18-a22feb81d91d",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 906.0,
                            "y": 86.0
                        }},
                        "scale": {{
                            "x": 1.0370370149612427,
                            "y": 1.0333333015441895
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 108.0,
                            "y": 31.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 19,
                        "group_item_backup": true,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Series Points",
                        "source_uuid": "47293b10-504d-4a96-a1f9-40b5af76b45c",
                        "visible": false,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 14,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{
                            "collapsed": true
                        }}
                    }},
                    {{
                        "name": "[NS] Overlays",
                        "source_uuid": "040479cf-960d-42a7-abd2-d0c0999568a8",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 16,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Audio Output Capture",
                        "source_uuid": "d52a078b-9ed9-44f5-b01b-646b27b77768",
                        "visible": false,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 17,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "OBSBasic.SelectScene": [],
                "libobs.show_scene_item.1": [],
                "libobs.hide_scene_item.1": [],
                "libobs.show_scene_item.2": [],
                "libobs.hide_scene_item.2": [],
                "libobs.show_scene_item.3": [],
                "libobs.hide_scene_item.3": [],
                "libobs.show_scene_item.5": [],
                "libobs.hide_scene_item.5": [],
                "libobs.show_scene_item.6": [],
                "libobs.hide_scene_item.6": [],
                "libobs.show_scene_item.7": [],
                "libobs.hide_scene_item.7": [],
                "libobs.show_scene_item.8": [],
                "libobs.hide_scene_item.8": [],
                "libobs.show_scene_item.14": [],
                "libobs.hide_scene_item.14": [],
                "libobs.show_scene_item.16": [],
                "libobs.hide_scene_item.16": [],
                "libobs.show_scene_item.17": [],
                "libobs.hide_scene_item.17": [],
                "libobs.show_scene_item.18": [],
                "libobs.hide_scene_item.18": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Discord",
            "uuid": "a526dbdc-0cb6-4cdb-ac11-2e4828bde919",
            "id": "wasapi_process_output_capture",
            "versioned_id": "wasapi_process_output_capture",
            "settings": {{
                "priority": 2,
                "window": "My Poorly Lit Minecraft Basement | Monkey Land - Discord:Chrome_WidgetWin_1:Discord.exe"
            }},
            "mixers": 229,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.mute": [],
                "libobs.unmute": [],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}},
            "filters": [
                {{
                    "prev_ver": 503382018,
                    "name": "Limiter",
                    "uuid": "f04a9b3a-8f3a-4646-8b8c-4c37b0c409a1",
                    "id": "limiter_filter",
                    "versioned_id": "limiter_filter",
                    "settings": {{
                        "threshold": -4.0
                    }},
                    "mixers": 255,
                    "sync": 0,
                    "flags": 0,
                    "volume": 1.0,
                    "balance": 0.5,
                    "enabled": true,
                    "muted": false,
                    "push-to-mute": false,
                    "push-to-mute-delay": 0,
                    "push-to-talk": false,
                    "push-to-talk-delay": 0,
                    "hotkeys": {{}},
                    "deinterlace_mode": 0,
                    "deinterlace_field_order": 0,
                    "monitoring_type": 0,
                    "private_settings": {{}}
                }}
            ]
        }},
        {{
            "prev_ver": 503382018,
            "name": "Slapshot",
            "uuid": "09fa4428-a6c5-47f6-b31c-aaa4b421e158",
            "id": "wasapi_process_output_capture",
            "versioned_id": "wasapi_process_output_capture",
            "settings": {{
                "priority": 2,
                "window": "Slapshot:UnityWndClass:Slapshot.exe"
            }},
            "mixers": 227,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.mute": [],
                "libobs.unmute": [],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Microphone",
            "uuid": "3b69d9d9-97ea-4347-a7c1-3346e7dc542c",
            "id": "wasapi_input_capture",
            "versioned_id": "wasapi_input_capture",
            "settings": {{
                "device_id": "{{0.0.1.00000000}}.{{54437c68-ba06-4de1-b53a-e790a38bd7f4}}",
                "use_device_timing": false
            }},
            "mixers": 233,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.mute": [
                    {{
                        "shift": true,
                        "control": true,
                        "key": "OBS_KEY_BACKSLASH"
                    }}
                ],
                "libobs.unmute": [
                    {{
                        "shift": true,
                        "control": true,
                        "key": "OBS_KEY_BACKSLASH"
                    }}
                ],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}},
            "filters": [
                {{
                    "prev_ver": 503382018,
                    "name": "Noise Suppression",
                    "uuid": "0eef2f93-fea8-4a6e-b696-e00998fa08e2",
                    "id": "noise_suppress_filter",
                    "versioned_id": "noise_suppress_filter_v2",
                    "settings": {{
                        "suppress_level": -7,
                        "method": "speex",
                        "intensity": 1.0
                    }},
                    "mixers": 255,
                    "sync": 0,
                    "flags": 0,
                    "volume": 1.0,
                    "balance": 0.5,
                    "enabled": false,
                    "muted": false,
                    "push-to-mute": false,
                    "push-to-mute-delay": 0,
                    "push-to-talk": false,
                    "push-to-talk-delay": 0,
                    "hotkeys": {{}},
                    "deinterlace_mode": 0,
                    "deinterlace_field_order": 0,
                    "monitoring_type": 0,
                    "private_settings": {{}}
                }},
                {{
                    "prev_ver": 503382018,
                    "name": "Noise Gate",
                    "uuid": "d693935b-29f0-404a-bff3-dfce1ce987e1",
                    "id": "noise_gate_filter",
                    "versioned_id": "noise_gate_filter",
                    "settings": {{
                        "open_threshold": -35.0,
                        "close_threshold": -40.0,
                        "hold_time": 100,
                        "release_time": 50
                    }},
                    "mixers": 255,
                    "sync": 0,
                    "flags": 0,
                    "volume": 1.0,
                    "balance": 0.5,
                    "enabled": true,
                    "muted": false,
                    "push-to-mute": false,
                    "push-to-mute-delay": 0,
                    "push-to-talk": false,
                    "push-to-talk-delay": 0,
                    "hotkeys": {{}},
                    "deinterlace_mode": 0,
                    "deinterlace_field_order": 0,
                    "monitoring_type": 0,
                    "private_settings": {{}}
                }},
                {{
                    "prev_ver": 503382018,
                    "name": "Gain",
                    "uuid": "9aebbd13-3142-4d21-87de-cfe099bd17ea",
                    "id": "gain_filter",
                    "versioned_id": "gain_filter",
                    "settings": {{
                        "db": 0.40000000000000002
                    }},
                    "mixers": 255,
                    "sync": 0,
                    "flags": 0,
                    "volume": 1.0,
                    "balance": 0.5,
                    "enabled": false,
                    "muted": false,
                    "push-to-mute": false,
                    "push-to-mute-delay": 0,
                    "push-to-talk": false,
                    "push-to-talk-delay": 0,
                    "hotkeys": {{}},
                    "deinterlace_mode": 0,
                    "deinterlace_field_order": 0,
                    "monitoring_type": 0,
                    "private_settings": {{}}
                }},
                {{
                    "prev_ver": 503382018,
                    "name": "VST 2.x Plug-in",
                    "uuid": "e281b2b2-027a-4b25-82f6-0b196c634c37",
                    "id": "vst_filter",
                    "versioned_id": "vst_filter",
                    "settings": {{
                        "chunk_data": "IQAAAAQAAAAAAAAAAQAAAB73wBeIKGJAqwZFAKuN+j8NAAAAAAAAQAEIAAAAAQAAAAAAAAAAwHJAAAAAAAAA8D8AAAAAAAAAQAEIAAAAAQAAAL+K7CsE1I5Aj6vo6n2n5j8NAAAAAAAAQAEBAAAAAQAAAG0IznvGFapA67hbLZjs/z8NAAAAAAAAQAEBAAAAAQAAAAAAAAAAAPA/AAAAAA==",
                        "chunk_hash": "4b87c6ed275ef63d9f4a298d4e92930f",
                        "plugin_path": "C:/Program Files/VSTPlugins/ReaPlugs/reaeq-standalone.dll"
                    }},
                    "mixers": 255,
                    "sync": 0,
                    "flags": 0,
                    "volume": 1.0,
                    "balance": 0.5,
                    "enabled": false,
                    "muted": false,
                    "push-to-mute": false,
                    "push-to-mute-delay": 0,
                    "push-to-talk": false,
                    "push-to-talk-delay": 0,
                    "hotkeys": {{}},
                    "deinterlace_mode": 0,
                    "deinterlace_field_order": 0,
                    "monitoring_type": 0,
                    "private_settings": {{}}
                }},
                {{
                    "prev_ver": 503382018,
                    "name": "Upward Compressor",
                    "uuid": "d822bcd1-9944-4e70-93ab-1fbd76f9e6a5",
                    "id": "upward_compressor_filter",
                    "versioned_id": "upward_compressor_filter",
                    "settings": {{
                        "ratio": 0.5,
                        "threshold": -15.699999999999999,
                        "knee_width": 10
                    }},
                    "mixers": 255,
                    "sync": 0,
                    "flags": 0,
                    "volume": 1.0,
                    "balance": 0.5,
                    "enabled": true,
                    "muted": false,
                    "push-to-mute": false,
                    "push-to-mute-delay": 0,
                    "push-to-talk": false,
                    "push-to-talk-delay": 0,
                    "hotkeys": {{}},
                    "deinterlace_mode": 0,
                    "deinterlace_field_order": 0,
                    "monitoring_type": 0,
                    "private_settings": {{}}
                }},
                {{
                    "prev_ver": 503382018,
                    "name": "Compressor",
                    "uuid": "9c58b252-d2f3-4e57-94e6-6a9403a36c1f",
                    "id": "compressor_filter",
                    "versioned_id": "compressor_filter",
                    "settings": {{
                        "ratio": 2.0,
                        "threshold": -9.1999999999999993,
                        "output_gain": 0.0,
                        "sidechain_source": "none"
                    }},
                    "mixers": 255,
                    "sync": 0,
                    "flags": 0,
                    "volume": 1.0,
                    "balance": 0.5,
                    "enabled": true,
                    "muted": false,
                    "push-to-mute": false,
                    "push-to-mute-delay": 0,
                    "push-to-talk": false,
                    "push-to-talk-delay": 0,
                    "hotkeys": {{}},
                    "deinterlace_mode": 0,
                    "deinterlace_field_order": 0,
                    "monitoring_type": 0,
                    "private_settings": {{}}
                }},
                {{
                    "prev_ver": 503382018,
                    "name": "Limiter",
                    "uuid": "2c0add01-cf98-4ad6-89ad-b3550b63533b",
                    "id": "limiter_filter",
                    "versioned_id": "limiter_filter",
                    "settings": {{
                        "threshold": -2.0
                    }},
                    "mixers": 255,
                    "sync": 0,
                    "flags": 0,
                    "volume": 1.0,
                    "balance": 0.5,
                    "enabled": true,
                    "muted": false,
                    "push-to-mute": false,
                    "push-to-mute-delay": 0,
                    "push-to-talk": false,
                    "push-to-talk-delay": 0,
                    "hotkeys": {{}},
                    "deinterlace_mode": 0,
                    "deinterlace_field_order": 0,
                    "monitoring_type": 0,
                    "private_settings": {{}}
                }},
                {{
                    "prev_ver": 503382018,
                    "name": "Effect",
                    "uuid": "da760eec-8bd3-4f5b-b82c-3e9072ae8a4b",
                    "id": "vst_filter",
                    "versioned_id": "vst_filter",
                    "settings": {{
                        "plugin_path": "C:/Program Files/VSTPlugins/KHS/kHs Dual Delay.dll",
                        "chunk_data": "UEsDBBQACAgIANSwqlgAAAAAAAAAAAAAAAAKAAAAc3RhdGUuanNvbu3b22rCMBgH8Ov2KUbZpYjOTcbeYU8whsT2qxZzKDm4ifjuaw61Lbi7MTb4eyH2yz/JL/GEQs55VgiyrHi5O+dZVjBn90p3VwV3B/oo8uwy6yJH0qZRsk/VSgtmfWpZzHyh5W7XyFBYLB/7Xq0mQ7bv1DK794nYQzJB4SplhaqI99HuITttbBMji/lD7KOZbVSYZL5ePi9Wj7Ec09IJ6gIRvxq3VCSVaGTfNrrcLNcp6MpDmCpempMsN17ka4ERyjVRtWUpOX+KxVIrYyzj06rp1s6qSckqSaM5RPMZm1fxlhaz42rLuEk70e2TE6+qctwvXZqhf9ixUfnN17LQx8/F9C7u/GWWSkY5XdKkxIRy0o7G9Mtx+kjTEkm25RQWY7Wja/3entoQHSRFaEoTnL+f+YbvlzDYmX+xM3iagMELGBi8m4ABBp/AwAADDDB/EIOvA2CAAQYYYIDBTxVggAEGGGCAAQYYYIABBj9VgAEGGGCAAQYYYIABBhhggAEGGGAy/FkEDDA/iPH37yE2hPrzdXnCFhXVzHE7nLjjTUnS0IareNKv7uJpttuGYfDrWNfRhybHeDiO6A885pf8C1BLBwh0h9GovwEAAHk5AABQSwECAAAUAAgICADUsKpYdIfRqL8BAAB5OQAACgAAAAAAAAAAAAAAAAAAAAAAc3RhdGUuanNvblBLBQYAAAAAAQABADgAAAD3AQAAAAA=",
                        "chunk_hash": "922fb1466eea67c909aefcad40e3ea42"
                    }},
                    "mixers": 255,
                    "sync": 0,
                    "flags": 0,
                    "volume": 1.0,
                    "balance": 0.5,
                    "enabled": false,
                    "muted": false,
                    "push-to-mute": false,
                    "push-to-mute-delay": 0,
                    "push-to-talk": false,
                    "push-to-talk-delay": 0,
                    "hotkeys": {{}},
                    "deinterlace_mode": 0,
                    "deinterlace_field_order": 0,
                    "monitoring_type": 0,
                    "private_settings": {{}}
                }},
                {{
                    "prev_ver": 503382018,
                    "name": "Hotkeys",
                    "uuid": "c65883df-9141-4681-b5b7-0bbcafebd6f6",
                    "id": "_filter_hotkeys_audio",
                    "versioned_id": "_filter_hotkeys_audio",
                    "settings": {{
                        "2;Mic/Aux;Noise Suppression": [],
                        "3;Mic/Aux;Noise Suppression": [],
                        "3;Mic/Aux;Upward Compressor": [],
                        "3;Mic/Aux;Effect": [
                            {{
                                "key": "OBS_KEY_NUM9"
                            }}
                        ],
                        "1;Mic/Aux;Noise Gate": [],
                        "0;Mic/Aux;Noise Gate": [],
                        "2;Mic/Aux;Noise Gate": [],
                        "3;Mic/Aux;Noise Gate": [],
                        "3;Mic/Aux;Compressor": [],
                        "1;Mic/Aux;Compressor": [],
                        "0;Mic/Aux;Compressor": [],
                        "1;Mic/Aux;Limiter": [],
                        "0;Mic/Aux;Limiter": [],
                        "2;Mic/Aux;Limiter": [],
                        "3;Mic/Aux;Limiter": [],
                        "2;Mic/Aux;Compressor": [],
                        "1;Mic/Aux;Effect": [],
                        "0;Mic/Aux;Effect": [],
                        "2;Mic/Aux;Effect": [],
                        "1;Mic/Aux;Gain": [],
                        "0;Mic/Aux;Gain": [],
                        "2;Mic/Aux;Gain": [],
                        "3;Mic/Aux;Gain": [],
                        "2;Mic/Aux;Upward Compressor": [],
                        "0;Mic/Aux;Upward Compressor": [],
                        "1;Mic/Aux;VST 2.x Plug-in": [],
                        "0;Mic/Aux;VST 2.x Plug-in": [],
                        "2;Mic/Aux;VST 2.x Plug-in": [],
                        "3;Mic/Aux;VST 2.x Plug-in": [],
                        "1;Mic/Aux;Upward Compressor": [],
                        "1;Mic/Aux;Noise Suppression": [],
                        "0;Mic/Aux;Noise Suppression": []
                    }},
                    "mixers": 255,
                    "sync": 0,
                    "flags": 0,
                    "volume": 1.0,
                    "balance": 0.5,
                    "enabled": false,
                    "muted": false,
                    "push-to-mute": false,
                    "push-to-mute-delay": 0,
                    "push-to-talk": false,
                    "push-to-talk-delay": 0,
                    "hotkeys": {{}},
                    "deinterlace_mode": 0,
                    "deinterlace_field_order": 0,
                    "monitoring_type": 0,
                    "private_settings": {{}}
                }}
            ]
        }},
        {{
            "prev_ver": 503382018,
            "name": "Game Capture",
            "uuid": "bddf043c-3316-41e3-b034-f623600074aa",
            "id": "game_capture",
            "versioned_id": "game_capture",
            "settings": {{
                "window": "Slapshot:UnityWndClass:Slapshot.exe",
                "capture_mode": "window",
                "capture_cursor": false
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.mute": [],
                "libobs.unmute": [],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": [],
                "hotkey_start": [],
                "hotkey_stop": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "TickerBG",
            "uuid": "c3b1a8ca-9df6-4ebc-84bf-5decc9b249e4",
            "id": "image_source",
            "versioned_id": "image_source",
            "settings": {{
                "file": "{pathin}/Ticker.png"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Temp",
            "uuid": "6d11ed0d-e614-4bcb-bbf3-7a14499174e9",
            "id": "scene",
            "versioned_id": "scene",
            "settings": {{
                "id_counter": 23,
                "custom_size": false,
                "items": [
                    {{
                        "name": "[NS] Background",
                        "source_uuid": "f3da34e6-1ba4-4980-a925-2639f7bda1cc",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 21,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Browser",
                        "source_uuid": "22c6eb60-8391-48a1-807c-d0a5d1ece151",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 60.0,
                            "y": 90.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 23,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "OBSBasic.SelectScene": [],
                "libobs.show_scene_item.21": [],
                "libobs.hide_scene_item.21": [],
                "libobs.show_scene_item.23": [],
                "libobs.hide_scene_item.23": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "SC2",
            "uuid": "51e9ddfd-cf12-4440-8863-071e5275946b",
            "id": "image_source",
            "versioned_id": "image_source",
            "settings": {{
                "file": "{pathin}/Score2.png"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Left Text 2",
            "uuid": "fc6bdd2a-26f1-44fd-bc48-60bb5c93136e",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "drop_shadow": true,
                "from_file": true,
                "outline": false,
                "read_from_file": true,
                "text": "",
                "text_file": "E:/!Videos Or Streaming/Streaming Stuff/OSL Stats/Statsheet/teams/leftTeam/teamName.txt",
                "file": "{pathin}/accroHome.txt",
                "font": {{
                    "face": "Century Gothic",
                    "style": "Bold",
                    "size": 56,
                    "flags": 1
                }}
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}},
            "filters": [
                {{
                    "prev_ver": 503382018,
                    "name": "Image Mask/Blend",
                    "uuid": "360b90c2-292a-4d63-ada3-046b4ad558ff",
                    "id": "mask_filter",
                    "versioned_id": "mask_filter_v2",
                    "settings": {{
                        "image_path": "{colourHome}",
                        "type": "blend_mul_filter.effect"
                    }},
                    "mixers": 0,
                    "sync": 0,
                    "flags": 0,
                    "volume": 1.0,
                    "balance": 0.5,
                    "enabled": true,
                    "muted": false,
                    "push-to-mute": false,
                    "push-to-mute-delay": 0,
                    "push-to-talk": false,
                    "push-to-talk-delay": 0,
                    "hotkeys": {{}},
                    "deinterlace_mode": 0,
                    "deinterlace_field_order": 0,
                    "monitoring_type": 0,
                    "private_settings": {{}}
                }}
            ]
        }},
        {{
            "prev_ver": 503382018,
            "name": "Right Text 3",
            "uuid": "07070643-cf4a-4cbd-bdfe-f27acd6c82a4",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "drop_shadow": true,
                "from_file": true,
                "outline": false,
                "read_from_file": true,
                "text_file": "E:/!Videos Or Streaming/Streaming Stuff/OSL Stats/Statsheet/teams/rightTeam/teamName.txt",
                "text": "",
                "file": "{pathin}/accroAway.txt",
                "undo_sname": "Right Text 3",
                "font": {{
                    "face": "Century Gothic",
                    "style": "Bold",
                    "size": 56,
                    "flags": 1
                }}
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}},
            "filters": [
                {{
                    "prev_ver": 503382018,
                    "name": "Image Mask/Blend",
                    "uuid": "6f141ad8-5be1-467e-8995-4de31ee3a0bb",
                    "id": "mask_filter",
                    "versioned_id": "mask_filter_v2",
                    "settings": {{
                        "image_path": "{colourAway}",
                        "type": "blend_mul_filter.effect"
                    }},
                    "mixers": 0,
                    "sync": 0,
                    "flags": 0,
                    "volume": 1.0,
                    "balance": 0.5,
                    "enabled": true,
                    "muted": false,
                    "push-to-mute": false,
                    "push-to-mute-delay": 0,
                    "push-to-talk": false,
                    "push-to-talk-delay": 0,
                    "hotkeys": {{}},
                    "deinterlace_mode": 0,
                    "deinterlace_field_order": 0,
                    "monitoring_type": 0,
                    "private_settings": {{}}
                }}
            ]
        }},
        {{
            "prev_ver": 503382018,
            "name": "Left Score 2",
            "uuid": "f7742ed6-c8b1-4db7-8627-b6b33f2e9dd7",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "outline": false,
                "read_from_file": true,
                "text": "2",
                "undo_sname": "Left Score",
                "file": "{pathin}/scoreHome.txt",
                "font": {{
                    "face": "Century Gothic",
                    "style": "Bold",
                    "size": 56,
                    "flags": 1
                }},
                "outline_size": 7,
                "outline_color": 4278190080
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Right Score 2",
            "uuid": "820be9c0-cc29-4dc7-9f25-7c55cfeccb12",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "chatlog": false,
                "extents": false,
                "outline": false,
                "read_from_file": true,
                "text": "10000",
                "undo_sname": "Right Score",
                "file": "{pathin}/scoreAway.txt",
                "font": {{
                    "face": "Century Gothic",
                    "style": "Bold",
                    "size": 56,
                    "flags": 1
                }},
                "outline_size": 7,
                "outline_color": 4278190080,
                "antialiasing": true
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Middle 2",
            "uuid": "bbd196f5-047d-4c06-ac6e-7b8ba6fead86",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "outline": false,
                "text": "-",
                "font": {{
                    "face": "Century Gothic",
                    "style": "Bold",
                    "size": 56,
                    "flags": 1
                }},
                "outline_size": 7,
                "outline_color": 4278190080
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Best Of 2",
            "uuid": "04f344af-879e-41f7-ab18-a22feb81d91d",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "outline": false,
                "undo_sname": "Best Of",
                "text": "BEST OF 3",
                "font": {{
                    "face": "Century Gothic",
                    "style": "Bold",
                    "size": 28,
                    "flags": 1
                }},
                "align": "left",
                "valign": "top",
                "color": 16777215,
                "opacity": 100,
                "gradient_color": 16777215,
                "gradient_opacity": 100,
                "gradient_dir": 90,
                "bk_color": 0,
                "bk_opacity": 0,
                "outline_size": 7,
                "outline_color": 4278190080,
                "outline_opacity": 100,
                "chatlog_lines": 6,
                "extents_wrap": true,
                "extents_cx": 100,
                "extents_cy": 100,
                "transform": 0,
                "antialiasing": true
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Ticker Text",
            "uuid": "50bcd47d-7a30-4206-bc09-732f141e585c",
            "id": "text_gdiplus",
            "versioned_id": "text_gdiplus_v2",
            "settings": {{
                "drop_shadow": true,
                "file": "{pathin}/teamName.txt",
                "from_file": true,
                "outline": false,
                "read_from_file": false,
                "text_file": "E:/!Videos Or Streaming/Streaming Stuff/OSL Stats/Statsheet/teams/rightTeam/teamName.txt",
                "undo_sname": "Right Text",
                "vertical": false,
                "font": {{
                    "face": "Century Gothic",
                    "style": "Bold",
                    "size": 48,
                    "flags": 1
                }},
                "transform": 1,
                "text": "    |    Want to play slapshot? Come join the OSL! - discord.gg/OSL    |    Commentary by CowArmy33    |    Check out the Official OSL Youtube channel: @OSL-Slapshot    |    Slapshot super saturday signups out now!"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}},
            "filters": [
                {{
                    "prev_ver": 503382018,
                    "name": "Scroll",
                    "uuid": "1e280650-4126-4261-a7ee-782d63628134",
                    "id": "scroll_filter",
                    "versioned_id": "scroll_filter",
                    "settings": {{
                        "speed_x": 37.0,
                        "limit_cx": true,
                        "cx": 2020
                    }},
                    "mixers": 0,
                    "sync": 0,
                    "flags": 0,
                    "volume": 1.0,
                    "balance": 0.5,
                    "enabled": true,
                    "muted": false,
                    "push-to-mute": false,
                    "push-to-mute-delay": 0,
                    "push-to-talk": false,
                    "push-to-talk-delay": 0,
                    "hotkeys": {{}},
                    "deinterlace_mode": 0,
                    "deinterlace_field_order": 0,
                    "monitoring_type": 0,
                    "private_settings": {{}}
                }}
            ]
        }},
        {{
            "prev_ver": 503382018,
            "name": "Audio Output Capture",
            "uuid": "d52a078b-9ed9-44f5-b01b-646b27b77768",
            "id": "wasapi_output_capture",
            "versioned_id": "wasapi_output_capture",
            "settings": {{
                "device_id": "default"
            }},
            "mixers": 255,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.mute": [],
                "libobs.unmute": [],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Display Capture 2",
            "uuid": "940fb243-3f08-42a4-804f-ffdee50a21df",
            "id": "monitor_capture",
            "versioned_id": "monitor_capture",
            "settings": {{
                "monitor_id": "\\\\?\\DISPLAY#AOC2702#5&d4bdda8&1&UID176389#{{e6f07b5f-ee97-4a90-b076-33f57bf4eaa7}}"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Browser",
            "uuid": "22c6eb60-8391-48a1-807c-d0a5d1ece151",
            "id": "browser_source",
            "versioned_id": "browser_source",
            "settings": {{
                "is_local_file": true,
                "local_file": "{pathin}/schedule.html",
                "url": "file:///h%3A/%21Personal%20Projects/Slap%20Streaming%20Toll%20Python%20Port/Outputs/board.html",
                "width": 1920,
                "height": 500,
                "shutdown": true,
                "restart_when_active": true
            }},
            "mixers": 255,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.mute": [],
                "libobs.unmute": [],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": [],
                "ObsBrowser.Refresh": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "StatBoardBrowser",
            "uuid": "7154e16e-f452-452e-abd0-9a547bb34d00",
            "id": "browser_source",
            "versioned_id": "browser_source",
            "settings": {{
                "is_local_file": true,
                "local_file": "{pathin}/board.html",
                "width": 1500,
                "height": 800,
                "shutdown": true,
                "restart_when_active": true
            }},
            "mixers": 255,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.mute": [],
                "libobs.unmute": [],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": [],
                "ObsBrowser.Refresh": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Super Saturday Ad",
            "uuid": "658082aa-678c-4f5b-bf81-cd87c40fd6be",
            "id": "image_source",
            "versioned_id": "image_source",
            "settings": {{
                "file": "{pathin}/super saturday.png"
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }}
    ],
    "groups": [
        {{
            "prev_ver": 503382018,
            "name": "Game #3",
            "uuid": "e42d976c-9dc6-4f84-b21f-df7ce6a84fb7",
            "id": "group",
            "versioned_id": "group",
            "settings": {{
                "custom_size": true,
                "cx": 1920,
                "cy": 184,
                "id_counter": 0,
                "items": [
                    {{
                        "name": "Game Time 3",
                        "source_uuid": "dcecabec-939e-4e02-86a4-ca5c291bd2cb",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1653.0,
                            "y": 1.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 267.0,
                            "y": 183.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 25,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Match Logo Right 3",
                        "source_uuid": "81618301-32d0-43f4-a207-da371f025c4f",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1379.0,
                            "y": 12.0
                        }},
                        "scale": {{
                            "x": 0.30236220359802246,
                            "y": 0.30206379294395447
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 273.0,
                            "y": 158.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 18,
                        "group_item_backup": false,
                        "scale_filter": "bilinear",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Team Name R 3",
                        "source_uuid": "da485504-9d08-4342-a533-5ee96a230019",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1004.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 364.0,
                            "y": 183.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 31,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Team Name L 3",
                        "source_uuid": "3673d563-b2f7-418e-b810-60fcf8f22e85",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 552.0,
                            "y": 1.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 364.0,
                            "y": 183.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 32,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Match Logo Left 3",
                        "source_uuid": "fd7fa8fa-3bbb-472a-9e5c-dc1bf35b33c5",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 267.0,
                            "y": 12.0
                        }},
                        "scale": {{
                            "x": 0.30236220359802246,
                            "y": 0.30206379294395447
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 273.0,
                            "y": 158.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 16,
                        "group_item_backup": false,
                        "scale_filter": "bilinear",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Game Num 3",
                        "source_uuid": "87a7928c-4d29-4344-a0ac-c6657e4e6878",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 1.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 267.0,
                            "y": 183.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 7,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.show_scene_item.25": [],
                "libobs.hide_scene_item.25": [],
                "libobs.show_scene_item.18": [],
                "libobs.hide_scene_item.18": [],
                "libobs.show_scene_item.31": [],
                "libobs.hide_scene_item.31": [],
                "libobs.show_scene_item.32": [],
                "libobs.hide_scene_item.32": [],
                "libobs.show_scene_item.16": [],
                "libobs.hide_scene_item.16": [],
                "libobs.show_scene_item.7": [],
                "libobs.hide_scene_item.7": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Game #2",
            "uuid": "a1b7ce7d-abbf-410e-b73e-160675ed1a72",
            "id": "group",
            "versioned_id": "group",
            "settings": {{
                "custom_size": true,
                "cx": 1919,
                "cy": 184,
                "id_counter": 0,
                "items": [
                    {{
                        "name": "Game Time 2",
                        "source_uuid": "3275f904-4ffc-4104-b944-06a85e5f5277",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1652.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 267.0,
                            "y": 183.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 24,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Match Logo Right 2",
                        "source_uuid": "18348e45-ea23-4f92-aa76-65b710dc62be",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1379.0,
                            "y": 12.0
                        }},
                        "scale": {{
                            "x": 0.30236220359802246,
                            "y": 0.30206379294395447
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 273.0,
                            "y": 158.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 17,
                        "group_item_backup": false,
                        "scale_filter": "bilinear",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Team Name R 2",
                        "source_uuid": "ef0ac7ef-8655-4b39-9365-121776c00f9c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1004.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 364.0,
                            "y": 183.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 29,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Team Name L 2",
                        "source_uuid": "0e104feb-6409-4a4d-a4e7-15823ff1bae6",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 552.0,
                            "y": 1.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 364.0,
                            "y": 183.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 30,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Match Logo Left 2",
                        "source_uuid": "b8f05595-200d-4aed-aa3b-5278916a3fd9",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 267.0,
                            "y": 12.0
                        }},
                        "scale": {{
                            "x": 0.30236220359802246,
                            "y": 0.30206379294395447
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 273.0,
                            "y": 158.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 15,
                        "group_item_backup": false,
                        "scale_filter": "bilinear",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Game Num 2",
                        "source_uuid": "574f7b32-d69a-438f-a8b7-a4c2987ef35f",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 267.0,
                            "y": 183.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 10,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.show_scene_item.24": [],
                "libobs.hide_scene_item.24": [],
                "libobs.show_scene_item.17": [],
                "libobs.hide_scene_item.17": [],
                "libobs.show_scene_item.29": [],
                "libobs.hide_scene_item.29": [],
                "libobs.show_scene_item.30": [],
                "libobs.hide_scene_item.30": [],
                "libobs.show_scene_item.15": [],
                "libobs.hide_scene_item.15": [],
                "libobs.show_scene_item.10": [],
                "libobs.hide_scene_item.10": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Game #1",
            "uuid": "09d5d84f-c1da-40cd-aa96-8cdc7215d853",
            "id": "group",
            "versioned_id": "group",
            "settings": {{
                "custom_size": true,
                "cx": 1920,
                "cy": 190,
                "id_counter": 0,
                "items": [
                    {{
                        "name": "Game Time 1",
                        "source_uuid": "648a9ef9-263b-41ab-91fc-013110f154f0",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1653.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 267.0,
                            "y": 183.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 23,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Match Logo Right 1",
                        "source_uuid": "409c7aeb-1981-4f08-9375-529721ae03aa",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1379.0,
                            "y": 12.0
                        }},
                        "scale": {{
                            "x": 0.30236220359802246,
                            "y": 0.30206379294395447
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 274.0,
                            "y": 158.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 19,
                        "group_item_backup": false,
                        "scale_filter": "bilinear",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Team Name R 1",
                        "source_uuid": "158d5e1e-bb1e-4158-8485-cccde9547879",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1004.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 364.0,
                            "y": 183.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 28,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Team Name L 1",
                        "source_uuid": "a51aa3e3-048c-432f-8eaf-6ca817ffa80d",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 552.0,
                            "y": 1.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 364.0,
                            "y": 183.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 27,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Match Logo Left 1",
                        "source_uuid": "3a6e3fd8-68d7-40be-b797-5aa89a12a176",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 267.0,
                            "y": 12.0
                        }},
                        "scale": {{
                            "x": 0.30236220359802246,
                            "y": 0.30206379294395447
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 274.0,
                            "y": 158.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 14,
                        "group_item_backup": false,
                        "scale_filter": "bilinear",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Game Num 1",
                        "source_uuid": "70b4dda3-9a9e-4e4b-932f-9f9cb80b18a2",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 7.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 267.0,
                            "y": 183.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 9,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.show_scene_item.23": [],
                "libobs.hide_scene_item.23": [],
                "libobs.show_scene_item.19": [],
                "libobs.hide_scene_item.19": [],
                "libobs.show_scene_item.28": [],
                "libobs.hide_scene_item.28": [],
                "libobs.show_scene_item.27": [],
                "libobs.hide_scene_item.27": [],
                "libobs.show_scene_item.14": [],
                "libobs.hide_scene_item.14": [],
                "libobs.show_scene_item.9": [],
                "libobs.hide_scene_item.9": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Background",
            "uuid": "c090dfd8-4311-495c-8cff-13571d009647",
            "id": "group",
            "versioned_id": "group",
            "settings": {{
                "custom_size": true,
                "cx": 505,
                "cy": 95,
                "id_counter": 0,
                "items": [
                    {{
                        "name": "ScoreBack",
                        "source_uuid": "90c73104-8759-475a-a52f-11dc626da959",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 0.55523425340652466,
                            "y": 0.55517476797103882
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 27,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "ScoreFront",
                        "source_uuid": "b9d25a44-5905-4a2f-a156-b7315330424a",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 0.55523425340652466,
                            "y": 0.55517476797103882
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 28,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.show_scene_item.27": [],
                "libobs.hide_scene_item.27": [],
                "libobs.show_scene_item.28": [],
                "libobs.hide_scene_item.28": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Long score lol",
            "uuid": "9542250f-bd68-4e80-a5c8-c34ab0924e76",
            "id": "group",
            "versioned_id": "group",
            "settings": {{
                "custom_size": true,
                "cx": 0,
                "cy": 0,
                "id_counter": 0,
                "items": []
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{}},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Elements",
            "uuid": "096ecadd-bef5-4341-8bf3-190ad7384771",
            "id": "group",
            "versioned_id": "group",
            "settings": {{
                "custom_size": true,
                "cx": 2552,
                "cy": 471,
                "id_counter": 0,
                "items": [
                    {{
                        "name": "Left Logo",
                        "source_uuid": "b31bc3c2-c8f8-4a0d-a423-04fdbabaa8c0",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 424.0,
                            "y": 2.0
                        }},
                        "scale": {{
                            "x": 0.38222211599349976,
                            "y": 0.38319912552833557
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 399.0,
                            "y": 365.625
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 1,
                        "group_item_backup": false,
                        "scale_filter": "bilinear",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Right Logo",
                        "source_uuid": "96e8db6f-2029-460f-973e-aee47e99fc7c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1717.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 0.49250000715255737,
                            "y": 0.49250000715255737
                        }},
                        "align": 5,
                        "bounds_type": 2,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 408.0,
                            "y": 351.625
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 2,
                        "group_item_backup": false,
                        "scale_filter": "bilinear",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Left Text",
                        "source_uuid": "b99d0e62-4d9a-40d6-a619-95df24f1f639",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 615.0,
                            "y": 415.0
                        }},
                        "scale": {{
                            "x": 3.8743946552276611,
                            "y": 3.875
                        }},
                        "align": 0,
                        "bounds_type": 6,
                        "bounds_align": 8,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1230.130615234375,
                            "y": 110.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 29,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Right Text",
                        "source_uuid": "0367b2db-b567-44ce-8c90-1a4ca8850aca",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1316.0,
                            "y": 361.0
                        }},
                        "scale": {{
                            "x": 3.874394416809082,
                            "y": 3.875
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 8,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1235.551025390625,
                            "y": 110.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 30,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.show_scene_item.1": [],
                "libobs.hide_scene_item.1": [],
                "libobs.show_scene_item.2": [],
                "libobs.hide_scene_item.2": [],
                "libobs.show_scene_item.29": [],
                "libobs.hide_scene_item.29": [],
                "libobs.show_scene_item.30": [],
                "libobs.hide_scene_item.30": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Scores",
            "uuid": "07086113-4b0d-444a-bf60-40a5458b3677",
            "id": "group",
            "versioned_id": "group",
            "settings": {{
                "custom_size": true,
                "cx": 665,
                "cy": 337,
                "id_counter": 0,
                "items": [
                    {{
                        "name": "Left Score",
                        "source_uuid": "81e2c3c8-eac6-416e-a2db-07aea7730030",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 75.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 3,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Right Score",
                        "source_uuid": "680b1eed-2ea6-4111-ac9f-73838907eeb8",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 544.9998779296875,
                            "y": 75.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 5,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Middle",
                        "source_uuid": "bee309be-495b-4a20-ad5e-fb4646875001",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 333.0001220703125,
                            "y": 75.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 4,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 6,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Best Of",
                        "source_uuid": "7139dd99-b8e9-4533-b13b-754ca06f72be",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 334.1810302734375,
                            "y": 61.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 0,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 21,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.show_scene_item.3": [],
                "libobs.hide_scene_item.3": [],
                "libobs.show_scene_item.5": [],
                "libobs.hide_scene_item.5": [],
                "libobs.show_scene_item.6": [],
                "libobs.hide_scene_item.6": [],
                "libobs.show_scene_item.21": [],
                "libobs.hide_scene_item.21": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Nested",
            "uuid": "20af7571-0bed-4550-a3f8-77ae99188b0f",
            "id": "group",
            "versioned_id": "group",
            "settings": {{
                "custom_size": true,
                "cx": 1920,
                "cy": 1080,
                "id_counter": 0,
                "items": [
                    {{
                        "name": "[NS] Background",
                        "source_uuid": "f3da34e6-1ba4-4980-a925-2639f7bda1cc",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 6,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.show_scene_item.6": [],
                "libobs.hide_scene_item.6": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Caster Setup",
            "uuid": "4bb05f72-5ed2-4465-bf77-b7c92c741c46",
            "id": "group",
            "versioned_id": "group",
            "settings": {{
                "custom_size": true,
                "cx": 474,
                "cy": 669,
                "id_counter": 0,
                "items": [
                    {{
                        "name": "Caster Frame",
                        "source_uuid": "efe75205-f7f9-4f0f-9206-47408bf5ef08",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 13,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Casters",
                        "source_uuid": "8d5d9598-e3c9-42d4-b072-8ecc0c0e89db",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 59.0,
                            "y": 125.0
                        }},
                        "scale": {{
                            "x": 1.0885714292526245,
                            "y": 1.0880000591278076
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 18,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.show_scene_item.13": [],
                "libobs.hide_scene_item.13": [],
                "libobs.show_scene_item.18": [],
                "libobs.hide_scene_item.18": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Discord Link",
            "uuid": "f2f5e807-beb9-4e3d-9d45-a287984599e9",
            "id": "group",
            "versioned_id": "group",
            "settings": {{
                "custom_size": true,
                "cx": 367,
                "cy": 168,
                "id_counter": 0,
                "items": [
                    {{
                        "name": "Discord Box Back",
                        "source_uuid": "f1c6105f-819f-442e-bc9f-23d1bed3be98",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 16,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord Invite Link",
                        "source_uuid": "056ad710-8177-4fe4-ab8e-2e33c5cf7759",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 10.0,
                            "y": 11.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 17,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Discord Box Frame",
                        "source_uuid": "17b335cb-ddd9-43bf-8cd3-6b017b716816",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 15,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.show_scene_item.16": [],
                "libobs.hide_scene_item.16": [],
                "libobs.show_scene_item.17": [],
                "libobs.hide_scene_item.17": [],
                "libobs.show_scene_item.15": [],
                "libobs.hide_scene_item.15": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Ticker",
            "uuid": "03531d4f-e2b0-4503-b2c0-8e0c2db3c9b6",
            "id": "group",
            "versioned_id": "group",
            "settings": {{
                "id_counter": 0,
                "custom_size": true,
                "cx": 1934,
                "cy": 1080,
                "items": [
                    {{
                        "name": "TickerBG",
                        "source_uuid": "c3b1a8ca-9df6-4ebc-84bf-5decc9b249e4",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 30,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Ticker Text",
                        "source_uuid": "50bcd47d-7a30-4206-bc09-732f141e585c",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 199.39999389648438,
                            "y": 1019.0
                        }},
                        "scale": {{
                            "x": 0.85850000381469727,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 32,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.show_scene_item.30": [],
                "libobs.hide_scene_item.30": [],
                "libobs.show_scene_item.32": [],
                "libobs.hide_scene_item.32": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }},
        {{
            "prev_ver": 503382018,
            "name": "Series Points",
            "uuid": "47293b10-504d-4a96-a1f9-40b5af76b45c",
            "id": "group",
            "versioned_id": "group",
            "settings": {{
                "id_counter": 0,
                "custom_size": true,
                "cx": 1920,
                "cy": 1080,
                "items": [
                    {{
                        "name": "SC2",
                        "source_uuid": "51e9ddfd-cf12-4440-8863-071e5275946b",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 0,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 0.0,
                            "y": 0.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 11,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Left Text 2",
                        "source_uuid": "fc6bdd2a-26f1-44fd-bc48-60bb5c93136e",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 685.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 193.0,
                            "y": 86.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 14,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Right Text 3",
                        "source_uuid": "07070643-cf4a-4cbd-bdfe-f27acd6c82a4",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 1042.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 193.0,
                            "y": 86.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 15,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Left Score 2",
                        "source_uuid": "f7742ed6-c8b1-4db7-8627-b6b33f2e9dd7",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 878.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 47.0,
                            "y": 86.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 16,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Right Score 2",
                        "source_uuid": "820be9c0-cc29-4dc7-9f25-7c55cfeccb12",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 996.0,
                            "y": 1.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 47.0,
                            "y": 85.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 17,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Middle 2",
                        "source_uuid": "bbd196f5-047d-4c06-ac6e-7b8ba6fead86",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 924.0,
                            "y": 0.0
                        }},
                        "scale": {{
                            "x": 1.0,
                            "y": 1.0
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 72.0,
                            "y": 86.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 18,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }},
                    {{
                        "name": "Best Of 2",
                        "source_uuid": "04f344af-879e-41f7-ab18-a22feb81d91d",
                        "visible": true,
                        "locked": false,
                        "rot": 0.0,
                        "pos": {{
                            "x": 906.0,
                            "y": 86.0
                        }},
                        "scale": {{
                            "x": 1.0370370149612427,
                            "y": 1.0333333015441895
                        }},
                        "align": 5,
                        "bounds_type": 6,
                        "bounds_align": 0,
                        "bounds_crop": false,
                        "bounds": {{
                            "x": 108.0,
                            "y": 31.0
                        }},
                        "crop_left": 0,
                        "crop_top": 0,
                        "crop_right": 0,
                        "crop_bottom": 0,
                        "id": 19,
                        "group_item_backup": false,
                        "scale_filter": "disable",
                        "blend_method": "default",
                        "blend_type": "normal",
                        "show_transition": {{
                            "duration": 0
                        }},
                        "hide_transition": {{
                            "duration": 0
                        }},
                        "private_settings": {{}}
                    }}
                ]
            }},
            "mixers": 0,
            "sync": 0,
            "flags": 0,
            "volume": 1.0,
            "balance": 0.5,
            "enabled": true,
            "muted": false,
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "hotkeys": {{
                "libobs.show_scene_item.11": [],
                "libobs.hide_scene_item.11": [],
                "libobs.show_scene_item.14": [],
                "libobs.hide_scene_item.14": [],
                "libobs.show_scene_item.15": [],
                "libobs.hide_scene_item.15": [],
                "libobs.show_scene_item.16": [],
                "libobs.hide_scene_item.16": [],
                "libobs.show_scene_item.17": [],
                "libobs.hide_scene_item.17": [],
                "libobs.show_scene_item.18": [],
                "libobs.hide_scene_item.18": [],
                "libobs.show_scene_item.19": [],
                "libobs.hide_scene_item.19": []
            }},
            "deinterlace_mode": 0,
            "deinterlace_field_order": 0,
            "monitoring_type": 0,
            "private_settings": {{}}
        }}
    ],
    "quick_transitions": [
        {{
            "name": "Cut",
            "duration": 300,
            "hotkeys": [],
            "id": 1,
            "fade_to_black": false
        }},
        {{
            "name": "Fade",
            "duration": 300,
            "hotkeys": [],
            "id": 2,
            "fade_to_black": false
        }},
        {{
            "name": "Fade",
            "duration": 300,
            "hotkeys": [],
            "id": 3,
            "fade_to_black": true
        }},
        {{
            "name": "Slapshot Transition",
            "duration": 300,
            "hotkeys": [],
            "id": 4,
            "fade_to_black": false
        }}
    ],
    "transitions": [
        {{
            "name": "Slapshot Transition",
            "id": "obs_stinger_transition",
            "settings": {{
                "audio_fade_style": 1,
                "audio_monitoring": 0,
                "path": "{pathin}/OSL Transition_1.webm",
                "tp_type": 1,
                "track_matte_enabled": true,
                "transition_point": 70,
                "hw_decode": true
            }}
        }}
    ],
    "saved_projectors": [],
    "current_transition": "Slapshot Transition",
    "transition_duration": 500,
    "preview_locked": false,
    "scaling_enabled": false,
    "scaling_level": 8,
    "scaling_off_x": 0.0,
    "scaling_off_y": 0.0,
    "virtual-camera": {{
        "type2": 3
    }},
    "modules": {{
        "scripts-tool": [],
        "output-timer": {{
            "streamTimerHours": 0,
            "streamTimerMinutes": 0,
            "streamTimerSeconds": 30,
            "recordTimerHours": 0,
            "recordTimerMinutes": 0,
            "recordTimerSeconds": 30,
            "autoStartStreamTimer": false,
            "autoStartRecordTimer": false,
            "pauseRecordTimer": true
        }},
        "auto-scene-switcher": {{
            "interval": 300,
            "non_matching_scene": "",
            "switch_if_not_matching": false,
            "active": false,
            "switches": []
        }},
        "captions": {{
            "source": "",
            "enabled": false,
            "lang_id": 2057,
            "provider": "mssapi"
        }},
        "advanced-scene-switcher": {{
            "sceneGroups": [],
            "macros": [],
            "macroProperties": {{
                "highlightExecuted": false,
                "highlightConditions": false,
                "highlightActions": false,
                "newMacroRegisterHotkey": false
            }},
            "variables": [],
            "switches": [],
            "ignoreWindows": [],
            "screenRegion": [],
            "pauseEntries": [],
            "sceneRoundTrip": [],
            "sceneTransitions": [],
            "defaultTransitions": [],
            "defTransitionDelay": 0,
            "ignoreIdleWindows": [],
            "idleTargetType": 0,
            "idleSceneName": "",
            "idleTransitionName": "",
            "idleEnable": false,
            "idleTime": 60,
            "executableSwitches": [],
            "randomSwitches": [],
            "fileSwitches": [],
            "readEnabled": false,
            "readPath": "",
            "writeEnabled": false,
            "writePath": "",
            "mediaSwitches": [],
            "timeSwitches": [],
            "audioSwitches": [],
            "audioFallbackTargetType": 0,
            "audioFallbackScene": "",
            "audioFallbackTransition": "",
            "audioFallbackEnable": false,
            "audioFallbackDuration": {{
                "value": {{
                    "value": 0.0,
                    "type": 0
                }},
                "unit": 0,
                "version": 1
            }},
            "videoSwitches": [],
            "ServerEnabled": false,
            "ServerPort": 55555,
            "LockToIPv4": false,
            "ClientEnabled": false,
            "Address": "",
            "ClientPort": 55555,
            "SendSceneChange": true,
            "SendSceneChangeAll": true,
            "SendPreview": true,
            "triggers": [],
            "interval": 300,
            "non_matching_scene": "",
            "switch_if_not_matching": 0,
            "noMatchDelay": {{
                "value": {{
                    "value": 0.0,
                    "type": 0
                }},
                "unit": 0,
                "version": 1
            }},
            "cooldown": {{
                "value": {{
                    "value": 0.0,
                    "type": 0
                }},
                "unit": 0,
                "version": 1
            }},
            "active": true,
            "startup_behavior": 0,
            "autoStartEvent": 0,
            "logLevel": 0,
            "showSystemTrayNotifications": false,
            "disableHints": false,
            "disableFilterComboboxFilter": false,
            "warnPluginLoadFailure": true,
            "hideLegacyTabs": true,
            "priority0": 10,
            "priority1": 0,
            "priority2": 2,
            "priority3": 8,
            "priority4": 6,
            "priority5": 9,
            "priority6": 7,
            "priority7": 4,
            "priority8": 1,
            "priority9": 5,
            "priority10": 3,
            "threadPriority": 3,
            "transitionOverrideOverride": false,
            "adjustActiveTransitionType": true,
            "lastImportPath": "",
            "startHotkey": [],
            "stopHotkey": [],
            "toggleHotkey": [],
            "upMacroSegmentHotkey": [],
            "downMacroSegmentHotkey": [],
            "removeMacroSegmentHotkey": [],
            "tabWidgetOrder": [
                {{
                    "generalTab": 0
                }},
                {{
                    "macroTab": 1
                }},
                {{
                    "variableTab": 2
                }},
                {{
                    "windowTitleTab": 3
                }},
                {{
                    "executableTab": 4
                }},
                {{
                    "screenRegionTab": 5
                }},
                {{
                    "mediaTab": 6
                }},
                {{
                    "fileTab": 7
                }},
                {{
                    "randomTab": 8
                }},
                {{
                    "timeTab": 9
                }},
                {{
                    "idleTab": 10
                }},
                {{
                    "sceneSequenceTab": 11
                }},
                {{
                    "audioTab": 12
                }},
                {{
                    "videoTab": 13
                }},
                {{
                    "networkTab": 14
                }},
                {{
                    "sceneGroupTab": 15
                }},
                {{
                    "transitionsTab": 16
                }},
                {{
                    "pauseTab": 17
                }},
                {{
                    "sceneTriggerTab": 18
                }}
            ],
            "saveWindowGeo": false,
            "windowPosX": 0,
            "windowPosY": 0,
            "windowWidth": 0,
            "windowHeight": 0,
            "macroListMacroEditSplitterPosition": [],
            "version": "cdacfc946c062982a5e865b9a4f849b5ce2fb05f",
            "websocketConnections": [],
            "twitchConnections": [],
            "actionQueues": []
        }}
    }},
    "resolution": {{
        "x": 1920,
        "y": 1080
    }}
}}
"""
def recursiveSearch(dir: str, target: str):
    files = listdir(dir)
    if target in files:
        return normpath(join(dir, target)).replace("\\", "/")
    else:
        rtValue = False
        for file in files:
            file = join(dir,file)
            if isdir(file): rtValue=recursiveSearch(file, target)
            if rtValue is not False: return rtValue
        return rtValue



base = input("Please provide the path to your base directory: ")


gradientLocation = recursiveSearch(base, "gradient.png")
colourHomeLocation = recursiveSearch(base, "colourHome.png")
colourAwayLocation = recursiveSearch(base, "colourAway.png")

locations = [gradientLocation,colourHomeLocation,colourAwayLocation]
if False not in locations:
    with open("template.json", "w") as f:
        f.write(template.format(pathin = normpath(base).replace("\\", "/"), colourHome=colourHomeLocation, colourAway=colourAwayLocation, gradient=gradientLocation))
else:
    print("Error has occured, could not find files")
    if gradientLocation is False:
        print("Can't find gradient.png in given folder")
    if colourHomeLocation is False:
        print("Can't find colourHome.png in given folder")
    if colourAwayLocation is False:
        print("Can't find colourAway.png in given folder")
    time.sleep(5)