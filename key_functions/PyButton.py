import pygame

white = (255, 255, 255)
black = (0,0,0)
class PyButton:

    requirements = [
        {
            "var_name": "color",
            "default": white
        },
        {
            "var_name": "hover_color",
            "default": white
        },

        {
            "var_name": "position",
            "default": (0, 0)
        },
        {
            "var_name": "size",
            "default": (100, 50)
        },

        {"var_name": "onclick", "default": False}, # [Key, Optional(boolean)]

        "text",
        {
            "var_name": "text_color",
            "default": black
        },

        "font",
        "screen",
    ] # This is for properties not set by __init__ itself. The only exception you shouldnt put here is "button"
    Properties = {}
    def __init__(self, **kwargs):

        for k in kwargs.keys():
            self.Properties[k] = kwargs[k]

        self.Properties["button"] = pygame.Rect(self.Properties["position"], self.Properties["size"])

    def Render(self):
        props = self.Properties
        Screenie: pygame.Surface | None = ('screen' in props and props['screen'])

        if not Screenie: return
        (
            button_color,
            button_rect,
            font,
            text,
            text_color
        ) = props["color"], props["button"], props["font"], props["text"], props["text_color"]

        pygame.draw.rect(Screenie, button_color, button_rect)

        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=button_rect.center)

        Screenie.blit(text_surface, text_rect)



__all__ = "PyButton",
