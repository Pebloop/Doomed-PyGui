from typing import Optional, Any, Union, List, Tuple, Callable
from src.items.items import Item
import dearpygui.dearpygui as dpg
from src.items.tippable_item import TippableItem


class ColorPicker(TippableItem):
    def __init__(self,
                 default_value: Union[List[int], Tuple[int, ...]] = (0, 0, 0, 255),
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
                 no_alpha: bool = False,
                 no_side_preview: bool = False,
                 no_small_preview: bool = False,
                 no_inputs: bool = False,
                 no_tooltip: bool = False,
                 no_label: bool = False,
                 alpha_bar: bool = False,
                 display_rgb: bool = False,
                 display_hsv: bool = False,
                 display_hex: bool = False,
                 picker_mode: int = 33554432,
                 alpha_preview: int = 0,
                 display_type: int = 8388608,
                 input_mode: int = 134217728,
                 **kwargs
                 ):
        self.identifier = dpg.add_color_picker(
            default_value=default_value,
            use_internal_label=use_internal_label,
            user_data=user_data,
            parent=parent,
            height=height,
            tracked=tracked,
            filter_key=filter_key,
            payload_type=payload_type,
            drop_callback=drop_callback,
            source=source,
            before=before,
            track_offset=track_offset,
            drag_callback=drag_callback,
            indent=indent,
            label=label,
            width=width,
            tag=tag,
            callback=callback,
            show=show,
            enabled=enabled,
            pos=pos,
            no_alpha=no_alpha,
            picker_mode=picker_mode,
            no_inputs=no_inputs,
            alpha_bar=alpha_bar,
            no_tooltip=no_tooltip,
            input_mode=input_mode,
            no_label=no_label,
            display_hex=display_hex,
            display_hsv=display_hsv,
            display_rgb=display_rgb,
            display_type=display_type,
            alpha_preview=alpha_preview,
            no_side_preview=no_side_preview,
            no_small_preview=no_small_preview,
            **kwargs
        )
