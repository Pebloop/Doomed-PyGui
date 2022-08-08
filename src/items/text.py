from typing import Optional, Any, Union, List, Tuple, Callable

from src.items.items import Item
import dearpygui.dearpygui as dpg
from src.items.tippable_item import TippableItem


class Text(TippableItem):
    def __init__(self,
                 *,
                 default_value: str = '',
                 label: Optional[str] = None,
                 user_data: Optional[Any] = None,
                 use_internal_label: bool = True,
                 tag: Union[int, str] = 0,
                 indent: int = -1,
                 parent: Union[int, str] = 0,
                 before: Union[int, str] = 0,
                 source: Union[int, str] = 0,
                 payload_type: str = '$$DPG_PAYLOAD',
                 drag_callback: Optional[Callable] = None,
                 drop_callback: Optional[Callable] = None,
                 show: bool = True,
                 pos: Union[List[int], Tuple[int, ...]] = [],
                 filter_key: str = '',
                 tracked: bool = False,
                 track_offset: float = 0.5,
                 wrap: int = -1,
                 bullet: bool = False,
                 color: Union[List[int], Tuple[int, ...]] = (-255, 0, 0, 255),
                 show_label: bool = False,
                 **kwargs: Any
                 ):
        self.identifier = dpg.add_text(
            default_value=default_value,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            tag=tag,
            indent=indent,
            parent=parent,
            before=before,
            source=source,
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            wrap=wrap,
            bullet=bullet,
            color=color,
            show_label=show_label,
            **kwargs
        )
