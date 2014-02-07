# Written by Mehdy Dara (mdara@eleven-labs.com)

import sublime, sublime_plugin, webbrowser, urllib

class FindDocSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit, url):
        arrayUrl = []

        # Get the text for each selections and cursors.
        for region in self.view.sel():
            if region.empty():
                word = self.view.word(region)
                text = self.view.substr(word)
            else:
                text = self.view.substr(region)

            # Encode the text for url
            try:
                text = urllib.parse.quote(text)
            except AttributeError:
                print("FindDoc AttributeError : 'urllibl' object has no attribute 'parse'")
                text = text.replace(' ', '%20')

            # Concatenate url and text
            try:
                arrayUrl.append(url % text)
            except TypeError:
                arrayUrl.append(url % '')

        if sublime.active_window():
            # Open new tab for each highlighted text
            for aUrl in arrayUrl:
                webbrowser.open_new_tab(aUrl)
