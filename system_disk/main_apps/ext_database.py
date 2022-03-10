"""
This extension script will identify the extension of 
the file and return the correct program to open it.
"""

from errors.system_error import *

all_ext = {".txt": "system_disk/applications/notepad/ntpd.py",
           ".py": "system_disk/applications/notepad/ntpd.py"}


def load_ext(ext) -> str:
    return all_ext[ext] if ext in all_ext else None
    