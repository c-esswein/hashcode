
def points(cars, bonus):
 totalScore = 0
 bonusRide = 0

 for car in cars:
   carScore, carBonusRide = points_for_car(car, bonus)
   totalScore += carScore
   bonusRide += carBonusRide

 return totalScore, bonusRide

def points_for_car(car, bonus):
 totalScore = 0
 bonusRide = 0

 carTime = 0
 for ride in car.rides:
   rideStart = carTime
   rideEnd = carTime + ride.distance()

   # check if car finished in time
   if rideEnd <= ride.finish:
     totalScore += ride.distance()

     # bonus
     if carTime <= ride.start:
       bonusRide += 1
       totalScore += bonus
   else:
     print('no points!')

   carTime = rideEnd

 return totalScore, bonusRide
 