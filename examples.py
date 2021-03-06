# Put JSON HERE

bw_chat_message = {
    'text': '',
    'strikethrough': False,
    'extra': [
        {
            'text': '§7[44✫] §b[MVP§9+§b] ByonPlays§f',
            'strikethrough': False,
            'clickEvent': {'action': 'run_command', 'value': '/viewprofile 880a651b-ffc1-460f-9f91-4449f069ab03'},
            'hoverEvent': {'action': 'show_text', 'value': {
                'text': "§b[MVP§9+§b] ByonPlays§f\n§7Hypixel Level: §6117\n§7Achievement Points: §e2,905\n§7Guild: §b§bNone\n\n§eClick to view §bByonPlays§e's profile!",
                'strikethrough': False}}
        },
        {
            'text': ': Need an active guild do /g join Team Voided (Level 83) Tag:✧VOID✧ Reqs: Network lvl 60 or 500 wins in BW. Must have Discord and get 100k weekly.',
            'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False, 'strikethrough': False,
            'color': 'white'}
    ]
}

friend_status = {'text': 'Friend > ', 'color': 'green',
                 'extra': [{'text': 'JqmmyYT ', 'color': 'green'}, {'text': 'left.', 'color': 'yellow'}]}

skywars_chat_message = {
    'text': '',
    'strikethrough': False,
    'extra': [
        {
            'text': '§7[6✫] §7pogleah§7',
            'strikethrough': False,
            'clickEvent': {'action': 'run_command', 'value': '/viewprofile ba1859c5-5c38-4e43-b448-660679f968fc'},
            'hoverEvent': {'action': 'show_text', 'value': {
                'text': "§7pogleah§7\n§7Hypixel Level: §612\n§7Achievement Points: §e360\n§7Guild: §b§bNone\n\n§eClick to view §7pogleah§e's profile!",
                'strikethrough': False}}
        },
        {'text': ': a', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False,
         'strikethrough': False, 'color': 'gray'}
    ]
}

# NOT ACTUALLY A LIST IT ARE 2 SEPERATE MESSAGES
watchdog_json = [
    {'italic': False, 'extra': [{'bold': True, 'color': 'red', 'text': 'A player has been removed from your lobby.'}],
     'text': ''},
    {'italic': False, 'extra': [{'color': 'aqua', 'text': 'Use /report to continue helping out the server!'}],
     'text': ''}
]


chat_message = {
    'text': '',
    'strikethrough': False,
    'extra': [
        {
            'text': '§7jenscc2006§7',
            'strikethrough': False,
            'clickEvent': {'action': 'run_command', 'value': '/viewprofile 5beb3dff-b44d-49af-8ad0-f35aecac9eb7'},
            'hoverEvent': {
                'action': 'show_text',
                'value': {'text': "§7jenscc2006§7\n§7Hypixel Level: §61\n§7Achievement Points: §e35\n§7Guild: §b§bNone\n\n§eClick to view §7jenscc2006§e's profile!", 'strikethrough': False}
            }
        },
        {'text': 'This is where the chat message is. Its not what jenscc2006 actually said. They made an emote and it was hard to see. Is this illegal?', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False, 'strikethrough': False, 'color': 'gray'}
    ]
}

important_mystery_box_opened = {
    'text': '[Mystery Box] ',
    'strikethrough': False,
    'color': 'aqua',
    'hoverEvent': {
        'action': 'show_text',
        'value': {
            'text': 'You can find ',
            'bold': False,
            'italic': False,
            'underlined': False,
            'obfuscated': False,
            'strikethrough': False,
            'color': 'gray',
            'extra': [
                {'text': 'Mystery Boxes ', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False, 'strikethrough': False, 'color': 'aqua'},
                {'text': 'by\n', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False, 'strikethrough': False, 'color': 'gray'},
                {'text': 'playing games on the server!', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False, 'strikethrough': False, 'color': 'gray'}
            ]
        }
    },
    'extra': [
        {
            'text': '§f§bFrost_alt §ffound a §6Legendary Thor Suit Head§f!',
            'strikethrough': False,
            'color': 'aqua',
            'hoverEvent': {
                'action': 'show_text',
                'value': {
                    'text': 'Type: ',
                    'bold': False,
                    'italic': False,
                    'underlined': False,
                    'obfuscated': False,
                    'strikethrough': False,
                    'color': 'gray',
                    'extra': [
                        {'text': 'Suit Pieces\n', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False, 'strikethrough': False, 'color': 'yellow'},
                        {'text': 'Rarity: ', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False,
                         'strikethrough': False, 'color': 'gray'},
                        {'text': 'Legendary', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False,
                         'strikethrough': False, 'color': 'gold'}
                    ]
                }
            }
        }
    ]
}

