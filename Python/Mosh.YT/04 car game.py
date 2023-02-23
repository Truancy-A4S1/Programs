want_to_quit = False
command = "Init"
prev_state = "Init"

while want_to_quit == False:
    command = input(" >")

    if command.lower() == "help":
        print("\tstart - to start the car")
        print("\tstop - to stop the car")
        print("\tquit - to exit")

    elif command.lower() == "start":
        if command == prev_state:
            print("Car already started.")
        else:
            print("Car started... Ready to go!")

    elif command.lower() == "stop":
        if command == prev_state:
            print("Car already stopped.")
        else:
            print("Car stopped.")

    elif command.lower() == "quit":
        print("Bye!")
        want_to_quit = True

    else:
        print("I don't understand that...")

    prev_state = command
