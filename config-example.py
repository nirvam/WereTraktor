"""
Copy this file to 'config.py'. Modify 'config.py' to change app settings and basic game rules.
"""

import sys

settings = {
    'port': 8000,
    'debug': False,
    'database_path': sys.path[0]  # app folder
}

basic_rules = {
    'witch_can_self_heal': False,
    'sheriff_vote_count': 1.5
}
