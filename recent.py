#!/usr/bin/python3

import sys
import time

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, Gio

try:
    arg = sys.argv[1]
    input_file = Gio.File.new_for_path(arg)
    if not input_file.query_exists():
        print("No such file or directory: %s" % arg)
        exit(1)
    info = input_file.query_info('time::access', Gio.FileQueryInfoFlags.NONE, None)
    info.set_attribute_uint64("time::access", time.time())
    input_file.set_attributes_from_info(info, Gio.FileQueryInfoFlags.NONE, None)
    uri = input_file.get_uri()
    rm = Gtk.RecentManager()
    rm = rm.get_default()
    rm.add_item(uri)
    GObject.idle_add(Gtk.main_quit)
    Gtk.main()
except IndexError:
    exit(0)
