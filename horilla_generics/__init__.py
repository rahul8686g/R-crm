import importlib
import sys

target = 'genie_generics'
mod = importlib.import_module(target)
sys.modules.setdefault('horilla_generics', mod)

for sub in ['urls', 'signals', 'views', 'mixins', 'global_search', 'horilla_support_views', 'forms', 'filters', 'templatetags.horilla_tags']:
    try:
        sys.modules[f'horilla_generics.{sub}'] = importlib.import_module(f'{target}.{sub}')
    except Exception:
        pass

