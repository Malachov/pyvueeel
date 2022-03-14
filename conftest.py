"""Runs before every pytest test. Used automatically (at least at VS Code)."""
from __future__ import annotations
import os
from pathlib import Path
import sys


# Find paths and add to sys.path to be able to use local version and not installed mypythontools version
root = Path(__file__).parent

if root not in sys.path:
    sys.path.insert(0, root.as_posix())

import mypythontools_cicd as cicd
import mypythontools

cicd.tests.setup_tests(matplotlib_test_backend=True)
