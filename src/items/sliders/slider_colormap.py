from typing import Any, Union, Callable, Tuple, List

from src.items.items import Item
import dearpygui.dearpygui as dpg

from src.items.sliders.slider import Slider


class SliderColormap(Slider):
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
                 payload_type: str = '$$DPG_PAYLOAD',
                 callback: Callable = None,
                 drop_callback: Callable = None,
                 show: bool = True,
                 pos: Union[List[int], Tuple[int, ...]] = [],
                 filter_key: str = '',
                 tracked: bool = False,
                 track_offset: float = 0.5,
                 default_value: float = 0.0,
                 **kwargs
                 ):
        self.identifier = dpg.add_colormap_slider(
            use_internal_label=use_internal_label,
            width=width,
            tag=tag,
            default_value=default_value,
            track_offset=track_offset,
            pos=pos,
            payload_type=payload_type,
            drop_callback=drop_callback,
            callback=callback,
            filter_key=filter_key,
            user_data=user_data,
            indent=indent,
            before=before,
            tracked=tracked,
            parent=parent,
            label=label,
            show=show,
            height=height,
            **kwargs
        )
