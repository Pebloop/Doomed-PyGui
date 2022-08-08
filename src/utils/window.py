import dearpygui.dearpygui as dpg


def width():
    return dpg.get_viewport_client_width()


def height():
    return dpg.get_viewport_client_height()
