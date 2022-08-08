from typing import Optional, Any, Union, List, Tuple, Callable

from src.items.items import Item
import dearpygui.dearpygui as dpg

from src.items.sliders.slider import Slider


class Slider3D(Slider):
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
                 source: Union[int, str] = 0,
                 payload_type: str = '$$DPG_PAYLOAD',
                 callback: Callable = None,
                 drag_callback: Callable = None,
                 drop_callback: Callable = None,
                 show: bool = True,
                 pos: Union[List[int], Tuple[int, ...]] = [],
                 filter_key: str = '',
                 tracked: bool = False,
                 track_offset: float = 0.5,
                 default_value: Union[List[float], Tuple[float, ...]] = (0.0, 0.0, 0.0, 0.0),
                 max_x: float = 100.0,
                 max_y: float = 100.0,
                 max_z: float = 100.0,
                 min_x: float = 0.0,
                 min_y: float = 0.0,
                 min_z: float = 0.0,
                 scale: float = 1.0,
                 **kwargs
                 ):
        self.identifier = dpg.add_3d_slider(label=label,
                                            user_data=user_data,
                                            parent=parent,
                                            height=height,
                                            width=width,
                                            scale=scale,
                                            default_value=default_value,
                                            use_internal_label=use_internal_label,
                                            show=show,
                                            tag=tag,
                                            pos=pos,
                                            callback=callback,
                                            filter_key=filter_key,
                                            payload_type=payload_type,
                                            track_offset=track_offset,
                                            drag_callback=drag_callback,
                                            drop_callback=drop_callback,
                                            indent=indent,
                                            tracked=tracked,
                                            before=before,
                                            source=source,
                                            max_x=max_x,
                                            max_y=max_y,
                                            max_z=max_z,
                                            min_x=min_x,
                                            min_y=min_y,
                                            min_z=min_z,
                                            **kwargs
                                            )
        
