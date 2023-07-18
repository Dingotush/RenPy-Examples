    # Simple screen top right to show day, day of week (first three letters),
    # and period.
    # Should probably move this to a separate file.
    #
screen datePeriodScr():
    frame:
        xalign 1.0
        yalign 0.0
        text _("Day [day] [dayOfWeekStr:.3s!t] [periodStr!t]"):
            alt ""