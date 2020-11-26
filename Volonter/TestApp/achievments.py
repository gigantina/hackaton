from .models import Achievments_From_User, Event, Bookings_From_User


def give_achieve(user, achieve):
    item = Achievments_From_User(user, achieve)
    item.save()


def get_num_events(user):
    history = Bookings_From_User.objects.filter(user_id=user)
    return len(history)



