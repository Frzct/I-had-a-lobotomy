import pygame
from tkinter import Tk

from key_functions .All import *

pygame.init()
filler_table = {
    "tk": Tk()
}

# variables
Res_X, Res_Y = (
    filler_table["tk"].winfo_screenwidth(),
    filler_table["tk"].winfo_screenheight()
)


#
del filler_table["tk"] # so it doesn't exist no more
#

running, Display = True, pygame.display
prompt = False
Initialized_Window = Display.set_mode((Res_X / 2, Res_Y / 1.5))
Display.set_caption("Those who know. Balkan rage. Still water.")


MainStorage = Global_Storage(
    screen=Initialized_Window,
    pygame=pygame,
    font=pygame.font.Font(None, 36)
)

# localized class

class Canvas:
    On_Display = {}

    def Insert(self, Object_Files):
        KeyIdsToReturn = []
        for File in Object_Files:

            Key = ("id" in File
                and File["id"]
                or len(self.On_Display.keys()))
            newClassObj = MainStorage.newClass(
                                File["type"],
                                **File["properties"]
                            )

            self.On_Display[Key] = newClassObj

            KeyIdsToReturn.append(Key)

        return KeyIdsToReturn

    def Remove(self, *KeyIds):
        for KeyId in KeyIds:
            if not KeyId in self.On_Display: return print("KeyID is already removed", self.On_Display)
            del self.On_Display[KeyId]

Canva = Canvas()

Canva.Insert([
    {
        "type": "PyButton",
        "id": "CBF DETECTED, LOSER!",
        "properties": {
            "text": "textholder",

        },
    }
])

#Above are the initial objects that should be in

OnDisplay = Canva.On_Display

while running:
    #
    for event in pygame.event.get():

        if event.type != pygame.KEYUP: continue
        if event.key != pygame.K_ESCAPE:
            if event.key == pygame.K_x:
                Canva.Remove("Chud")
            continue


        if not prompt:
            Canva.Insert([
                {
                    "type": "PyButton",
                    "id": "Chud",
                    "properties": {
                        "text": "You sure you wanna quit little chud?",
                        "position": (25, 50),
                        "size": (250, 200),
                        "color": (255, 0, 0),
                    }
                }
            ])
            prompt = True
        else:
            running = False
            continue

    Initialized_Window.fill((0, 0, 0))
    for CanvaItem in OnDisplay.values():
        CanvaItem.Render()

    Display.flip()

pygame.quit()
raise SystemExit
