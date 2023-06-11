from pynput.keyboard import Listener
import json

combinations = {
    "'\\x01'": "ctrl+a",
    "'\\x02'": 'ctrl+b',
    "'\\x03'": 'ctrl+c',
    "'\\x04'": 'ctrl+d',
    "'\\x05'": 'ctrl+e',
    "'\\x06'": 'ctrl+f',
    "'\\x07'": 'ctrl+g',
    "'\\x08'": 'ctrl+h',
    "'\\t'": 'ctrl+i',
    "'\\n'": 'ctrl+j',
    "'\\x0b'": 'ctrl+k',
    "'\\x0c'": 'ctrl+l',
    "'\\m'": 'ctrl+m',
    "'\\x0e'": 'ctrl+n',
    "'\\x0f'": 'ctrl+o',
    "'\\x10'": 'ctrl+p',
    "'\\x11'": 'ctrl+q',
    "'\\x12'": 'ctrl+r',
    "'\\x13'": 'ctrl+s',
    "'\\x14'": 'ctrl+t',
    "'\\x15'": 'ctrl+u',
    "'\\x16'": 'ctrl+v',
    "'\\x17'": 'ctrl+w',
    "'\\x18'": 'ctrl+x',
    "'\\x19'": 'ctrl+y',
    "'\\x1a'": 'ctrl+z',
    "<191>": 'ctrl+/',
}


class MyException(Exception):
    pass


def on_press(key):
    # Open file
    with open("keycount.json", "r") as fp:
        keycount_dict = json.load(fp)
        # Format Ctrl+key combinations (e.g. Ctrl+a)
        if format(key) in combinations:
            k = combinations[format(key)]
        # Format Single Quote character
        elif format(key) == "\"'\"":
            k = "\'"
        # Format Double Quote character (characters, numbers, and symbols)
        elif format(key).startswith("'") and format(key).endswith("'"):
            k = eval(format(key))
        # The rest of the keys (esc, shift, etc.)
        else:
            k = format(key)
        print('Pressed key:', k)
        pressed_key = k
        # Increment the key count
        keycount_dict[pressed_key] = keycount_dict.get(pressed_key, 0) + 1
        # Sort the dictionary by value (descending order)
        sorted_keycount_list = sorted(
            keycount_dict.items(), key=lambda x: x[1], reverse=True)
        # Convert the sorted list to a dictionary
        keycount_dict = dict(sorted_keycount_list)
    # Write the dictionary to the file
    with open("keycount.json", "w") as fp:
        json.dump(keycount_dict, fp)


    # Collect events until released
with Listener(
        on_press=on_press) as listener:
    try:
        listener.join()
    except MyException as e:
        print('{0} was pressed'.format(e.args[0]))
