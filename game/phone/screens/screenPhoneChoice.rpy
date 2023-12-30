#
# Choice screen that works with the phone.
#
# Choices move to the right when phone is open.
# Captions beginning with ".phone" are absorbed by the phone and enable actions
# within its screens.
# Supports making entries insensitive by item kwargs.
#
# See: https://patreon.renpy.org/menu-arguments.html
# See: renpy/exports.py:MenuEntry
# See: renpy/ui.py:ChoiceActionBase
#
screen phoneChoiceScr(phone, items):
    if phone.isOpen:
        style_prefix "pchoicer"
    else:
        style_prefix "pchoice"
    python:
        if phone.rdyChoice:
            phone.scanMenuCaptions(items)
    vbox:
        for item in items:
            if not item.caption.startswith('.phone'):
                textbutton item.caption:
                    action item.action
                    sensitive item.kwargs.get("sensitive", True) and item.action.get_sensitive()

style pchoice_vbox is vbox
style pchoice_button is button
style pchoice_button_text is button_text

style pchoice_vbox:
    xanchor 0.5
    xpos 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style pchoice_button is default:
    properties gui.button_properties("choice_button")

style pchoice_button_text is default:
    properties gui.button_text_properties("choice_button")

style pchoicer_vbox is vbox:
    xanchor 0.5
    xpos 0.75
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style pchoicer_button is default:
    properties gui.button_properties("choice_button")
    padding (50, 5, 50, 5)
    xsize 0.5

style pchoicer_button_text is default:
    properties gui.button_text_properties("choice_button")

