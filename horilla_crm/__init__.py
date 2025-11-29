import importlib
import sys

target = 'genie_crm'
mod = importlib.import_module(target)
sys.modules.setdefault('horilla_crm', mod)

for sub in [
    'leads', 'leads.api', 'leads.api.urls', 'leads.urls', 'leads.menu', 'leads.signals', 'leads.models', 'leads.forms', 'leads.filters', 'leads.admin', 'leads.tasks',
    'reports', 'reports.api', 'reports.api.urls', 'reports.urls', 'reports.menu', 'reports.signals', 'reports.models', 'reports.forms', 'reports.filters', 'reports.admin',
    'activity', 'activity.api', 'activity.api.urls', 'activity.urls', 'activity.menu', 'activity.signals', 'activity.models', 'activity.forms', 'activity.filters', 'activity.admin',
    'timeline', 'timeline.api', 'timeline.api.urls', 'timeline.urls', 'timeline.menu', 'timeline.signals', 'timeline.models',
    'opportunities', 'opportunities.api', 'opportunities.api.urls', 'opportunities.urls', 'opportunities.menu', 'opportunities.signals', 'opportunities.models', 'opportunities.forms', 'opportunities.filters', 'opportunities.admin',
    'accounts', 'accounts.api', 'accounts.api.urls', 'accounts.urls', 'accounts.menu', 'accounts.signals', 'accounts.models', 'accounts.forms', 'accounts.filters', 'accounts.admin',
    'campaigns', 'campaigns.api', 'campaigns.api.urls', 'campaigns.urls', 'campaigns.menu', 'campaigns.signals', 'campaigns.models', 'campaigns.forms', 'campaigns.filters', 'campaigns.admin',
    'forecast', 'forecast.api', 'forecast.api.urls', 'forecast.urls', 'forecast.menu', 'forecast.signals', 'forecast.models',
    'contacts', 'contacts.api', 'contacts.api.urls', 'contacts.urls', 'contacts.menu', 'contacts.signals', 'contacts.models', 'contacts.forms', 'contacts.filters', 'contacts.admin',
]:
    try:
        sys.modules[f'horilla_crm.{sub}'] = importlib.import_module(f'{target}.{sub}')
    except Exception:
        pass
