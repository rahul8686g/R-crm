import importlib
import sys

# Alias root package
sys.modules.setdefault('horilla', importlib.import_module('genie'))

def _alias(mod_map):
    for alias, target in mod_map.items():
        try:
            sys.modules[alias] = importlib.import_module(target)
        except Exception:
            pass

# Core module aliases
_alias({
    'horilla.settings': 'genie.settings',
    'horilla.settings.base': 'genie.settings.base',
    'horilla.settings.local_settings': 'genie.settings.local_settings',
    'horilla.settings.horilla_apps': 'genie.settings.horilla_apps',
    'horilla.urls': 'genie.urls',
    'horilla.exceptions': 'genie.exceptions',
    'horilla.menu': 'genie.menu',
    'horilla.menu.main_section_menu': 'genie.menu.main_section_menu',
    'horilla.menu.sub_section_menu': 'genie.menu.sub_section_menu',
    'horilla.menu.settings_menu': 'genie.menu.settings_menu',
    'horilla.menu.my_settings_menu': 'genie.menu.my_settings_menu',
    'horilla.menu.floating_menu': 'genie.menu.floating_menu',
    'horilla.registry': 'genie.registry',
    'horilla.registry.feature': 'genie.registry.feature',
    'horilla.registry.permission_registry': 'genie.registry.permission_registry',
    'horilla.registry.js_registry': 'genie.registry.js_registry',
    'horilla.utils': 'genie.utils',
    'horilla.utils.choices': 'genie.utils.choices',
})

