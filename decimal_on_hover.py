import sublime
import sublime_plugin
import re

patterns = [
    (re.compile(r'0b[01]+'),         2),
    (re.compile(r'0o[0-7]+'),        8),
    (re.compile(r'0x[0-9a-fA-F]+'), 16)
]

class ShowDecimalOnHoverCommand(sublime_plugin.ViewEventListener):

    def on_hover(self, point, hover_zone):

        if hover_zone == sublime.HOVER_TEXT:
            word = self.view.substr(self.view.word(point))

            for p, base in patterns:
                if (p.match(word)):
                    self.show_tooltip(point, word, str(int(word, base)))

    def show_tooltip(self, point, literal, decimal_value):
        self.view.show_popup(f"{literal}: {decimal_value}", sublime.HIDE_ON_MOUSE_MOVE_AWAY, point)
