import loader
from model import Car
import operator
from validate import points
from score import score
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


if __name__ == "__main__":
    
    # ---- config ----
    parser = ArgumentParser("hashcode runner",
                            formatter_class=ArgumentDefaultsHelpFormatter,
                            conflict_handler='resolve')
    parser.add_argument('--ride_distance', type=int, default=1)
    parser.add_argument('--bonus', type=int, default=1)
    parser.add_argument('--wait_time', type=int, default=1)
    parser.add_argument('--distance_to_coi', type=int, default=1)
    parser.add_argument('--distance_to_start', type=int, default=1)
    parser.add_argument('--file', type=str, default='a')
    params = parser.parse_args()


    file_dict = {
        'a': 'a_example',
        'b': 'b_should_be_easy',
        'c': 'c_no_hurry',
        'd': 'd_metropolis',
        'e': 'e_high_bonus',
    }
    FILE = file_dict[params.file]

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
                    ride_scores[ride] = score(params, ride, car, definition.bonus, center)

            if len(ride_scores) <= 0:
                continue

            ride_scores = sorted(ride_scores.items(), key=operator.itemgetter(1))

            # assign best ride
            best_ride = ride_scores[-1][0]
            car.assign_ride(best_ride)
            del indexed_rides[best_ride.index]
            changed = True
            nb_assigned_rides += 1
    
    points, bonusRides = points(cars, loaded_input.definition.bonus)
    print('total points: {}, bonus rides: {}'.format(points, bonusRides))
    print('assigned {} of {} total rides'.format(nb_assigned_rides, len(loaded_input.rides)))

    params_dic = {
        'ride_distance': params.ride_distance,
        'bonus': params.bonus,
        'wait_time': params.wait_time,
        'distance_to_coi': params.distance_to_coi,
        'distance_to_start': params.distance_to_start,
        'file': params.file,
        'score': points
    }
    paramStr = ''
    for param_key in params_dic:
        paramStr += '{}-{}#'.format(param_key, params_dic[param_key])

    with open('outputs/{}{}.out'.format(FILE, paramStr), 'w') as file:
        for car in cars:
            file.write(str(car) + "\n")

