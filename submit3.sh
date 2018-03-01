#!/bin/bash
python schedule.py --file c --distance_to_start 20 &
python schedule.py --file d --distance_to_start 20 &
python schedule.py --file e --bonus 100 --distance_to_coi 10 &
python schedule.py --file c --distance_to_coi 10 &
python schedule.py --file d --distance_to_coi 10 &
python schedule.py --file e --bonus 100 --distance_to_coi 20 &

