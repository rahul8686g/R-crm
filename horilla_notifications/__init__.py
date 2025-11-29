import importlib
import sys

target = 'genie_notifications'
mod = importlib.import_module(target)
sys.modules.setdefault('horilla_notifications', mod)

for sub in ['api', 'api.urls', 'views', 'urls', 'signals', 'models', 'api.tests', 'api.serializers', 'api.filters']:
    try:
        sys.modules[f'horilla_notifications.{sub}'] = importlib.import_module(f'{target}.{sub}')
    except Exception:
        pass

