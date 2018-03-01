#!/bin/bash
python schedule.py --file c --wait_time 20 &
python schedule.py --file d --wait_time 20 &
python schedule.py --file e --bonus 100 --ride_distance 40 &
python schedule.py --file c --distance_to_coi 50 &
python schedule.py --file d --distance_to_coi 50 &
python schedule.py --file e --bonus 100 --distance_to_coi -10 &

