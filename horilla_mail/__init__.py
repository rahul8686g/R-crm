import importlib
import sys

target = 'genie_mail'
mod = importlib.import_module(target)
sys.modules.setdefault('horilla_mail', mod)

for sub in [
    'api', 'api.urls', 'views', 'urls', 'signals', 'scheduler', 'menu',
    'methods', 'tasks', 'services', 'incoming_mail', 'outgoing_mail',
    'horilla_outlook', 'horilla_mail_template', 'horilla_backends', 'encryption_utils',
    'models', 'filters', 'forms', 'admin', 'celery_schedules', 'fields',
]:
    try:
        sys.modules[f'horilla_mail.{sub}'] = importlib.import_module(f'{target}.{sub}')
    except Exception:
        pass
