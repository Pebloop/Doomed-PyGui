from typing import Optional, Any, Union, List, Tuple, Callable
from src.items.items import Item
import dearpygui.dearpygui as dpg
from src.items.tippable_item import TippableItem


class Clipper(TippableItem):
    def __init__(self,
                 *,
                 label: str = None,
                 user_data: Any = None,
                 use_internal_label: bool = True,
                 tag: Union[int, str] = 0,
                 width: int = 0,
                 indent: int = -1,
                 parent: Union[int, str] = 0,
                 before: Union[int, str] = 0,
                 show: bool = True,
                 delay_search: bool = False,
                 **kwargs
                 ):
        self.identifier = dpg.add_clipper()
