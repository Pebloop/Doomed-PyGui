from typing import Any, Union, Callable, Tuple, List

from src.items.items import Item
import dearpygui.dearpygui as dpg

from src.items.sliders.slider import Slider


class SliderDoubleX(Slider):
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
                 default_value: Any = (0.0, 0.0, 0.0, 0.0),
                 size: int = 4,
                 no_input: bool = False,
                 clamped: bool = False,
                 min_value: float = 0.0,
                 max_value: float = 100.0,
                 format: str = '%.3f',
                 **kwargs
                 ):
        self.identifier = dpg.add_slider_doublex(
            clamped=clamped,
            no_input=no_input,
            format=format,
            enabled=enabled,
            max_value=max_value,
            min_value=min_value,
            width=width,
            source=source,
            tag=tag,
            track_offset=track_offset,
            drag_callback=drag_callback,
            default_value=default_value,
            use_internal_label=use_internal_label,
            user_data=user_data,
            filter_key=filter_key,
            callback=callback,
            payload_type=payload_type,
            drop_callback=drop_callback,
            tracked=tracked,
            before=before,
            parent=parent,
            indent=indent,
            label=label,
            pos=pos,
            show=show,
            size=size,
            **kwargs
        )
