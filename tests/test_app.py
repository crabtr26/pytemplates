import os
import sys
from pathlib import Path

project_path = os.path.join(str(Path(__file__).parent.parent))
sys.path.append(project_path)
from src.app import main


def test_app():
    pass
