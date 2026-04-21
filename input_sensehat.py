class InputSenseHat(InputBase):
    """
    Input handler for the Sense HAT joystick.

    This class reads input from the Sense HAT joystick and maps it to the defined key codes.
    """

    def __init__(self, sense_hat):
        """
        Initialize the InputSenseHat with a Sense HAT instance.

        Args:
            sense_hat: An instance of the Sense HAT class.
        """
        self.sense_hat = sense_hat

    def read_key(self) -> Keys:
        """
        Read a key input from the Sense HAT joystick and return its corresponding key code.

        Returns:
            An enumeration member of Keys based on the joystick input.
        """
        events = self.sense_hat.stick.get_events()
        if not events:
            return Keys.UNKNOWN

        event = events[0]  # Get the first event
        if event.action != "pressed":
            return Keys.UNKNOWN

        if event.direction == "up":
            return Keys.UP
        elif event.direction == "down":
            return Keys.DOWN
        elif event.direction == "left":
            return Keys.LEFT
        elif event.direction == "right":
            return Keys.RIGHT
        elif event.direction == "middle":
            return Keys.ENTER

        return Keys.UNKNOWN