limbo_message = {'text': 'You are AFK. Move around to return from AFK.', 'color': 'red'}

quest_message = {
    'text': '§aAutomatically activated: §6Daily Quest: First Win of the Day',
    'strikethrough': False,
    'color': 'green',
    'hoverEvent': {
        'action': 'show_text',
        'value': {
            'text': 'Daily Quest: First Win of the Day\n',
            'bold': False,
            'italic': False,
            'underlined': False,
            'obfuscated': False,
            'strikethrough': False,
            'color': 'green',
            'extra': [{'text': 'Win a game of Bed Wars', 'bold': False, 'italic': False, 'underlined': False,
                       'obfuscated': False, 'strikethrough': False, 'color': 'gray'}]
        }
    }
}

mystery_box_rare_item = {
    'text': '[Mystery Box] ',
    'strikethrough': False,
    'color': 'aqua',
    'hoverEvent': {
        'action': 'show_text',
        'value': {
            'text': 'You can find ',
            'bold': False,
            'italic': False,
            'underlined': False,
            'obfuscated': False,
            'strikethrough': False,
            'color': 'gray',
            'extra': [
                {'text': 'Mystery Boxes ', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False,
                 'strikethrough': False, 'color': 'aqua'},
                {'text': 'by\n', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False,
                 'strikethrough': False, 'color': 'gray'},
                {'text': 'playing games on the server!', 'bold': False, 'italic': False, 'underlined': False,
                 'obfuscated': False, 'strikethrough': False, 'color': 'gray'}
            ]
        }
    },
    'extra': [
        {
            'text': '§f§aPinguinKeks6522 §ffound a §5Epic Wave Dance Gesture§f!',
            'strikethrough': False,
            'color': 'aqua',
            'hoverEvent': {
                'action': 'show_text',
                'value': {
                    'text': 'Type: ',
                    'bold': False,
                    'italic': False,
                    'underlined': False,
                    'obfuscated': False,
                    'strikethrough': False,
                    'color': 'gray',
                    'extra': [
                        {'text': 'Gestures\n', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False,
                         'strikethrough': False, 'color': 'yellow'},
                        {'text': 'Rarity: ', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False,
                         'strikethrough': False, 'color': 'gray'},
                        {'text': 'Epic', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False,
                         'strikethrough': False, 'color': 'dark_purple'}
                    ]
                }
            }
        }
    ]
}

