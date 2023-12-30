#
# Message list screen.
#
screen appMsgListScr(phone, app):
    window id "phoneApp":
        style 'msgListWindow'
        side "t":
            xfill True
            yfill True
            vbox:
                xfill True
                # yfill True
                hbox:
                    xfill True
                    text _("Messages"):
                        style 'msgListTitle'
                vpgrid:
                    cols 1
                    spacing 5
                    draggable True
                    mousewheel True
                    # scrollbars "vertical"
                    xfill True
                    ypos 0.0
                    yanchor 0.0
                    # yfill True
                    for who, contact in app.msgList():
                        if contact.unreadMsg:
                            side "c r":
                                textbutton who:
                                    xfill True
                                    style 'msgListTextButton'
                                    action Function(phone.startApp, 'msgDx', 'msgList', contact)
                                text str(contact.unreadMsg):
                                    color '#f40'
                        else:
                            textbutton who:
                                xfill True
                                style 'msgListTextButton'
                                action Function(phone.startApp, 'msgDx', 'msgList', contact)



style msgListWindow:
    background Solid('#999')
    xpadding 4

style msgListTitle:
    xanchor 0.5
    xpos 0.5

style msgListTextButton is button

style msgListTextButton_text is button_text:
    idle_color '#000'
    hover_color '#FFC'

