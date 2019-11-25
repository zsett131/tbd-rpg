"""
Module containing animations.
__author__: Zachary Setterquist
"""
PROCESSING = []


class Animation:
    """
    This is a base class for animation processes.
    """
    def __init__(self, base, seconds):
        self.base = base
        self.seconds = seconds
        self.finished = False
        self.startTime = None
        self.stopTime = None


class TextWriter(Animation):
    """
    Draws out text from start to finish at a set rate or within a set
    duration.
    """
    def __init__(self, base, seconds, text, callback, rate=True):
        Animation.__init__(self, base, seconds)
        self.text = text
        self.currentIndex = 0
        self.finalText = ''
        self.callback = callback
        self.divIncrement = 0
        self.rate = rate

    def process(self):
        """
        Method called every frame to continue drawing out text until
        reaching the final character.
        """
        div_increment = self.seconds / self.base.clock.get_fps()
        if not self.rate:
            div_increment = len(self.text) / max(1, (
                        self.seconds * self.base.clock.get_fps()))
        self.currentIndex += div_increment
        text = self.text[len(self.finalText):int(self.currentIndex)]
        self.finalText += text
        self.callback(self.finalText)
        if self.finalText == self.text:
            self.stop()

    def start(self):
        """
        Adds TextWriter instance to PROCESSING to be processed every frame.
        """
        PROCESSING.append(self)

    def stop(self):
        """
        Stops processing for TextWriter.
        """
        PROCESSING.remove(self)
