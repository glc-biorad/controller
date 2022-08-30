'''
DESCRIPTION:
This module contains a data structure of commands based on module and command.

AUTHOR:
G.LC

AFFILIATION:
Bio-Rad, CDG, Advanced-Tech Team

CREATED ON:
8/30/2022
'''

commands = {
    'UpperGantry' : {
        'Pipettor-X' : {
            'home' : b'>01,0,home,<CR>\n',
            'mabs' : b'>01,0,mabs,target,speed,<CR>\n'
            },
        'Pipettor-Y' : {
            'home' : b'>02,0,home,<CR>\n',
            'mabs' : b'>02,0,mabs,target,speed,<CR>\n'
            },
        'Pipettor-Z' : {
            'home' : b'>03,0,home,<CR>\n',
            'mabs' : b'>03,0,mabs,target,speed,<CR>\n'
            },
        'Drip Plate' : {
            'home' : b'>04,0,home,<CR>\n',
            'mabs' : b''
            },
        'Air Module' : {}
        },
    'Prep Deck' : {
        'Mag Separator' : {}
        },
    'Reader' : {
        'X Axis' : {
            'home' : b'>06,0,home,<CR>\n',
            'mabs' : b'>06,0,mabs,target,speed,<CR>\n'
            },
        'Y Axis' : {
            'home' : b'>07,0,home,<CR>\n',
            'mabs' : b'>07,0,mabs,target,speed,<CR>\n'
            },
        'Z Axis' : {
            'home' : b'>08,0,home,<CR>\n',
            'mabs' : b'>08,0,mabs,target,speed,<CR>\n'
            },
        'Filter Wheel' : {
            'home' : b'>09,0,home,<CR>\n',
            'mabs' : b''
            },
        'LED' : {},
        'Front Tray' : {
            'home' : b'>0B,0,home,<CR>\n',
            'mabs' : b''
            },
        'Rear Tray' : {
            'home' : b'>0C,0,home,<CR>\n',
            'mabs' : b''
            },
        'Heater Front-1' : {
            'home' : b'>0D,0,home,<CR>\n',
            'mabs' : b''
            },
        'Heater Front-2' : {
            'home' : b'>0E,0,home,<CR>\n',
            'mabs' : b''
            },
        'Heater Rear-1' : {
            'home' : b'>0F,0,home,<CR>\n',
            'mabs' : b''
            },
        'Heater Rear-2' : {
            'home' : b'>10,0,home,<CR>\n',
            'mabs' : b''
            }
        }
    }

commands_deprecated = {
    'motor' : {
        'home' : {
            'X' : b'>01,0,home,<CR>\n',
            'Y' : b'>02,0,home,<CR>\n',
            'Z' : b'>03,0,home,<CR>\n'
            },
        'mabs' : {
            'X' : b'>01,0,mabs,x,v,<CR>\n',
            'Y' : b'>02,0,mabs,y,v,<CR>\n',
            'Z' : b'>03,0,mabs,z,v,<CR>\n'
            }
        },
    'chassis' : {
        'pump_on' : b'',
        'pump_off' : b''
        },
    'coil' : {
        'set' : b'',
        'off' : b''
        },
    'pipettor' : {
        'set_asp_vol' : b'',
        'set_new_asp_resvol' : b'',
        'set_disp_vol' : b'',
        'set_new_disp_resvol' : b'',
        'set_action_mode' : b'',
        'trigger' : b'',
        'get_action_status' : b'',
        'get_action_mode' : b''
        }
    }