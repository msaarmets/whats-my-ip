import tkinter as tk
from getIP import IPv4, IPv6
import pyperclip


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.IP4 = self.getIP(4)
        self.IP6 = self.getIP(6)
        if self.IP4 != "No connection":
            pyperclip.copy(self.IP4)
        self.master = master
        self.pack()
        self.create_widgets(self.IP4, self.IP6)

    def create_widgets(self, ip4, ip6):
        # Margin
        w = tk.Canvas(self, width=200, height=50)
        w.grid(row=0)

        # IPv4 textfield
        self.IPv4Text = tk.Label(self, text="IPv4: " + ip4)
        self.IPv4Text.grid(row=1, column=0, pady="5", padx="5", sticky="W")

        # IPv6 textfield
        self.IPv6Text = tk.Label(self, text="IPv6: " + ip6)
        self.IPv6Text.grid(row=2, pady="5", padx="5", sticky="W")

        # Info textfield
        self.infoText = tk.Label(self, text="IPv4 copied to clipboard")
        self.infoText.grid(row=3, pady="10")

        # "Copy IPv4" button
        self.copyIPv4 = tk.Button(self)
        self.copyIPv4["text"] = "Copy"
        self.copyIPv4["command"] = lambda: pyperclip.copy(ip4)
        self.copyIPv4.grid(row=1, column=1, sticky="W")

        # "Copy IPv6" button
        self.copyIPv6 = tk.Button(self)
        self.copyIPv6["text"] = "Copy"
        self.copyIPv6["command"] = lambda: pyperclip.copy(ip6)
        self.copyIPv6.grid(row=2, column=1, sticky="W")

        # Quit button
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=4, pady="10")

    def getIP(self, v):
        ip = "No connection"
        if v == 4:
            res = IPv4
            if res.status_code == 200:
                ip = res.json()['ip']
        if v == 6:
            res = IPv6
            if res.status_code == 200:
                ip = res.json()['ip']
        return str(ip)


windowWidth = 500
windowHeight = 300

root = tk.Tk()
root.geometry("%dx%d+400+400" % (windowWidth, windowHeight))

app = Application(master=root)
app.master.title("What's my IP")
app.mainloop()
