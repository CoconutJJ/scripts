from enum import IntEnum

class CSField(IntEnum):
    MACHINE_LEARNING = 0
    COMPUTER_VISION = 1
    NATURAL_LANGUAGE_PROCESSING = 2
    SYSTEMS = 3
    PROGRAMMING_LANGUAGES = 4
    COMPILERS = 5
    OPERATING_SYSTEMS = 6
    SECURITY = 7
    DATABASES = 8
    NETWORKING = 9
    THEORY = 10
    GRAPHICS = 11
    HUMAN_COMPUTER_INTERACTION = 12


FIELD_SIMILARITY_MATRIX = [
    # ML    CV    NLP   Sys   PL    Comp  OS    Sec   DB    Net   Th    Gfx  HCI
    [1.0,   0.8,  0.8,  0.4,  0.4,  0.4,  0.4,  0.4,  0.4,  0.4,  0.5,  0.4, 0.4],  # MACHINE_LEARNING
    [-1.0,  1.0,  0.6,  0.4,  0.4,  0.4,  0.4,  0.4,  0.4,  0.4,  0.4,  0.5, 0.5],  # COMPUTER_VISION
    [-1.0, -1.0,  1.0,  0.4,  0.4,  0.4,  0.4,  0.4,  0.4,  0.4,  0.5,  0.4, 0.4], # NATURAL_LANGUAGE_PROCESSING
    [-1.0, -1.0, -1.0,  1.0,  0.5,  0.5,  0.8,  0.6,  0.6,  0.7,  0.4,  0.4, 0.4], # SYSTEMS
    [-1.0, -1.0, -1.0, -1.0,  1.0,  0.9,  0.5,  0.4,  0.4,  0.4,  0.6,  0.4, 0.4], # PROGRAMMING_LANGUAGES
    [-1.0, -1.0, -1.0, -1.0, -1.0,  1.0,  0.6,  0.4,  0.4,  0.4,  0.6,  0.4, 0.4], # COMPILERS
    [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0,  1.0,  0.6,  0.5,  0.6,  0.4,  0.4, 0.4], # OPERATING_SYSTEMS
    [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0,  1.0,  0.5,  0.7,  0.4,  0.4, 0.4], # SECURITY
    [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0,  1.0,  0.6,  0.5,  0.4, 0.4], # DATABASES
    [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0,  1.0,  0.4,  0.4, 0.4], # NETWORKING
    [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0,  1.0,  0.4, 0.4], # THEORY
    [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0,  1.0, 0.6], # GRAPHICS
    [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, 1.0]  # HCI
]