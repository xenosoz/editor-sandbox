#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urwid

Screen = urwid.raw_display.Screen
screen = Screen()

title = urwid.Text('Exit        C-x C-c')
title = urwid.AttrMap(title, 'title')

txt = urwid.Text('{key}')
body = urwid.Filler(urwid.Columns([title, txt]), 'top')

ctrl_x = False


def handle_exit(key):
    global ctrl_x

    key = key.replace('ctrl ', 'C-')
    txt.set_text(repr(key))

    if 'C-x' == key:
        ctrl_x = True

    if ctrl_x and ('C-c' == key):
        raise urwid.ExitMainLoop

    if 'C-x' not in key:
        ctrl_x = False


palette = [
    ('title', 'black', 'light gray'),
]


#loop = urwid.MainLoop(body, palette, screen, input_filter=input_filter)  # (keys, raw)
loop = urwid.MainLoop(body, palette, screen, unhandled_input=handle_exit)  # (key)


try:
    old = screen.tty_signal_keys('undefined', 'undefined', 'undefined', 'undefined', 'undefined')
    loop.run()
finally:
    screen.tty_signal_keys(*old)

