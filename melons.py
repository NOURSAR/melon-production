"""melon"""
import robots


class Melon:
    """Melon."""

    def __init__(self, melon_type):
        """Initialize melon.

        melon_type: type of melon being built.
        """

        self.melon_type = melon_type
        self.weight = 0.0
        self.color = None
        self.stickers = []

    def prep(self):
        """Prepare the melon."""

        robots.cleanerbot.clean(self)
        robots.stickerbot.apply_logo(self)

    def __str__(self):
        """Print out information about melon."""

        if self.weight <= 0:
            return self.melon_type
        else:
            return f"{self.color} {self.weight:.2f} lbs {self.melon_type}"


# FIXME: Add Squash class definition here.
class Squash(Melon):
    """Add a Squash class to melons.py to handle winter squashes."""
    def __init__(self, melon_type):
        super().__init__('squash')

    def prep(self):
        """ prep and paint"""
        robots.cleanerbot.clean(self)
        robots.stickerbot.apply_logo(self)
        robots.painterbot.paint(self)
        