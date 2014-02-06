# Written by Mehdy Dara (mdara@eleven-labs.com)

import sublime, sublime_plugin, webbrowser, urllib

class FindDocSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit, url):
        text = ""

        # Get the text for each selections and cursors.
        for region in self.view.sel():
            if region.empty():
                word = self.view.word(region)
                text += self.view.substr(word)
            else:
                text += self.view.substr(region)

        # Encode the text for url
        text = urllib.parse.quote(text)

        # Concate url and text
        try:
            url = url % text
        except TypeError:
            url = url

        # Open new tab on url
        if sublime.active_window():
            # '<b>bold</b>ä'
            sublime.message_dialog(url)
            sublime.active_window().run_command("prompt_find_doc", {"url": url} )

class PromptFindDocCommand(sublime_plugin.WindowCommand):
    def run(self, url):
        self.window.show_input_panel("Find doc on : ", url, self.on_done, None, None)

    def on_done(self, url):
        webbrowser.open_new_tab(url)
