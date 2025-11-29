import importlib
import sys

target = 'genie_keys'
mod = importlib.import_module(target)
sys.modules.setdefault('horilla_keys', mod)

for sub in ['api', 'api.urls', 'views', 'urls', 'signals', 'menu', 'models', 'forms', 'filters', 'admin']:
    try:
        sys.modules[f'horilla_keys.{sub}'] = importlib.import_module(f'{target}.{sub}')
    except Exception:
        pass

