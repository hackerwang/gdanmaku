#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import json
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import Gtk
from danmaku_ui import Danmaku


class DBusObject(dbus.service.Object):

    @dbus.service.method("moe.tuna.danmaku.Service", in_signature=r's', out_signature='s')
    def new_danmaku(self, jargs):
        kwargs = json.loads(jargs)
        Danmaku(**kwargs)
        return "Done!"

    @dbus.service.method("moe.tuna.danmaku.Service", in_signature='', out_signature='s')
    def exit(self):
        Gtk.main_quit()
        return "Bye!"


def danmaku_service():
    DBusGMainLoop(set_as_default=True)
    session_bus = dbus.SessionBus()
    name = dbus.service.BusName("moe.tuna.danmaku", session_bus)
    _object = DBusObject(session_bus, "/Danmaku")
    Gtk.main()

# vim: ts=4 sw=4 sts=4 expandtab