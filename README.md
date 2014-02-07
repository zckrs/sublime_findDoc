# FindDoc - Sublime Text plugin
This is a [Sublime Text](http://www.sublimetext.com) plugins that allows you to search the documentation on your favorites urls.

### How to install
The easiest way to install this is with [Package Control](http://wbond.net/sublime\_packages/package\_control).

Or you can download the zip archive and unzip in your packages directory (by Preferences->Browse Packages...).

### How to configure
The default shortcut to call the plugin is : `ctrl + alt + d`.

The default used url is : `http://devdocs.io/#q=%s`.

But you can set multiple shortcuts and urls by your key bindings.

Examples :
```json
{ "keys": ["ctrl+alt+d"], "command": "find_doc_selection", "args" : {"url" : "http://devdocs.io/#q=%s"} }
{ "keys": ["ctrl+alt+g"], "command": "find_doc_selection", "args" : {"url" : "http://google.fr/search?q=%s"} }
{ "keys": ["ctrl+alt+k"], "command": "find_doc_selection", "args" : {"url" : "http://php.net/%s"} }
```
Others examples : you can open cheat sheet or what do you want
```json
{ "keys": ["ctrl+alt+c"], "command": "find_doc_selection", "args" : {"url" : "http://www.cheatography.com/fredv/cheat-sheets/gmail-cheat-sheet/"} }
{ "keys": ["ctrl+alt+n"], "command": "find_doc_selection", "args" : {"url" : "http://www.nyan.cat/"} }
```
### How to use
Highlight the function(s)/method(s)/text(s) to search and use the shortcut to open a new tab(s).

If you don't highlight text, the plugin selects the current word at cursor by camelCase.

### How to contribute
If you have some problems or improvements, [contact me](https://github.com/zckrs/sublime_findDoc/issues) via GitHub.
