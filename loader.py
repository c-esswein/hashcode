from csv import reader
from model import Definition, RideCall, LoadedInput

def load_input(file_name):
    rides = []
    with open(file_name, 'r') as file:
        csv_reader = reader(file, delimiter=' ')
        definition = next(csv_reader)
        definition = Definition(*definition)
        index = 0
        for row in csv_reader:
            ride = RideCall(index, *row)
            rides.append(ride)
            index += 1
    return LoadedInput(definition, rides)
