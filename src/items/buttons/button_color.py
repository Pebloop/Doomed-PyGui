from typing import Any, Union, Callable, List, Tuple

from src.items.buttons.button import Button
from src.items.items import Item
import dearpygui.dearpygui as dpg


class ButtonColor(Button):
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
                 no_alpha: bool = False,
                 no_border: bool = False,
                 no_drag_drop: bool = False,
                 **kwargs
                 ):
        self.identifier = dpg.add_color_button(
            default_value=default_value,
            width=width,
            use_internal_label=use_internal_label,
            tag=tag,
            drag_callback=drag_callback,
            track_offset=track_offset,
            enabled=enabled,
            label=label,
            indent=indent,
            pos=pos,
            user_data=user_data,
            show=show,
            filter_key=filter_key,
            callback=callback,
            payload_type=payload_type,
            parent=parent,
            tracked=tracked,
            before=before,
            height=height,
            drop_callback=drop_callback,
            no_alpha=no_alpha,
            no_border=no_border,
            no_drag_drop=no_drag_drop,
            **kwargs
        )
