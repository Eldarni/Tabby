import sublime
import sublime_plugin
import logging

##################################################

TABBY_SETTINGS_FILE = 'Tabby.sublime-settings'

##################################################


def loadTabGroups():
    settings = sublime.load_settings(TABBY_SETTINGS_FILE)
    return settings.get('groups')


def saveTabGroups(group_list):
    settings = sublime.load_settings(TABBY_SETTINGS_FILE)
    settings.set('groups', group_list)
    sublime.save_settings(TABBY_SETTINGS_FILE)


def openTabGroupQuickPanel(callback):
    group_names = []
    for group in loadTabGroups():
        group_names.append(group[0])

    sublime.active_window().show_quick_panel(group_names, callback)


def openInputQuickPanel(message, callback):
    sublime.active_window().show_input_panel(message, '', callback, None, None)


def loadTabGroup(index):
    if (index >= 0):
        return loadTabGroups()[index]


def addTabGroup(group_name, new_tab_group):
    current_tab_groups = loadTabGroups()
    new_tab_group.insert(0, group_name)
    current_tab_groups.append(new_tab_group)
    saveTabGroups(current_tab_groups)


def getFilesInGroup(index):
    if (index >= 0):
        return loadTabGroup(index)[1:-1]


def removeTabGroup(index):
    if (index >= 0):
        current_tab_groups = loadTabGroups()
        del current_tab_groups[index]
        saveTabGroups(current_tab_groups)

##################################################


class TabbySaveCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        openInputQuickPanel('Enter Group Name', self.save_group)

    def save_group(self, group_name):
        new_tab_group = []
        for view in sublime.active_window().views():
            new_tab_group.append(view.file_name())

        addTabGroup(group_name, new_tab_group)

##################################################


class TabbyLoadCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        openTabGroupQuickPanel(self.load_group)

    def load_group(self, index):
        if (index >= 0):
            for filename in getFilesInGroup(index):
                sublime.active_window().open_file(filename)

##################################################


class TabbyRenameCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        openTabGroupQuickPanel(self.rename_group_input)

    def rename_group_input(self, index):
        openInputQuickPanel('Please enter the new name', self.rename_group)

    def rename_group(self, new_name):
        logging.warning('Will rename to:' + new_name)

##################################################


class TabbyRemoveCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        openTabGroupQuickPanel(self.remove_group)

    def remove_group(self, index):
        removeTabGroup(index)

##################################################


class TabbySwitchCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        logging.warning('TabbySwitchCommand')

##################################################


class TabbyCloseTabAllCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        logging.warning('TabbyCloseAllCommand')

##################################################


class TabbyCloseTabOtherCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        logging.warning('TabbyCloseOtherCommand')

##################################################


class TabbyCloseTabCurrentCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        logging.warning('TabbyCloseOtherCommand')

##################################################
