import json   

def generate_code(config):
    board = config.get("board")
    peripheral = config.get("peripheral")

    if board == "ESP32" and peripheral == "I2C":
        sda = config.get("sda")
        scl = config.get("scl")

        return f"""
#include <Wire.h>

void setup() {{
    Wire.begin({sda}, {scl});
}}

void loop() {{}}
"""
    else:
        return "// Unsupported board or peripheral"

def main():
    input_file = "config.json"
    with open(input_file) as f:
        config = json.load(f)

    code = generate_code(config)

    with open("output.c", "w") as f:
        f.write(code)

    print("Firmware code generated in output.c")

if __name__ == "__main__":
    main()
