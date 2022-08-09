# Doomed-PyGui
A Dear pygui wrapper : more object oriented and more documented.
Because we're all doomed to create wrapper of others code, because we're all developers.

I don't guarantee any form of code maintenance or whatever, use this code at your own risk.

Please support Dear PyGui and its creator here : https://github.com/hoffstadt/DearPyGui

## What is the difference with Dear PyGui ?

All functions in dear PyGui come from `dearpygui.py`.

It's not the most user-friendly approach, so I separated them in different classes. It add some hierarchy and stop you
from using the wrong functions on the wrongs items.

Which function can be used on which item is more clear.

example :
```py
# Dear PyGui
window = dpg.add_window()
text_field = dpg.add_input_text(parent=window)
dpg.add_tooltip(parent=text_field)

# Doomed PyGui
window = Window()
text_field = window.add_input_field_text()
text_field.add_tooltip
```

The difference might not look important, but what stop you in dear pygui from using 'add_input_text' onto an input_text
? Your program would crash, you shouldn't do that.

Doomed PyGui, with its more object-oriented structure, let you know with the autocomplete feature of your IDE what
methods you can use and prevent you from doing dumb things !

Moreover, Doomed Pygui give a more intuitive documentation, with examples ! (Or will give ?)

You can use it to understand Dear PyGui better and just not use Doomed PyGui.

## How to use ?

You cannot, yet.

But you can launch the demo with
```sh
python ./doomed_pygui.py
```

## Documentation

You can access the documentation [here](./doc/main.md)


