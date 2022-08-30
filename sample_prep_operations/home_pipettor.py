'''
DESCRIPTION:
This module homes the pipettor using the gantry for sample prep operations.

AUTHOR:
G.LC

AFFILIATION:
Bio-Rad, CDG, Advanced-Tech Team

CREATED ON:
8/30/2022
'''

from commands import commands

import time

def HomePipettor(controller):
    # Home reader gantry Z.
    controller.write(commands['UpperGantry']['Pipettor-Z']['home'])
    # Wait for move to complete.
    wait(controller)
    # Home reader gantry X.
    controller.write(commands['UpperGantry']['Pipettor-X']['home'])
    # Home reader gantry Y.
    controller.write(commands['UpperGantry']['Pipettor-Y']['home'])
    # Wait for move to complete.
    wait(controller)

def wait(controller, timeout=10, verbose=True):
    time_start = time.time()
    while time.time() - time_start < timeout:
        response = controller.read().decode()
        if response == '\r':
            return
    if verbose:
        print("WARNING (home_pipettor, wait): timeout ({0} sec) reached with no response!".format(timeout))