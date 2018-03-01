
def score(params, ride, car, bonus, center_of_interest):
    # distance is good
    ride_distance = ride.distance()
    score = params.ride_distance * ride_distance

    # do we get bonus?
    x, y = car.current_position()
    if ride.reachable_on_time(car.time, x, y):
        score += params.bonus *bonus

    # does this ride take us far away from the center of interest?
    coi_x, coi_y = center_of_interest
    distance_to_coi = abs(coi_x - ride.x) + abs(coi_y - ride.y)
    score -= params.distance_to_coi * distance_to_coi

    # do we have a wait time for this ride to start?
    wait_time = ride.wait_time_until_earliest_start(car.time, x, y)
    score -= params.wait_time * wait_time

    # is it far away?
    distance_to_start = abs(ride.a - x) + abs(ride.b - y)
    score -= params.distance_to_start * distance_to_start
    
    return score
