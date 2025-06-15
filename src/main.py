import ttkbootstrap
import tkinter
import langful

from . import secure


class main:

    def __init__(self) -> None:
        self.langful = langful.langful()
        self.root = tkinter.Tk()
        self.root.geometry("1000x600")
        self.init()
        self.update_language()

    def run(self) -> None:
        self.root.mainloop()

    def init(self) -> None:
        pass

    def update_language(self) -> None:
        self.root.title(self.langful.get("title"))


if __name__ == "__main__":
    main().run()
