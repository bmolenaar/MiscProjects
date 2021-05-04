# Initialize the dictionary to hold our results
rooms = {}


# Function CheckRoom
# Purpose: Validate the user input is correct and valid
# Returns: Validation
def CheckRoom():
    redo = 'y'
    while redo != 'n':
        roomNum = str(input("Please enter the room number: "))
        room = roomNum.lower()
        if len(room) != 4:
            print('Invalid room. The format should  follow l/n as the first char,  char 2/3 as a  number and char 4 as k/s')
            redo = str(input('Would you like to enter another room?'))
        elif not room[0] in ['l', 'n']:
            print('The first character is invalid')
            redo = str(input('Would you like to enter another room?'))
        elif room[1] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print('The second character is invalid')
            redo = str(input('Would you like to enter another room?'))
        elif room[2] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print('The third character is invalid')
            redo = str(input('Would you like to enter another room?'))
        elif room[3].lower() not in ['k', 's']:
            print('The last character is invalid')
            redo = str(input('Would you like to enter another room?'))
        else:
            CalcPrices(room)
            redo = str(input('Would you like to enter another room?'))

    if redo != 'y':
        print('All the rooms and the rate you just checked:')
        for x, y in rooms.items():
            print(str(x) + '...... $' + str(y))


# Function CalcPrices
# Purpose: Performs arithmetic operations on the user input to calculate prices
# Returns: The room entered and the price
def CalcPrices(room):
    baseRate = 60

    if room[0] != 'N':
        baseRate += 20
    if int(room[1]) >= 3:
        baseRate += 30
    if room[3] != 'S':
        baseRate += 10
    toAdd = {room: baseRate}
    rooms.update(toAdd)

    return print('The room ' + room + ' costs $' + str(baseRate))


CheckRoom()
