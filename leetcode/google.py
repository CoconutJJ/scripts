def solution(T):

    hour_min = T.split(":")

    hour = hour_min[0]

    hour = [c for c in hour]

    minute = hour_min[1]

    minute = [c for c in minute]

    if minute[1] == "?":
        minute[1] = "9"

    if minute[0] == "?":
        minute[0] = "5"

    if hour[1] == "?":
        if hour[0] == "2" or hour[0] == "?":

            hour[1] = "3"

        else:

            hour[1] = "9"

    if hour[0] == "?":

        if int(hour[1]) < 4:

            hour[0] = "2"
        else:
            hour[0] = "1"

    return "".join(hour) + ":" + "".join(minute)


def isBefore(target, room):

    target_room, target_book = target

    curr_room, curr_book = room

    if target_book >= curr_book:

        if target_book == curr_book:

            t_room_lttr = ord(target_room[1].lower()) - 96

            t_room_num = int(target_room[0])

            c_room_lttr = ord(curr_room[1].lower()) - 96

            c_room_num = int(curr_room[0])

            if t_room_num < c_room_num:
                return True
            elif t_room_num == c_room_num:

                if t_room_lttr < c_room_lttr:
                    return True
                else:
                    return False
            else:
                return False

        return True

    return False


def maxBooked(A):

    room_bookings = dict()

    for room_book in A:

        if room_book[0] == "+":

            if room_book[1:] in room_bookings:

                room_bookings[room_book[1:]] += 1
            else:
                room_bookings[room_book[1:]] = 1

    max_room = None

    for r in room_bookings:

        if max_room is None:
            max_room = r
        else:
            if isBefore((r, room_bookings[r]),
                        (max_room, room_bookings[max_room])):
                max_room = r

    return max_room


print(maxBooked(["+0A"]))
