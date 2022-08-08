from typing import Optional, Any, Union, List, Tuple, Callable
from src.items.items import Item
import dearpygui.dearpygui as dpg
from src.items.tippable_item import TippableItem


class DatePicker(TippableItem):
    def __init__(self,
                 *,
                 label: str = None,
                 user_data: Any = None,
                 use_internal_label: bool = True,
                 tag: Union[int, str] = 0,
                 indent: int = -1,
                 parent: Union[int, str] = 0,
                 before: Union[int, str] = 0,
                 payload_type: str = '$$DPG_PAYLOAD',
                 callback: Callable = None,
                 drag_callback: Callable = None,
                 drop_callback: Callable = None,
                 show: bool = True,
                 pos: Union[List[int], Tuple[int, ...]] = [],
                 filter_key: str = '',
                 tracked: bool = False,
                 track_offset: float = 0.5,
                 default_value: dict = {'month_day': 14, 'year': 20, 'month': 5},
                 level: int = 0,
                 **kwargs
                 ):
        self.identifier = dpg.add_date_picker(
            default_value=default_value,
            drop_callback=drop_callback,
            filter_key=filter_key,
            payload_type=payload_type,
            before=before,
            tracked=tracked,
            parent=parent,
            user_data=user_data,
            callback=callback,
            track_offset=track_offset,
            indent=indent,
            drag_callback=drag_callback,
            use_internal_label=use_internal_label,
            label=label,
            pos=pos,
            show=show,
            tag=tag,
            level=level,
            **kwargs
        )
