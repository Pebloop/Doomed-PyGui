from typing import Optional, Union, Any

import dearpygui.dearpygui as dpg

from src.items.items import Item


class TippableItem(Item):
    tooltip = None

    def add_tooltip(self,
                    *,
                    label: str = None,
                    user_data: Any = None,
                    use_internal_label: bool = True,
                    tag: Union[int, str] = 0,
                    show: bool = True,
                    **kwargs
                    ):
        from src.items.tooltip import Tooltip

        if self.tooltip is not None:
            print("This item has a tooltip already.")
            return self.tooltip

        item = Tooltip(
            parent=self.identifier,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            tag=tag,
            show=show,
            **kwargs
        )
        self.tooltip = item
        return item
