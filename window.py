from subprocess import Popen, PIPE

def quicktime_values():

    window = '''
        tell application "System Events" to tell application process "QuickTime Player"
        set s to size of window 1
        set p to position of window 1
        end tell
        return {s, p}
      '''

    proc = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    window_data, error = proc.communicate(window)

    return window_data
