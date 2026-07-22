import subprocess

# Scripti, joka soittaa Apple musiikin tietystä soittolistasta tietyn kappaleen
def play_song():
    script = '''
    tell application "Musiikki"
        set p to playlist "rokkia ja muuta"
        set t to first track of p whose name is "Wicked Game"
        play t
    end tell
    '''

    subprocess.run(["osascript", "-e", script])

# Palauttaa kappaleen kohdan, joka soi
def get_position():
    script = '''        
    tell application "Musiikki"
        if player state is playing then
            return player position
        else
            return -1
        end if
    end tell
    '''

    result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    output = result.stdout.strip()

    if output:
        return output if float(output) >= 0 else None
    return None