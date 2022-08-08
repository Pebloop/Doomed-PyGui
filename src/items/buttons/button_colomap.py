from typing import Any, Union, Callable, List, Tuple

from src.items.buttons.button import Button
from src.items.items import Item
import dearpygui.dearpygui as dpg


class ButtonColormap(Button):
    def __init__(self,
                 default_value: Union[List[int], Tuple[int, ...]] = (0, 0, 0, 255),
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
                 drag_callback: Callable = None,
                 drop_callback: Callable = None,
                 show: bool = True,
                 enabled: bool = True,
                 pos: Union[List[int], Tuple[int, ...]] = [],
                 filter_key: str = '',
                 tracked: bool = False,
                 track_offset: float = 0.5,
                 **kwargs
                 ):
        self.identifier = dpg.add_colormap_button(
            default_value=default_value,
            height=height,
            tracked=tracked,
            before=before,
            drop_callback=drop_callback,
            user_data=user_data,
            filter_key=filter_key,
            callback=callback,
            payload_type=payload_type,
            parent=parent,
            indent=indent,
            use_internal_label=use_internal_label,
            track_offset=track_offset,
            enabled=enabled,
            drag_callback=drag_callback,
            label=label,
            pos=pos,
            width=width,
            show=show,
            tag=tag,
            **kwargs
        )
