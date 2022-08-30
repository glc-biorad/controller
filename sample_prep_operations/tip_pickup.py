'''
DESCRIPTION:
This module contains the TipPickup function for picking up tips at a given target location.

NOTES:
target (in): a Coordinate object

AUTHOR:
G.LC

AFFILIATION:
Bio-Rad, CDG, Advanced-Tech Team

CREATED ON:
8/30/2022
'''

from coordinate import Coordinate, coordinates
from commands import commands

import sys
import time

SAFE_Z = '-1000' #??

SPEED_X = '100000' #???
SPEED_Y = '100000' #???
SPEED_Z = '100000' #???

N_TIP_TRAYS = 4
N_TIP_ROWS = 12

def TipPickup_depricated(controller, target):
    coordinate = Coordinate(target)
    print(f"Coordinate: {coordinate.x}, {coordinate.y}, {coordinate.z}")

def TipPickup(controller, tray_number, tray_row_number, ):
    # Make sure desired pickup location is valid.
    if _pickupNotInBounds(tray_number, tray_row_number):
        sys.exit()

    # Get the coordinate for the pickup location.
    coordinate = Coordinate(coordinates['deck_plate']['tip_trays'][tray_number][tray_row_number])
    x, y, z = [str(coordinate.x), str(coordinate.y), str(coordinate.z)]

    # Move the pipettor gantry Z to clear the prep deck.
    command = commands['UpperGantry']['Pipettor-Z']['mabs'].replace('target', SAFE_Z, 1).replace('speed', SPEED_Z, 1)
    controller.write(command)

    # Wait for move to complete.
    wait(controller)

    # Move the pipettor gantry X and Y.
    command = commands['UpperGantry']['Pipettor-X']['mabs'].replace('target', x, 1).replace('speed', SPEED_X, 1)
    controller.write(command)
    command = commands['UpperGantry']['Pipettor-Y']['mabs'].replace('target', y, 1).replace('speed', SPEED_Y, 1)
    controller.write(command)

    # Wait for moves to complete.
    wait(controller)

    # Move the pipettor gantry Z to mount tips on the pipettor mandrels.
    command = commands['UpperGantry']['Pipettor-Z']['mabs'].replace('target', z, 1).replace('speed', SPEED_Z, 1)
    controller.write(command)


def _pickupNotInBounds(tray_number, tray_row_number, verbose=True):
    if not (tray_number >= 0 and tray_number < N_TIP_TRAYS):
        if verbose:
            print(f"ERROR (tip_pickup, _pickupNotInBounds): tray number ({tray_number}) is out of bounds!")
        return True
    if not (tray_row_number >= 0 and tray_row_number < N_TIP_ROWS):
        if verbose:
            print(f"ERROR (tip_pickup, _pickupNotInBounds): tray row number ({tray_row_number}) is out of bounds!")
        return True
    return False

def wait(controller, timeout=10, verbose=True):
    time_start = time.time()
    while time.time() - time_start < timeout:
        response = controller.read().decode()
        if response == '\r':
            return
    if verbose:
        print("WARNING (tip_pickup, wait): timeout ({0} sec) reached with no response!".format(timeout))