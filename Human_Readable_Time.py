def main():
    while(True):
        seconds = get_input("input any whole amount of seconds to be formatted", int)
        if seconds < 0:
            print("value cannot be a negative number")
        else:
            break
        
    test_values([69, 696, 6969, 696969, "bruh", 6.21, 3722.32443, -200], time_format)
    time_format(seconds)
def get_input(input_message, input_type):
    while(True):
        raw_input = input(f"{input_message}\n")
        try:
            user_input = input_type(raw_input)
            break
        except ValueError:
            print("this is not a valid input")
    return user_input

#this function is used to simulate what needs to be done to ensure values passed through the program function as intended
#in this situation, although float values would work, i want to prevent confusion so i am testing what functions i can use to prevent floats from entering the system
def test_values(values, function_name):
    for x, value in enumerate(values):
        try:
            if values[x] < 0 or type(values[x]) != int:
                raise
            function_name(values[x])
            test = "success"
        except:
            test = "Failure"
        print(f"Value {x}: {values[x]} of type: {type(values[x])}, was a {test}")

def time_format(seconds):
    remaining_seconds = int(seconds%60)
    minutes = seconds/60
    remaining_minutes = int(minutes%60)
    hours = int(minutes/60)
    if hours > 99:
        print(-1)
    elif hours <= 99:
        print(f"{hours:02d}:{remaining_minutes:02d}:{remaining_seconds:02d}")

main()
