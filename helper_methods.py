import os
import json


def quit_msg(msg, error):
    print(msg)
    print("Error:", error)
    quit()


def file_exists(filepath, quit_message=None):
    # Returns True if file exists
    # Otherwise returns False (default) or exits with error message

    if os.path.exists(filepath):
        return True
    else:
        if quit_message:
            print(quit_message)
            exit()
        else:
            return False


def json_read_from_file(filepath):
    file_exists(filepath, f"'{filepath}' doesn't exist.")
    try:
        with open(filepath) as file:
            data = json.load(file)
            file.close()
            return data
    except Exception as error:
        quit_msg("Failed to read from file.", error)


def json_write_to_file(data, filepath, indent=1):
    try:
        with open(filepath, 'w+') as file:
            json.dump(data, file, indent=indent)
            file.close()
    except Exception as error:
        quit_msg("Failed to write to file", error)