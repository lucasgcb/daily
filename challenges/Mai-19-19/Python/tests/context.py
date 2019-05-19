import sys
import os
# append module root directory to sys.path
# https://docs.python-guide.org/writing/structure/#test-suite
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)
import solution #pylint: disable=import-error