#!/usr/bin/env python
import os
import sys
import threading
import time

def background_task():
    # Příklad úlohy běžící na pozadí - každých 10 sekund vypíše zprávu
    while True:
        print("Background task running in thread...")
        time.sleep(10)

def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jacketHM.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Spuštění background úlohy ve vlákně jako daemon
    t = threading.Thread(target=background_task, daemon=True)
    t.start()

    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()

