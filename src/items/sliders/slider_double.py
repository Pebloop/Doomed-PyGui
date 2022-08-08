from typing import Any, Union, Callable, Tuple, List

from src.items.items import Item
import dearpygui.dearpygui as dpg

from src.items.sliders.slider import Slider


class SliderDouble(Slider):
    def __init__(self,
                 *,
                 label: str = None,
                 user_data: Any = None,
                 use_internal_label: bool = True,
                 tag: Union[int, str] = 0,
                 width: int = 0,
                 height: int = 0,
                 indent: int = -1,
                 parent: Union[int, str] = 0,
                 before: Union[int, str] = 0,
                 source: Union[int, str] = 0,
                 payload_type: str = '$$DPG_PAYLOAD',
                 callback: Callable = None,
                 drag_callback: Callable = None,
                 drop_callback: Callable = None,
                 show: bool = True,
                 enabled: bool = True,
                 pos: Union[List[int], Tuple[int, ...]] = [],
                 filter_key: str = '',
                 tracked: bool = False,
                 track_offset: float = 0.5,
                 default_value: float = 0.0,
                 vertical: bool = False,
                 no_input: bool = False,
                 clamped: bool = False,
                 min_value: float = 0.0,
                 max_value: float = 100.0,
                 format: str = '%.3f',
                 **kwargs
                 ):
        self.identifier = dpg.add_slider_double(
            height=height,
            tracked=tracked,
            parent=parent,
            label=label,
            before=before,
            user_data=user_data,
            indent=indent,
            filter_key=filter_key,
            callback=callback,
            show=show,
            payload_type=payload_type,
            track_offset=track_offset,
            drop_callback=drop_callback,
            default_value=default_value,
            drag_callback=drag_callback,
            use_internal_label=use_internal_label,
            source=source,
            min_value=min_value,
            max_value=max_value,
            enabled=enabled,
            width=width,
            pos=pos,
            tag=tag,
            format=format,
            no_input=no_input,
            clamped=clamped,
            vertical=vertical,
            **kwargs
        )
