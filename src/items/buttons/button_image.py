from typing import Any, Union, Callable, List, Tuple

from src.items.buttons.button import Button
from src.items.items import Item
import dearpygui.dearpygui as dpg


class ButtonImage(Button):
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
                 callback: Callable = None,
                 drag_callback: Callable = None,
                 drop_callback: Callable = None,
                 show: bool = True,
                 enabled: bool = True,
                 pos: Union[List[int], Tuple[int, ...]] = [],
                 filter_key: str = '',
                 tracked: bool = False,
                 track_offset: float = 0.5,
                 frame_padding: int = -1,
                 tint_color: Union[List[float], Tuple[float, ...]] = (255, 255, 255, 255),
                 background_color: Union[List[float], Tuple[float, ...]] = (0, 0, 0, 0),
                 uv_min: Union[List[float], Tuple[float, ...]] = (0.0, 0.0),
                 uv_max: Union[List[float], Tuple[float, ...]] = (1.0, 1.0),
                 **kwargs
                 ):
        self.identifier = dpg.add_image_button(
            texture_tag=texture_tag,
            drop_callback=drop_callback,
            height=height,
            tracked=tracked,
            before=before,
            parent=parent,
            payload_type=payload_type,
            filter_key=filter_key,
            callback=callback,
            user_data=user_data,
            indent=indent,
            track_offset=track_offset,
            enabled=enabled,
            drag_callback=drag_callback,
            use_internal_label=use_internal_label,
            width=width,
            label=label,
            pos=pos,
            show=show,
            tag=tag,
            source=source,
            uv_max=uv_max,
            uv_min=uv_min,
            tint_color=tint_color,
            frame_padding=frame_padding,
            background_color=background_color,
            **kwargs
        )
