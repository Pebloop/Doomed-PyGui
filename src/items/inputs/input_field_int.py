from typing import Any, Union, Callable, Tuple, List

from src.items.inputs.input_field import InputField
from src.items.items import Item
import dearpygui.dearpygui as dpg

from src.items.tippable_item import TippableItem


class InputFieldInt(InputField):
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
                 default_value: int = 0,
                 min_value: int = 0,
                 max_value: int = 100,
                 step: int = 1,
                 step_fast: int = 100,
                 min_clamped: bool = False,
                 max_clamped: bool = False,
                 on_enter: bool = False,
                 readonly: bool = False,
                 **kwargs
                 ):
        self.identifier = dpg.add_input_int(
            default_value=default_value,
            use_internal_label=use_internal_label,
            width=width,
            source=source,
            track_offset=track_offset,
            drag_callback=drag_callback,
            tag=tag,
            pos=pos,
            min_value=min_value,
            callback=callback,
            max_value=max_value,
            payload_type=payload_type,
            drop_callback=drop_callback,
            on_enter=on_enter,
            user_data=user_data,
            filter_key=filter_key,
            enabled=enabled,
            indent=indent,
            readonly=readonly,
            before=before,
            tracked=tracked,
            max_clamped=max_clamped,
            parent=parent,
            min_clamped=min_clamped,
            step_fast=step_fast,
            label=label,
            show=show,
            step=step,
            **kwargs
        )
