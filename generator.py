

import json  # this is build in python to read/write in json files 

def generate_code(config):
    """
    Core function that converts configuration dictionary into firmware code.
    
    Args:
        config (dict): Configuration data containing:
            - board: Microcontroller board name (e.g., "ESP32", "Arduino Uno")
            - peripheral: Hardware interface type (e.g., "I2C", "SPI", "UART")
            - Additional pins/settings specific to the peripheral
    
    Returns:
        str: Generated C/C++ firmware code ready to compile
    """
    # Extract the board type (which microcontroller we're targeting)
    board = config.get("board")
    
    # Extract the peripheral type (what hardware interface we're setting up)
    peripheral = config.get("peripheral")

    # Check if we're generating code for ESP32 board with I2C peripheral
    if board == "ESP32" and peripheral == "I2C":
        # I2C (Inter-Integrated Circuit) is a two-wire serial communication protocol
        # SDA = Serial Data line (transmits data between devices)
        # SCL = Serial Clock line (synchronizes data transfer timing)
        sda = config.get("sda")  # Get SDA pin number (e.g., GPIO 21 on ESP32)
        scl = config.get("scl")  # Get SCL pin number (e.g., GPIO 22 on ESP32)

        # Generate Arduino/ESP32 firmware code using f-string template
        return f"""
#include <Wire.h>  // Arduino Wire library for I2C communication

// setup() runs once when the microcontroller boots up
void setup() {{
    // Initialize I2C bus with custom SDA and SCL pins
    // Wire.begin(sda_pin, scl_pin) configures the I2C hardware
    Wire.begin({sda}, {scl});
}}

// loop() runs repeatedly after setup() completes
void loop() {{
    // Your main program logic goes here
    // (currently empty - you'd add I2C read/write operations here)
}}
"""
    else:
        # If board/peripheral combination isn't supported, return error comment
        return "// Unsupported board or peripheral"

def main():
    """
    Main entry point of the script.
    Workflow:
    1. Read configuration from JSON file
    2. Generate firmware code based on config
    3. Write generated code to output file
    """
    # Input file path (JSON file containing hardware configuration)
    input_file = "config.json"
    
    # Open and parse the JSON configuration file
    with open(input_file) as f:
        config = json.load(f)  # Convert JSON text to Python dictionary

    # Call the code generator function with our configuration
    code = generate_code(config)

    # Write the generated firmware code to output file
    with open("output.c", "w") as f:
        f.write(code)

    # Confirm successful generation to the user
    print("Firmware code generated in output.c")

# Standard Python idiom - only run main() if script is executed directly
# (not imported as a module by another script)
if __name__ == "__main__":
    main()
