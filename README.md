# MCU Config Generator

A simple Python tool that converts hardware configuration into ready-to-use firmware code for microcontrollers.

## What It Does

Instead of manually writing initialization code for your microcontroller peripherals, describe your hardware setup in a JSON file and get the firmware code automatically generated.

**Input (config.json):**
```json
{
  "board": "ESP32",
  "peripheral": "I2C",
  "sda": 21,
  "scl": 22
}
```

**Output (output.c):**
```c
#include <Wire.h>

void setup() {
    Wire.begin(21, 22);
}

void loop() {}
```

## How to Use

1. Edit `config.json` with your hardware configuration
2. Run the generator:
   ```bash
   python generator.py
   ```
3. Find your generated firmware in `output.c`
4. Upload to your microcontroller using Arduino IDE or PlatformIO

## Supported Configurations

Currently supports:
- **Board:** ESP32
- **Peripheral:** I2C
- **Pins:** Custom SDA and SCL pins

## Files

- `config.json` - Hardware configuration input
- `generator.py` - Code generation script
- `output.c` - Generated firmware (auto-created)

## Requirements

- Python 3.x
- No external dependencies needed

## Future Enhancements

- Support for more peripherals (SPI, UART, GPIO)
- Support for more boards (Arduino Uno, ESP8266, STM32)
- Multiple peripheral configurations
- Custom output formats (.ino, .cpp, .h)
