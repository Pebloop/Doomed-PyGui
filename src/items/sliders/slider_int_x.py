from typing import Any, Union, Callable, Tuple, List

from src.items.items import Item
import dearpygui.dearpygui as dpg

from src.items.sliders.slider import Slider


class SliderIntX(Slider):
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
                 default_value: Union[List[int], Tuple[int, ...]] = (0, 0, 0, 0),
                 size: int = 4,
                 no_input: bool = False,
                 clamped: bool = False,
                 min_value: int = 0,
                 max_value: int = 100,
                 format: str = '%d',
                 **kwargs
                 ):
        self.identifier = dpg.add_slider_intx(tracked=tracked,
                                              before=before,
                                              drop_callback=drop_callback,
                                              parent=parent,
                                              label=label,
                                              user_data=user_data,
                                              use_internal_label=use_internal_label,
                                              filter_key=filter_key,
                                              payload_type=payload_type,
                                              track_offset=track_offset,
                                              indent=indent,
                                              width=width,
                                              pos=pos,
                                              tag=tag,
                                              show=show,
                                              enabled=enabled,
                                              callback=callback,
                                              default_value=default_value,
                                              drag_callback=drag_callback,
                                              source=source,
                                              no_input=no_input,
                                              max_value=max_value,
                                              min_value=min_value,
                                              clamped=clamped,
                                              format=format,
                                              size=size,
                                              **kwargs
                                              )
