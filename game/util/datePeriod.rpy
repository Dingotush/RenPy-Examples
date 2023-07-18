#
# Date/Period.
#

    # Name the days of the week.
    # Could be added to if you want an eight day week for example.
    #
define  daysOfWeek = (
        _("Monday"),        # 0
        _("Tuesday"),       # 1
        _("Wednesday"),     # 2
        _("Thusday"),       # 3
        _("Friday"),        # 4
        _("Saturday"),      # 5
        _("Sunday"),        # 6
        # _("Octoday"),     # 7
    )

    # Name the periods of a day.
    # Can be added to or shortened as needed.
    #
define  periodsOfDay = (
        _("Breakfast"),     # 0
        _("Morning"),       # 1
        _("Lunchtime"),     # 2
        _("Afternoon"),     # 3
        _("Evening"),       # 4
        _("Night"),         # 5
    )

default day = 1             # Day number at start of game
default dayOfWeek = 0       # Day of week at start of game
default period = 0          # Period of day at start of game

default dayOfWeekStr = daysOfWeek[dayOfWeek]    # Current day of week string
default periodStr = periodsOfDay[period]       # Current period string

init python:

    def addPeriod(delta = 1, rollDay=True):
        """
        Advance a number of periods.

        Updates periodStr and dayOfWeekStr too.

        :param delta: Number of periods to advance (default 1)
        :param rollDay: True (default) to advance to the next day,
            False to stop at last period of current day

        NOTE: delta can be negative if you need to travel backwards in time.
        """
        global period, day, dayOfWeek, periodStr, dayOfWeekStr
        oldDay = day
        periods = len(periodsOfDay)
        period += delta
        if rollDay:
            # Use mod math to advance period, day, dayOfWeek.
            day += period // periods
            dayOfWeek += period // periods
            period %= periods
            dayOfWeek %= len(daysOfWeek)
            dayOfWeekStr = daysOfWeek[dayOfWeek]
        else:
            if period >= periods:
                period = periods - 1
            elif period < 0:
                period = 0
        periodStr = periodsOfDay[period]
        # Announce time/day change if self-voicing.
        if day == oldDay:
            alt(_("It is now [periodStr!t]."))
        else:
            alt(_("It is now [periodStr!t] of day [day], a [dayOfWeekStr!t]"))



    def nextDayPer(delta = 1):
        """
        Advance to the start of the next day.

        Updates periodStr and dayOfWeekStr too.

        :param delta: Number of days to advance (default 1)

        NOTE: delta can be negative if you need to travel backwards in time.
        """
        global period, day, dayOfWeek, periodStr, dayOfWeekStr
        period = 0
        day += delta
        dayOfWeek += delta
        dayOfWeek %= len(daysOfWeek)
        dayOfWeekStr = daysOfWeek[dayOfWeek]
        periodStr = periodsOfDay[period]
        alt(_("It is now [periodStr!t] of day [day], a [dayOfWeekStr!t]"))



    def isLastPeriod():
        """
        Is this the last period of the day?

        :return: True if it is the last period.
        """
        return period == len(periodsOfDay) - 1



    def isWorkDayPer():
        """
        Is this a work day?

        :return: True if it is.
        """
        return dayOfWeek <= 4


