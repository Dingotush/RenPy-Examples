#
# Message list screen.
#
screen appMsgListScr(phone, app):
    window id "phoneApp":
        style 'msgListWindow'
        side "t c":
            xfill True
            yfill True
            text _("Messages"):
                style 'phoneAppTitleText'
            viewport:
                xfill True
                yfill True
                draggable True
                mousewheel True
                vbox:
                    xfill True
                    
                    for entry in app.msgList():
                        $ print("Entry: {}".format(entry))
                        $ who, contact = entry
                        $ print("who \"{}\" count {}".format(who, contact.unreadMsg))
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

