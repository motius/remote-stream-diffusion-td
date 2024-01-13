import platform
import sys

if "macOS" in platform.platform():
    # using this on mac so package was installed to homebrew's python
    custom_module_path = "../.venv/lib"
    if custom_module_path not in sys.path:
        sys.path = [custom_module_path] + sys.path
else:
    # ToDo windows python site-packages
    print("Implementing this in Windows is still a ToDo, sry :-)")

# import touchdesigner_plugin as td_plugin  # flake8: noqa
print("Custom fileserver touchdesigner plugin was successfully imported")
