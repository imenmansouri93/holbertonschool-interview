#!/usr/bin/python3
"""
"""


def canUnlockAll(boxes):
    n = len(boxes)  # Number of boxes
    unlocked = [False] * n  # Keeps track of whether each box is unlocked
    unlocked[0] = True  # The first box is unlocked by default

    keys_to_check = [0]  # Start with the keys from the first box

    while keys_to_check:
        current_box = keys_to_check.pop()

        for key in boxes[current_box]:
            if 0 <= key < n and not unlocked[key]:
                unlocked[key] = True
                keys_to_check.append(key)

    return all(unlocked) 