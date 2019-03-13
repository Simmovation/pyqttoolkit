class ThemeManager:
    default_theme = {
        'button_foreground': (0, 0, 0),
        'button_background_hover': (255, 255, 255),
        'highlight': (255, 96, 154),
        'highlight_hover': (255, 163, 196),
        'highlight_pressed': (255, 147, 186),
        'highlight': (255, 96, 154),
        'module_background': (200, 200, 200),
        'module_text': (0, 0, 0)
    }

    def __init__(self, application_configuration):
        self._config = application_configuration
    
    def get_color(self, key):
        selected_theme = self._get_selected_theme()
        color = self._config.get_value(f'application.themes.{selected_theme}.{key}') if selected_theme else None
        return tuple(color) if color else self.default_theme.get(key)
    
    def _get_selected_theme(self):
        return self._config.get_value(f'application.themes.selected_theme') or None

    @staticmethod
    def get(widget):
        while widget is not None and not hasattr(widget, 'themeManager'):
            widget = widget.parent()
        if widget is not None and hasattr(widget, 'themeManager'):
            return widget.themeManager
        return None
