from typing import Optional, Any, Union, List, Tuple, Callable

from src.items.container import Container
from src.items.group import Group

import dearpygui.dearpygui as dpg

from src.items.items import Item
from src.items.menu_bar import MenuBar


class Window(Container):
    def on_loop(self):
        pass

    def on_resize(self):
        pass

    def __init__(self,
                 label: Optional[str] = None,
                 user_data: Optional[Any] = None,
                 use_internal_label: bool = True,
                 tag: Union[int, str] = 0,
                 width: int = 0,
                 height: int = 0,
                 indent: int = -1,
                 parent: Optional[Union[int, str]] = None,
                 show: bool = True,
                 pos: Union[List[int], Tuple[int, ...]] = [],
                 delay_search: bool = False,
                 min_size: Union[List[int], Tuple[int, ...]] = [100, 100],
                 max_size: Union[List[int], Tuple[int, ...]] = [30000, 30000],
                 menubar: bool = False,
                 collapsed: bool = False,
                 autosize: bool = False,
                 no_resize: bool = False,
                 no_title_bar: bool = False,
                 no_move: bool = False,
                 no_scrollbar: bool = False,
                 no_collapse: bool = False,
                 horizontal_scrollbar: bool = False,
                 no_focus_on_appearing: bool = False,
                 no_bring_to_front_on_focus: bool = False,
                 no_close: bool = False,
                 no_background: bool = False,
                 modal: bool = False,
                 popup: bool = False,
                 no_saved_settings: bool = False,
                 no_open_over_existing_popup: bool = True,
                 on_close: Optional[Callable] = None,
                 **kwargs: Any
                 ):
        self.identifier = dpg.add_window(label=label,
                                         user_data=user_data,
                                         use_internal_label=use_internal_label,
                                         tag=tag,
                                         width=width,
                                         height=height,
                                         indent=indent,
                                         show=show,
                                         pos=pos,
                                         delay_search=delay_search,
                                         min_size=min_size,
                                         max_size=max_size,
                                         menubar=menubar,
                                         collapsed=collapsed,
                                         autosize=autosize,
                                         no_resize=no_resize,
                                         no_title_bar=no_title_bar,
                                         no_move=no_move,
                                         no_scrollbar=no_scrollbar,
                                         no_collapse=no_collapse,
                                         horizontal_scrollbar=horizontal_scrollbar,
                                         no_focus_on_appearing=no_focus_on_appearing,
                                         no_bring_to_front_on_focus=no_bring_to_front_on_focus,
                                         no_close=no_close,
                                         no_background=no_background,
                                         modal=modal,
                                         popup=popup,
                                         no_saved_settings=no_saved_settings,
                                         no_open_over_existing_popup=no_open_over_existing_popup,
                                         on_close=on_close,
                                         **kwargs
                                         )

    def add_menu_bar(self,
                     *,
                     label: Optional[str] = None,
                     user_data: Optional[Any] = None,
                     use_internal_label: bool = True,
                     tag: Union[int, str] = 0,
                     indent: int = -1,
                     show: bool = True,
                     delay_search: bool = False,
                     **kwargs: Any
                     ) -> MenuBar:
        item = MenuBar(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            tag=tag,
            indent=indent,
            parent=self.identifier,
            show=show,
            delay_search=delay_search,
            **kwargs
        )
        self.items.append(item)
        return item
