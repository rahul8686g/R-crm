import importlib
import sys

target = 'genie_core'
mod = importlib.import_module(target)
sys.modules.setdefault('horilla_core', mod)

# Attach commonly used submodules as attributes for migration compatibility
try:
    import importlib as _il
    mod.models = _il.import_module(f'{target}.models')
except Exception:
    pass

for sub in [
    'api', 'api.urls', 'models', 'views', 'urls', 'signals', 'scheduler',
    'login_history', 'menu', 'middlewares', 'users', 'tasks', 'utils',
    'decorators', 'change_password', 'forgot_password', 'groups_and_permissions',
    'initialiaze_database', 'import_data', 'roles', 'branches', 'departments',
    'fiscal_year', 'export_data', 'multiple_currency', 'recycle_bin', 'customer_role',
    'partner_role', 'scoring_rule', 'team_role', 'users', 'user_holidays',
    'mixins', 'middlewares', 'forms', 'progress',
]:
    try:
        sys.modules[f'horilla_core.{sub}'] = importlib.import_module(f'{target}.{sub}')
    except Exception:
        pass
