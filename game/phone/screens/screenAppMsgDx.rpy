#
# Messaging screen.
#
transform msgRxAppearTf:
    alpha 0.0
    xoffset 50
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 xoffset 0

transform msgTxAppearTf:
    alpha 0.0
    xoffset -50
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 xoffset 0

screen appMsgDxScr(phone, app):
    default yadj = ui.adjustment()
    python:
        contact = app._contactM
        if contact.unreadMsg:
            yadj.value = float('inf')
            del contact.unreadMsg
        menuResponse = app.getMenuResponse(phone)
    window id "phoneApp":
        style 'msgDxWindow'
        side "t c b":
            xfill True
            yfill True
            hbox:
                xfill True
                text contact._whoM:
                    style 'msgDxWho'
            viewport:
                xfill True
                yfill True
                yadjustment yadj
                draggable True
                mousewheel True
                # scrollbars "vertical"
                vbox:
                    xfill True
                    for msg in contact._msgHistM:
                        $ rx, what = msg
                        $ last = msg is contact._msgHistM[-1]
                        if rx:
                            frame:
                                style 'msgRxFrame'
                                if last:
                                    text what at msgRxAppearTf:
                                        style 'msgDxText'
                                else:
                                    text what:
                                        style 'msgDxText'
                        else:
                            frame:
                                style 'msgTxFrame'
                                if last:
                                    text what at msgTxAppearTf:
                                        style 'msgDxText'
                                else:
                                    text what:
                                        style 'msgDxText'
            if menuResponse:
                textbutton "Send":
                    xanchor 1.0
                    xpos 1.0
                    action menuResponse
            else:
                #null height 1
                text "caption: [app._menuCaptionM]"
                    



style msgDxWindow:
    background Solid('#999')
    xpadding 4

style msgRxFrame:
    background Frame("images/phone/sms-rx-frame.png", 23,23,23,23)
    padding(20,20)
    xsize 0.8
    xpos 0.0
    xanchor 0.0

style msgTxFrame:
    background Frame("images/phone/sms-tx-frame.png", 23,23,23,23)
    padding(20,20)
    xsize 0.8
    xpos 1.0
    xanchor 1.0

style msgDxText:
    color "#000000"

style msgDxWho:
    xanchor 0.5
    xpos 0.5
