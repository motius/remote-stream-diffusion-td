# before you can use this you have to build the project and globally install it
# rye build
# pip install dist/touchdesigner_plugin-0.1.0-py3-none-any.whl

import sys

# using this on mac so package was installed to homebrew's python
custom_module_path = "/opt/homebrew/lib/python3.11/site-packages"
if custom_module_path not in sys.path:
    sys.path = [custom_module_path] + sys.path


from touchdesigner_plugin.prompt_client import PromptClient  # noqa: E402

prompt_client = PromptClient()
prompt_client.run("text dat prompt")
