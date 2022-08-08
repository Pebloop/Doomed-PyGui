from typing import Any, Union, Callable, List, Tuple

from src.items.buttons.button import Button
from src.items.items import Item
import dearpygui.dearpygui as dpg


class ButtonText(Button):
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
                 callback: Callable = None, drag_callback: Callable = None,
                 drop_callback: Callable = None,
                 show: bool = True,
                 enabled: bool = True,
                 pos: Union[List[int], Tuple[int, ...]] = [],
                 filter_key: str = '',
                 tracked: bool = False,
                 track_offset: float = 0.5,
                 small: bool = False,
                 arrow: bool = False,
                 direction: int = 0, **kwargs
                 ):
        self.identifier = dpg.add_button(label=label,
                                         user_data=user_data,
                                         use_internal_label=use_internal_label,
                                         tag=tag,
                                         width=width,
                                         height=height,
                                         indent=indent,
                                         parent=parent,
                                         before=before,
                                         payload_type=payload_type,
                                         callback=callback,
                                         drop_callback=drop_callback,
                                         show=show,
                                         enabled=enabled,
                                         pos=pos,
                                         filter_key=filter_key,
                                         tracked=tracked,
                                         track_offset=track_offset,
                                         small=small,
                                         arrow=arrow,
                                         direction=direction,
                                         **kwargs
                                         )
