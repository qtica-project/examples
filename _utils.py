#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
from Qtica.enums import Colors


def get_random_color():
    return getattr(Colors, random.choice(tuple(Colors.__members__.keys()))).value
