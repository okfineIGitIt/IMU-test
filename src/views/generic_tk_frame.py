from abc import ABC


class GenericFrame(ABC):

    def __init__(self, frame, parent_window, *args, **kwargs):
        self.frame = frame
        self.window = parent_window
        super().__init__()

    def configure_ui(self):
        pass
