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
    #info.set_attribute("time::atime", 1522440880, None)
    t = info.get_attribute_type("time::access")
    atime = info.get_attribute_uint64("time::access")
    import time
    print("Now:" + str(time.time()))
    print("access: " + str(atime))
    info.set_attribute_uint64("time::access", 1502236800)
    input_file.set_attributes_from_info(info, Gio.FileQueryInfoFlags.NONE, None)
    GObject.idle_add(Gtk.main_quit)
    Gtk.main()
    #print(info.get_size())
    exit(0)
    uri = input_file.get_uri()
    #uri = "file://%s" % arg
    print(uri)
    rm = Gtk.RecentManager()
    rm = rm.get_default()
    #rm.remove_item(uri)
    # update atime first?
    rm.add_item(uri)
    #print(item.get_added())
    GObject.idle_add(Gtk.main_quit)
    Gtk.main()
except IndexError:
    exit(0)
