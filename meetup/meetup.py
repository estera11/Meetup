import datetime
from calendar import Calendar
weekdays = {'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5,'Sunday':6}

cal = Calendar()

def meetup_day(year, month, day_of_the_week, which):
    day_names = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    day_of_the_week_as_number = day_names.index(day_of_the_week)
    candidates = [day for day, weekday in cal.itermonthdays2(year,month) if day!=0 and weekday==day_of_the_week_as_number]
    if which=='last':
        meetup_day = candidates[-1]
    elif which=='teenth':
        meetup_day = [day for day in candidates if day>=13 ][0]
    else:
        ordinal = int(which[0])
        if ordinal>len(candidates):
            raise MeetupDayException("No such")
        else:
            meetup_day = candidates[ordinal-1]
    return datetime.date(year, month, meetup_day)

class MeetupDayException(BaseException):
    def _init_ (self,message):
        self.message = message
