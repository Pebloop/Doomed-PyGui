from typing import Optional, Any, Union, List, Tuple, Callable

from src.items.items import Item
import dearpygui.dearpygui as dpg


class Tooltip(Item):
    def __init__(self,
                 parent: Union[int, str],
                 *,
                 label: str = None,
                 user_data: Any = None,
                 use_internal_label: bool = True,
                 tag: Union[int, str] = 0,
                 show: bool = True,
                 **kwargs
                 ):
        self.identifier = dpg.add_tooltip(
            parent=parent,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            tag=tag,
            show=show,
            **kwargs
        )
