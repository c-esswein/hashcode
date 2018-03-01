class RideCall():
    def __init__(self, index, a, b, x, y, start, finish):
        self.index = index
        self.a = int(a)
        self.b = int(b)
        self.x = int(x)
        self.y = int(y)
        self.start = int(start)
        self.finish = int(finish)
        self.started = None
        
    def distance(self):
        return abs(self.x-self.a) + abs(self.y-self.b)

    def latest_start(self, x_now, y_now):
        latest_start = self.finish - self.distance() - abs(x_now - self.a) - abs(y_now - self.b)
        return latest_start

    def wait_time_until_earliest_start(self, t_now, x_now, y_now):
        arrival_time = t_now + abs(x_now - self.a) - abs(y_now - self.b)
        return self.start - arrival_time

    def reachable_on_time(self, t_now, x_now, y_now):
        if self.wait_time_until_earliest_start(t_now, x_now, y_now) >= 0:
            return True
        else:
            return False

    def reachable(self, t_now, x_now, y_now):
        latest_start = self.latest_start(x_now, y_now)
        if latest_start > t_now:
            return True
        else:
            return False

    def __str__(self):
        return str(self.index)
        
    def __repr__(self):
        return str(self.index)

class Definition:
    def __init__(self, rows, columns, vehicles, rides, bonus, steps):
        self.rows = int(rows)
        self.columns = int(columns)
        self.vehicles = int(vehicles)
        self.rides = int(rides)
        self.bonus = int(bonus)
        self.steps = int(steps)

class LoadedInput():
    def __init__(self, definition, rides):
        self.definition = definition
        self.rides = rides

class Car():
    def __init__(self):
        self.rides = []
        self.time = 0

    def assign_ride(self, ride):
        self.rides.append(ride)
        self.time += self.distance_to_ride(ride) + ride.distance()

    def can_assign_ride(self, ride):
        (x, y) = self.current_position()
        return ride.reachable(self.time, x, y)

    def distance_to_ride(self, ride):
        (x, y) = self.current_position()
        return abs(ride.x-x) + abs(ride.y-y)

    def current_position(self):
        if len(self.rides) <= 0:
            return (0, 0)
        else:
            last_ride = self.rides[-1]
            return (last_ride.x, last_ride.y)

    def __str__(self):
        return '{} {}'.format(len(self.rides), ' '.join([str(ride) for ride in self.rides]))

    def __repr__(self):
        return '{} {}'.format(len(self.rides), ' '.join([str(ride) for ride in self.rides]))

