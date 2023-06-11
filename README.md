# Local Keylogger

The **Local Keylogger** is a program designed to accurately tally the frequency of key presses on your keyboard, encompassing regular keystrokes as well as keyboard shortcuts _(e.g., Ctrl+C, Ctrl+V, etc.)_.

This utility allows you to effortlessly track your keyboard activity _(locally)_ and conveniently store the collected data in a file for further analysis or reference purposes.

## Usage

1. Clone the repository to your local machine.
2. Make sure the `keycount.json` is empty (only {}), and in the same directory as the `logger.py` file.
3. Download the required packages (`pynput`, `json`) if you don't have them already.
4. Run the `logger.py` file with the following command: `python logger.py`.
5. The program will automatically start counting your keystrokes, and will sort them ascendingly in the `keycount.json` file.

Made with 🦔 by **Rodrigo Ramirez**.
