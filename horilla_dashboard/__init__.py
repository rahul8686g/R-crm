import importlib
import sys

target = 'genie_dashboard'
mod = importlib.import_module(target)
sys.modules.setdefault('horilla_dashboard', mod)

for sub in ['views', 'urls', 'signals', 'menu', 'models', 'methods', 'api', 'api.urls', 'api.serializers', 'filters', 'forms', 'admin']:
    try:
        sys.modules[f'horilla_dashboard.{sub}'] = importlib.import_module(f'{target}.{sub}')
    except Exception:
        pass
