from src.items.window import Window
import dearpygui.dearpygui as dpg


def save_callback():
    print('saved')


class WindowPrimary(Window):
    def on_loop(self):
        super().on_loop()

    def __init__(self):
        super().__init__(id="Primary Window",
                         label="Example Window",
                         )

        tired_tempo = None

        width, height, channels, data = dpg.load_image('res/tired_tempo.png')  # 0: width, 1: height, 2: channels, 3: data
        with dpg.texture_registry():
            tired_tempo = dpg.add_static_texture(width, height, data, id="image_id")

        self.add_menu_bar()
        group = self.add_group(label="Group")
        group.add_checkbox(label="Checkbox")
        self.add_text(default_value="Hello world", label='Text')
        self.add_separator(label="Separator")

        #self.add_clipper(parent=self.identifier, label="Clipper")
        # dpg.add_menu(parent=self.identifier, label="Menu")

        cw = self.add_child_window(label="Child Window", id="Child Window")

        #cw.add_color_picker(width=100, label="Color Picker")

        group.add_slider_3d(scale=0.1, label="Slider 3D")
        dp = cw.add_date_picker(label="Date Picker")
        cw.add_image(tired_tempo, width=100, height=100)
        tt = dp.add_tooltip()
        # dpg.add_table(parent=cw.identifier, label="Table")

        cw.add_separator(label="Separator")

        cw.add_button_radio(['test', 'pasta'], label='Radio Button')
        cw.add_button_colormap([], label='Colormap Button')
        cw.add_button_color(label="Color Button")
        cw.add_button_image(texture_tag=tired_tempo,
                            label="Image button",
                            height=100,
                            width=100)
        cw.add_button(label="Button", callback=save_callback)

        cw.add_separator(label="Separator")

        cw.add_input_text(label="Input Text")
        cw.add_input_int(label="Input Int")
        cw.add_input_float(label="Input Float")
        cw.add_input_double(label='Input Double')
        cw.add_input_int_x(label="Input Int X")
        cw.add_input_double_x(label="Input Double X")
        cw.add_input_float_x(label="Input Float X")

        cw.add_separator(label="Separator")

        cw.add_slider_float(label="Slider Float")
        cw.add_slider_int(label="Slider Int")
        cw.add_slider_double(label='Slider Double')
        cw.add_slider_int_x(label='Slider Int X')
        cw.add_slider_float_x(label='Slider Float X')
        cw.add_slider_double_x(label='Slider Double X')
        cw.add_slider_colormap(label='Slider Colormap')

        cw.add_separator(label="Separator")

        plot = dpg.add_plot(parent=cw.identifier, label="Plot")

        dpg.add_plot_axis(dpg.mvXAxis, label="x", parent=plot)
        y_axis = dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis", parent=plot)
        dpg.add_line_series((1, 2, 3), (100, 451, 464), parent=y_axis)
