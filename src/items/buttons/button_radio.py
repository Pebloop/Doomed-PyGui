from typing import Any, Union, Callable, List, Tuple

from src.items.buttons.button import Button
from src.items.items import Item
import dearpygui.dearpygui as dpg


class ButtonRadio(Button):
    def __init__(self,
                 items: Union[List[str], Tuple[str, ...]] = (),
                 *,
                 label: str = None,
                 user_data: Any = None,
                 use_internal_label: bool = True,
                 tag: Union[int, str] = 0,
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
                 default_value: str = '',
                 horizontal: bool = False,
                 **kwargs
                 ):
        self.identifier = dpg.add_radio_button(
            items=items,
            source=source,
            use_internal_label=use_internal_label,
            label=label,
            drag_callback=drag_callback,
            tag=tag,
            user_data=user_data,
            callback=callback,
            track_offset=track_offset,
            enabled=enabled,
            filter_key=filter_key,
            payload_type=payload_type,
            indent=indent,
            tracked=tracked,
            parent=parent,
            before=before,
            drop_callback=drop_callback,
            default_value=default_value,
            pos=pos,
            show=show,
            horizontal=horizontal,
            **kwargs
        )
