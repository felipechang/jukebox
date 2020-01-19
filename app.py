import threading
import queue
import pafy
import vlc


# Add commands to queue
def console(q):
    while 1:
        cmd = input('> ')
        q.put(cmd)
        if cmd == 'quit':
            break


# Main program
def main():
    cmd_queue = queue.Queue()

    dj = threading.Thread(target=console, args=(cmd_queue,))
    dj.start()

    media = None

    while 1:

        # Get command
        cmd = cmd_queue.get()

        # Quit program
        if cmd == 'quit':
            break

        # Pause stream
        elif cmd == 'pause':
            media.pause()

        # Play command
        elif cmd == 'play':
            media.play()
        else:

            # Youtube IDs have 11 characters
            if len(cmd) != 11:
                print("Invalid ID")
                break
            url = "https://www.youtube.com/watch?v=" + cmd
            audio = pafy.new(url)
            best = audio.getbestaudio()

            # Pause last song
            if media:
                media.pause()

            # Print title to console
            print(audio.title + " - " + audio.duration + " @" + best.bitrate)

            # Play audio
            media = vlc.MediaPlayer(best.url)
            media.play()


main()
