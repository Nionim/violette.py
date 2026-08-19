import os, importlib
from typing import Dict, Any

LANG_PACKAGE = "lang"

def load_languages() -> Dict[str, Any]:
    languages = {}
    package_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), LANG_PACKAGE)
    for filename in os.listdir(package_dir):
        if filename.endswith('.py') and not filename.startswith('__'):
            module_name = filename[:-3]
            try:
                module = importlib.import_module(f".{module_name}", package=LANG_PACKAGE)
                if hasattr(module, "LABEL"):
                    languages[module.LABEL] = module
            except Exception:
                continue
    return languages

LANGUAGES = load_languages()
LANG_CHOICES = list(LANGUAGES.keys())