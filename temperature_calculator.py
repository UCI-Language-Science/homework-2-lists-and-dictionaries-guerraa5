# Write a program that continuously prompts the user for a 
# temperture (in the scale of your choosing). Every time 
# the user inputs a temperature, the program should report 
# the mean of all the values entered so far. When the user
# types in 'quit' the program should terminate.
#
# An example interaction might look like
# Input a temperature
# >> 42
# The average temperature so far is 42
# Input a temperature
# >> 26
# The average temperature so far is 34.0
# Input a temperature
# >> 52
# The average temperature so far is 40.0
# >> quit
# Goodbye
#
# You can use the sum function to sum all the values in a list
# sum(<list>)

def temperature_calculator():
    temperatures = []

    while True:
        temp_input = input("Input a temperature (type 'quit' to terminate program): ")

        if temp_input == "quit":
            print("Goodbye")
            break

        temperature = float(temp_input)
        temperatures.append(temperature)

        average = sum(temperatures) / len(temperatures)
        print(f"The average temperature so far is {average:.1f}")
    

if __name__ == "__main__":
    temperature_calculator()