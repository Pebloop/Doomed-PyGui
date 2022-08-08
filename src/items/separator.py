from typing import Any, Union, List, Tuple

from src.items.items import Item
import dearpygui.dearpygui as dpg
from src.items.tippable_item import TippableItem


class Separator(TippableItem):
    def __init__(self,
                 *,
                 label: str = None,
                 user_data: Any = None,
                 use_internal_label: bool = True,
                 tag: Union[int, str] = 0,
                 indent: int = -1,
                 parent: Union[int, str] = 0,
                 before: Union[int, str] = 0,
                 show: bool = True,
                 pos: Union[List[int], Tuple[int, ...]] = [],
                 **kwargs
                 ):
        self.identifier = dpg.add_separator(label=label,
                                            user_data=user_data,
                                            use_internal_label=use_internal_label,
                                            tag=tag,
                                            indent=indent,
                                            parent=parent,
                                            before=before,
                                            show=show,
                                            pos=pos,
                                            **kwargs
                                            )
