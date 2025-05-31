#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from ultralytics import YOLO
from G import G

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pyweb.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
if __name__ == '__main__':
    G.model_8n = YOLO('yolov8n.pt')
    G.model_8x = YOLO('yolov8x.pt')
    main()
