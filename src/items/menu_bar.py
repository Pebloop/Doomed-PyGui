from typing import Optional, Any, Union

from src.items.items import Item
import dearpygui.dearpygui as dpg
from src.items.tippable_item import TippableItem


class MenuBar(TippableItem):
    def __init__(self,
                 *,
                 label: Optional[str] = None,
                 user_data: Optional[Any] = None,
                 use_internal_label: bool = True,
                 tag: Union[int, str] = 0,
                 indent: int = -1,
                 parent: Union[int, str] = 0,
                 show: bool = True,
                 delay_search: bool = False,
                 **kwargs: Any
                 ):
        self.identifier = dpg.add_menu_bar(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            tag=tag,
            indent=indent,
            parent=parent,
            show=show,
            delay_search=delay_search,
            **kwargs
        )
