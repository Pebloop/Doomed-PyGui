from typing import Optional, Any, Union, List, Tuple, Callable

import dearpygui.dearpygui as dpg

from src.items.tippable_item import TippableItem


class Checkbox(TippableItem):
    def __init__(self,
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
                 default_value: bool = False,
                 **kwargs
                 ):
        self.identifier = dpg.add_checkbox(source=source,
                                           tracked=tracked,
                                           before=before,
                                           drop_callback=drop_callback,
                                           filter_key=filter_key,
                                           callback=callback,
                                           drag_callback=drag_callback,
                                           track_offset=track_offset,
                                           payload_type=payload_type,
                                           default_value=default_value,
                                           use_internal_label=use_internal_label,
                                           indent=indent,
                                           user_data=user_data,
                                           parent=parent,
                                           label=label,
                                           pos=pos,
                                           tag=tag,
                                           show=show,
                                           enabled=enabled,
                                           **kwargs
                                           )
