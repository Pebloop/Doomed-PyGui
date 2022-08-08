from typing import Optional, Any, Union, Callable, List, Tuple
import dearpygui.dearpygui as dpg

from src.items.container import Container


class Group(Container):
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
                 payload_type: str = '$$DPG_PAYLOAD',
                 drag_callback: Callable = None,
                 drop_callback: Callable = None,
                 show: bool = True,
                 pos: Union[List[int], Tuple[int, ...]] = [],
                 filter_key: str = '',
                 delay_search: bool = False,
                 tracked: bool = False,
                 track_offset: float = 0.5,
                 horizontal: bool = False,
                 horizontal_spacing: float = -1,
                 xoffset: float = 0.0,
                 **kwargs
                 ):
        self.identifier = dpg.add_group(label=label,
                                        user_data=user_data,
                                        use_internal_label=use_internal_label,
                                        tag=tag,
                                        width=width,
                                        indent=indent,
                                        parent=parent,
                                        before=before,
                                        payload_type=payload_type,
                                        drag_callback=drag_callback,
                                        drop_callback=drop_callback,
                                        show=show,
                                        pos=pos,
                                        filter_key=filter_key,
                                        delay_search=delay_search,
                                        tracked=tracked,
                                        track_offset=track_offset,
                                        horizontal=horizontal,
                                        horizontal_spacing=horizontal_spacing,
                                        xoffset=xoffset,
                                        **kwargs)

        ## ADD ITEMS
