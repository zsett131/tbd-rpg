PROCESSING = []


class Animation:
    def __init__(self, base, seconds):
        self.base = base
        self.seconds = seconds
        self.finished = False
        self.startTime = None
        self.stopTime = None


class TextWriter(Animation):
    def __init__(self, base, seconds, text, callback):
        Animation.__init__(self, base, seconds)
        self.text = text
        self.currentIndex = 0
        self.finalText = ''
        self.callback = callback

    def process(self):
        divIncrement = len(self.text) / (self.seconds * self.base.clock.get_fps())
        self.currentIndex += divIncrement
        text = self.text[len(self.finalText):int(self.currentIndex)]
        self.finalText += text
        self.callback(self.finalText)
        if self.finalText == self.text:
            self.stop()

    def start(self):
        PROCESSING.append(self)

    def stop(self):
        PROCESSING.remove(self)


