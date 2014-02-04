# Written by Mehdy Dara (mdara@eleven-labs.com)

import sublime, sublime_plugin, webbrowser

class FindDocSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit, url):
        text = ""

        for region in self.view.sel():

            if region.empty():
                word = self.view.word(region)
                text += self.view.substr(word)
            else:
                text += self.view.substr(region)

        try:
            url = url % text
        except TypeError:
            url = url

        if sublime.active_window():
            sublime.active_window().run_command("prompt_find_doc", {"url": url} )

class PromptFindDocCommand(sublime_plugin.WindowCommand):
    def run(self, url):
        self.window.show_input_panel("Find doc on : ", url, self.on_done, None, None)

    def on_done(self, url):
        webbrowser.open_new_tab(url)
