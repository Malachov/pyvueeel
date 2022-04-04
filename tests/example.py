from pathlib import Path

from mypythontools_cicd.tests import setup_tests

setup_tests()

import mylogging

import pyvueeel
from pyvueeel import run_gui, expose, eel, to_vue_plotly


def print_traceback(caption="Error", message=""):
    """Print python error to user web based GUI.

    Note:
        Suppose exposed function create_alert from Vue.

    Args:
        message (str, optional): Heading of detailed traceback. Defaults to "Error".
    """
    mylogging.traceback(
        f"Caught error - server still running.\n\n{message}",
        caption,
    )


pyvueeel.expose_error_callback = print_traceback


@expose
def test_function(params, arg1="default", arg2="default"):
    pyvueeel.eel.create_alert(
        "It works",
        "I am js function called from Py",
        None,
    )
    return [1, 2, 3]


if __name__ == "__main__":
    run_gui(build_gui_path=Path(__file__).parent / "gui", devel=False)
