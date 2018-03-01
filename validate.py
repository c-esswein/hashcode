

def points(cars, bonus):
 totalScore = 0

 for car in cars:
   totalScore += score_car(car, bonus)

 return totalScore

def score_car(car, bonus):
 totalScore = 0

 carTime = 0
 for ride in car.rides:
   rideStart = carTime
   rideEnd = carTime + ride.distance()

   # check if car finished in time
   if rideEnd <= ride.finish:
     totalScore += ride.distance()

     # bonus
     if carTime <= ride.start:
       totalScore += bonus
   else:
     print('no points!')

   carTime = rideEnd

 return totalScore