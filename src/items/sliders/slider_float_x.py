from typing import Any, Union, Callable, Tuple, List

from src.items.items import Item
import dearpygui.dearpygui as dpg

from src.items.sliders.slider import Slider


class SliderFloatX(Slider):
    def __init__(self,
                 *,
                 label: str = None,
                 user_data: Any = None,
                 use_internal_label: bool = True,
                 tag: Union[int, str] = 0,
                 width: int = 0,
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
                 default_value: Union[List[float], Tuple[float, ...]] = (0.0, 0.0, 0.0, 0.0),
                 size: int = 4,
                 no_input: bool = False,
                 clamped: bool = False,
                 min_value: float = 0.0,
                 max_value: float = 100.0,
                 format: str = '%.3f',
                 **kwargs
                 ):
        self.identifier = dpg.add_slider_floatx(
            indent=indent,
            parent=parent,
            label=label,
            before=before,
            tracked=tracked,
            drop_callback=drop_callback,
            pos=pos,
            callback=callback,
            payload_type=payload_type,
            show=show,
            user_data=user_data,
            filter_key=filter_key,
            use_internal_label=use_internal_label,
            min_value=min_value,
            max_value=max_value,
            track_offset=track_offset,
            source=source,
            default_value=default_value,
            drag_callback=drag_callback,
            no_input=no_input,
            enabled=enabled,
            format=format,
            clamped=clamped,
            width=width,
            tag=tag,
            size=size,
            **kwargs
        )