friend_list = {
    'text': '-----------------------------------------------------',
    'color': 'blue',
    'strikethrough': False,
    'extra': [
        {'text': '\n', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False,
         'strikethrough': False},
        {'text': '                         ', 'strikethrough': False},
        {'text': ' §6Friends (Page 1 of 28) ', 'strikethrough': False},
        {'text': '>>', 'color': 'yellow', 'bold': True, 'strikethrough': False,
         'clickEvent': {'action': 'run_command', 'value': '/f list 2'}, 'hoverEvent': {'action': 'show_text', 'value': {
            'text': 'Click to view page 2', 'color': 'yellow', 'strikethrough': False}}},
        {'text': '\n', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False,
         'strikethrough': False},
        {'text': '§b3p0', 'strikethrough': False,
         'clickEvent': {'action': 'run_command', 'value': '/viewprofile ecfc88ec-539f-49a5-be2a-6bfdaaa4563b'},
         'hoverEvent': {'action': 'show_text',
                        'value': {'text': "§eClick here to view §b3p0§e's profile", 'strikethrough': False}}},
        {'text': ' is in the house Relaxed Parkour / PVP', 'color': 'yellow', 'bold': False, 'italic': False,
         'underlined': False, 'obfuscated': False, 'strikethrough': False},
        {'text': '\n', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False,
         'strikethrough': False},
        {'text': '§bBlockyFacts', 'strikethrough': False,
         'clickEvent': {'action': 'run_command', 'value': '/viewprofile 11ba42c6-8486-48d3-8fce-94c48dab66d3'},
         'hoverEvent': {'action': 'show_text',
                        'value': {'text': "§eClick here to view §bBlockyFacts§e's profile", 'strikethrough': False}}},
        {'text': ' is playing SMP', 'color': 'yellow', 'bold': False, 'italic': False, 'underlined': False,
         'obfuscated': False, 'strikethrough': False},
        {'text': '\n', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False,
         'strikethrough': False},
        {'text': '§bCarsteel', 'strikethrough': False,
         'clickEvent': {'action': 'run_command', 'value': '/viewprofile 9c372df7-f7d2-4c44-a600-73bb5c2b281b'},
         'hoverEvent': {'action': 'show_text',
                        'value': {'text': "§eClick here to view §bCarsteel§e's profile", 'strikethrough': False}}},
        {'text': ' is in a Bed Wars Game', 'color': 'yellow', 'bold': False, 'italic': False, 'underlined': False,
         'obfuscated': False, 'strikethrough': False},
        {'text': '\n', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False,
         'strikethrough': False},
        {'text': '§aGodCow', 'strikethrough': False,
         'clickEvent': {'action': 'run_command', 'value': '/viewprofile 019a851b-a524-4cbc-8a24-fb7352576a53'},
         'hoverEvent': {'action': 'show_text',
                        'value': {'text': "§eClick here to view §aGodCow§e's profile", 'strikethrough': False}}},
        {'text': ' is in a Bed Wars Lobby', 'color': 'yellow', 'bold': False, 'italic': False, 'underlined': False,
         'obfuscated': False, 'strikethrough': False},
        {'text': '\n', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False,
         'strikethrough': False},
        {'text': '§6Grownupish', 'strikethrough': False,
         'clickEvent': {'action': 'run_command', 'value': '/viewprofile 4a39517e-4022-4ba8-af3b-c68f45371a20'},
         'hoverEvent': {'action': 'show_text',
                        'value': {'text': "§eClick here to view §6Grownupish§e's profile", 'strikethrough': False}}},
        {'text': ' is in SkyBlock - Private Island', 'color': 'yellow', 'bold': False, 'italic': False,
         'underlined': False, 'obfuscated': False, 'strikethrough': False},
        {'text': '\n', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False,
         'strikethrough': False},
        {'text': '§bHuade', 'strikethrough': False,
         'clickEvent': {'action': 'run_command', 'value': '/viewprofile 31aba356-a01c-46d6-90ef-ec07800dcd19'},
         'hoverEvent': {'action': 'show_text',
                        'value': {'text': "§eClick here to view §bHuade§e's profile", 'strikethrough': False}}},
        {'text': ' is in a SkyWars Lobby', 'color': 'yellow', 'bold': False, 'italic': False, 'underlined': False,
         'obfuscated': False, 'strikethrough': False},
        {'text': '\n', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False,
         'strikethrough': False},
        {'text': '§6jqnnick', 'strikethrough': False,
         'clickEvent': {'action': 'run_command', 'value': '/viewprofile e7e775a1-4c45-4d30-b532-bca4d7e00272'},
         'hoverEvent': {'action': 'show_text',
                        'value': {'text': "§eClick here to view §6jqnnick§e's profile", 'strikethrough': False}}},
        {'text': ' is in a Build Battle Game', 'color': 'yellow', 'bold': False, 'italic': False, 'underlined': False,
         'obfuscated': False, 'strikethrough': False},
        {'text': '\n', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False,
         'strikethrough': False},
        {'text': '§bLarissaahh', 'strikethrough': False,
         'clickEvent': {'action': 'run_command', 'value': '/viewprofile 6c4aed84-bd67-44ea-befb-dcd18eda86ad'},
         'hoverEvent': {'action': 'show_text',
                        'value': {'text': "§eClick here to view §bLarissaahh§e's profile", 'strikethrough': False}}},
        {'text': ' is in a TNT Games Game', 'color': 'yellow', 'bold': False, 'italic': False, 'underlined': False,
         'obfuscated': False, 'strikethrough': False},
        {'text': '\n', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False,
         'strikethrough': False},
        {'text': '-----------------------------------------------------', 'color': 'blue', 'strikethrough': False}
    ]
}
