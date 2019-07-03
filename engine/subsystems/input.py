import pygame

class Button:
    def __init__(self, name, btnlist):
        self.name = name
        self.type = ""
        self.btnlist = btnlist

    def key(self, evt):
        return evt.key in self.btnlist

    def mouse(self, evt):
        return evt.button in self.btnlist

    def joy(self, evt):
        return evt.joy in self.btnlist

    def get(self, evt):
        pass


class MouseButton(Button):
    def __init__(self, *args):
        super().__init__(*args)
        self.type = "mouse"

    def get(self, evt):
        return self.mouse(evt)


class KeyButton(Button):
    def __init__(self, *args):
        super().__init__(*args)
        self.type = "key"

    def get(self, evt):
        return self.key(evt)


class JoyButton(Button):
    def __init__(self, *args):
        super().__init__(*args)
        self.type = "joy"

    def get(self, evt):
        return self.joy(evt)


class Input:
    _mousepos = (0, 0)
    _current_size = (0, 0)

    def __init__(self, game_manager):
        self.game_manager = game_manager

    @classmethod
    def get_button_down(cls, button):
        events = [(ev.type, ev) for ev in pygame.event.get()]
        evts = []
        for event_type, event in events:
            if pygame.KEYDOWN == event_type and isinstance(button, KeyButton):
                evts.append(button.get(event))
            if pygame.MOUSEBUTTONDOWN == event_type and isinstance(button, MouseButton):
                evts.append(button.get(event))
            if pygame.JOYBUTTONDOWN == event_type and isinstance(button, JoyButton):
                evts.append(button.get(event))
        return True in evts

    @classmethod
    def get_button_up(cls, button):
        events = [(ev.type, ev) for ev in pygame.event.get()]
        evts = []
        for event_type, event in events:
            if pygame.KEYUP == event_type and isinstance(button, KeyButton):
                evts.append(button.get(event))
            if pygame.MOUSEBUTTONUP == event_type and isinstance(button, MouseButton):
                evts.append(button.get(event))
            if pygame.JOYBUTTONUP == event_type and isinstance(button, JoyButton):
                evts.append(button.get(event))
        return True in evts

    @classmethod
    def get_mouse_position(cls):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                cls._mousepos = event.pos
        return cls._mousepos

    @classmethod
    def get_quit(cls):
        return pygame.QUIT in [ev.type for ev in pygame.event.get()]

    @classmethod
    def get_resize(cls):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.VIDEORESIZE:
                cls._current_size = event.size
        return cls._current_size
