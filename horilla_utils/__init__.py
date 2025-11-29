import importlib
import sys

target = 'genie_utils'
mod = importlib.import_module(target)
sys.modules.setdefault('horilla_utils', mod)

for sub in [
    'methods', 'middlewares', 'management', 'management.commands.start_horilla_app',
]:
    try:
        sys.modules[f'horilla_utils.{sub}'] = importlib.import_module(f'{target}.{sub}')
    except Exception:
        pass

