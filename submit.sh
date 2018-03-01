#!/bin/bash
python schedule.py --file c --bonus 50 --distance_to_coi 0&
python schedule.py --file d --bonus 50&
python schedule.py --file e --bonus 50&
python schedule.py --file c --bonus 50&
python schedule.py --file d --bonus 50 --distance_to_coi 0&

