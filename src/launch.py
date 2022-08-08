import dearpygui.dearpygui as dpg
from src.utils import window
from src.items.window_primary import WindowPrimary


def update_size():
    pass


def run():
    dpg.create_context()
    dpg.create_viewport(title="test")
    dpg.setup_dearpygui()

    main_window = WindowPrimary()

    dpg.set_primary_window(main_window.identifier, True)
    dpg.set_viewport_resize_callback(update_size)

    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
