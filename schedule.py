import loader
from model import Car
import operator
from validate import points

def score(ride, car, bonus, center_of_interest):
    # distance is good
    ride_distance = ride.distance()
    score = ride_distance

    # do we get bonus?
    x, y = car.current_position()
    if ride.reachable_on_time(car.time, x, y):
        score += bonus

    # does this ride take us far away from the center of interest?
    coi_x, coi_y = center_of_interest
    distance_to_coi = abs(coi_x - ride.x) + abs(coi_y - ride.y)
    score -= distance_to_coi

    # do we have a wait time for this ride to start?
    wait_time = ride.wait_time_until_earliest_start(car.time, x, y)
    score -= wait_time

    # is it far away?
    distance_to_start = abs(ride.a - x) + abs(ride.b - y)
    score -= distance_to_start
    
    return score

if __name__ == "__main__":
    #FILE = 'a_example'
    FILE = 'b_should_be_easy'
    #FILE = 'c_no_hurry'

    loaded_input = loader.load_input('inputs/{}.in'.format(FILE))
    definition = loaded_input.definition
    rides = loaded_input.rides

    center = (int(definition.rows / 2.0), int(definition.columns / 2.0))

    print('Scheduling {} rides on {} cars for bonus {}'.format(len(rides), definition.vehicles, definition.bonus))

    # initialize
    cars = [Car() for i in range(loaded_input.definition.vehicles)]
    indexed_rides = dict()
    for ride in rides:
        indexed_rides[ride.index] = ride

    # schedule
    nb_assigned_rides = 0

    changed = True
    while changed == True:
        changed = False
        for car in cars:
            ride_scores = dict()
            for index in indexed_rides:
                ride = indexed_rides[index]
                if car.can_assign_ride(ride):
                    ride_scores[ride] = score(ride, car, definition.bonus, center)

            if len(ride_scores) <= 0:
                continue

            ride_scores = sorted(ride_scores.items(), key=operator.itemgetter(1))

            # assign best ride
            best_ride = ride_scores[-1][0]
            car.assign_ride(best_ride)
            del indexed_rides[best_ride.index]
            changed = True
            nb_assigned_rides += 1
    
    points = points(cars, loaded_input.definition.bonus)
    print('total points: {}'.format(points))
    print('assigned {} of {} total rides'.format(nb_assigned_rides, len(loaded_input.rides)))

    with open('outputs/{}.out'.format(FILE), 'w') as file:
        for car in cars:
            file.write(str(car) + "\n")