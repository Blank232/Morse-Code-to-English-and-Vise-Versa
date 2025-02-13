# Morse Code to English and Vise-Versa

This is a Python-based Morse Code Converter that allows users to translate text between English and Morse code. The program automatically detects whether the input is in English or Morse code and converts it accordingly.

## Features
- Convert English text to Morse code.
- Convert Morse code to English.
- Automatically detects input type.
- Supports letters (A-Z), numbers (0-9), and common punctuation (, . ? / - ( )).

## How It Works
- If the input contains `.` or `-` and includes spaces or `/`, it is interpreted as Morse code and converted to English.
- Otherwise, the input is assumed to be English and converted to Morse code.

## Usage
1. Run the script in a Python environment.
2. Enter your message when prompted.
3. The program will detect the input type and convert it accordingly.
4. The converted message will be displayed.

## Example
```bash
Enter message: Hello World
Original : Hello World
Converted: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

```bash
Enter message: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
Original : .... . .-.. .-.. --- / .-- --- .-. .-.. -..
Converted: HELLO WORLD
```

## Installation
1. Install Python (if not already installed).
2. Copy and save the script as `morse_code.py`.
3. Run the script using:
   ```bash
   python morse_code.py
   ```

## Contributing
Contributions are welcome! 

