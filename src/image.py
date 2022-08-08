from typing import Optional, Any, Union, List, Tuple, Callable

from src.items.items import Item
import dearpygui.dearpygui as dpg


class Image(Item):
    def __init__(self,
                 texture_tag: Union[int, str],
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
                 source: Union[int, str] = 0,
                 payload_type: str = '$$DPG_PAYLOAD',
                 drag_callback: Callable = None,
                 drop_callback: Callable = None,
                 show: bool = True,
                 pos: Union[List[int], Tuple[int, ...]] = [],
                 filter_key: str = '',
                 tracked: bool = False,
                 track_offset: float = 0.5,
                 tint_color: Union[List[float], Tuple[float, ...]] = (255, 255, 255, 255),
                 border_color: Union[List[float], Tuple[float, ...]] = (0, 0, 0, 0),
                 uv_min: Union[List[float], Tuple[float, ...]] = (0.0, 0.0),
                 uv_max: Union[List[float], Tuple[float, ...]] = (1.0, 1.0),
                 **kwargs
                 ):
        self.identifier = dpg.add_image(
            tag=tag,
            use_internal_label=use_internal_label,
            indent=indent,
            drag_callback=drag_callback,
            track_offset=track_offset,
            label=label,
            pos=pos,
            user_data=user_data,
            show=show,
            filter_key=filter_key,
            parent=parent,
            tracked=tracked,
            before=before,
            payload_type=payload_type,
            drop_callback=drop_callback,
            source=source,
            tint_color=tint_color,
            uv_min=uv_min,
            uv_max=uv_max,
            height=height,
            width=width,
            texture_tag=texture_tag,
            border_color=border_color,
            **kwargs
        )
