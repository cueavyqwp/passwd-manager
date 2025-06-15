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
        ttkbootstrap.Button(
            self.root, command=self.create_file, text=self.langful.get("cerate_file")).pack()
        self.input = ttkbootstrap.Entry(self.root)
        self.input.pack()

    def update_language(self) -> None:
        self.root.title(self.langful.get("title"))

    def create_file(self):
        print(self.input.get())
        print(secure.derive_passwd(self.input.get()))


if __name__ == "__main__":
    main().run()
