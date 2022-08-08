from typing import Optional, Any, Union, List, Tuple, Callable

from src.items.container import Container
from src.items.items import Item
import dearpygui.dearpygui as dpg


class ChildWindow(Container):

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
                 drop_callback: Callable = None,
                 show: bool = True,
                 pos: Union[List[int], Tuple[int, ...]] = [],
                 filter_key: str = '',
                 delay_search: bool = False,
                 tracked: bool = False,
                 track_offset: float = 0.5,
                 border: bool = True,
                 autosize_x: bool = False,
                 autosize_y: bool = False,
                 no_scrollbar: bool = False,
                 horizontal_scrollbar: bool = False,
                 menubar: bool = False,
                 **kwargs
                 ):
        self.identifier = dpg.add_child_window(track_offset=track_offset,
                                               payload_type=payload_type,
                                               filter_key=filter_key,
                                               user_data=user_data,
                                               use_internal_label=use_internal_label,
                                               height=height,
                                               indent=indent,
                                               menubar=menubar,
                                               width=width,
                                               delay_search=delay_search,
                                               no_scrollbar=no_scrollbar,
                                               horizontal_scrollbar=horizontal_scrollbar,
                                               show=show,
                                               parent=parent,
                                               tag=tag,
                                               label=label,
                                               pos=pos,
                                               drop_callback=drop_callback,
                                               tracked=tracked,
                                               before=before,
                                               border=border,
                                               autosize_x=autosize_x,
                                               autosize_y=autosize_y,
                                               **kwargs
                                               )
