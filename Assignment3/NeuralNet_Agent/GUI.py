# Import tkinter and agent.py
from tkinter import *
from agent import *
from places import *
from directions import *

# botname specified
bot_name = "Steven"

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


class ChatApplication:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        self.agent = Agent()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Chatbot")
        self.window.resizable(width=True, height=True)
        self.window.configure(width=1000, height=600, bg=BG_COLOR)

        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # text widget
        self.text_widget = Text(self.window, width=30, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=0, pady=0)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(state=NORMAL)
        intro_msg = "Welcome, we are here to help you with your computer issues. Please type \"Hello\" or the type " \
                    "of issue you are having, to begin.\nPlease use the \"Search Place\" button if you wish to find address of a place of interest nearby." \
                    "\nTo get directions from City A to City B, fill out Origin, Destination and Mode then press Get Directions. \n\n"
        self.text_widget.insert(END, intro_msg)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.configure(command=self.text_widget.yview)

        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        #directions entry section
        #origin
        self.direction_origin = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        labelText_Org=StringVar()
        labelText_Org.set("Origin:")
        labelDir_Org=Label(bottom_label, textvariable=labelText_Org, height=4, bg=BG_GRAY, font=FONT)
        labelDir_Org.place(relwidth=0.04, relheight=0.03, rely=0.08, relx=0)
        self.direction_origin.place(relwidth=0.12, relheight=0.03, rely=0.08, relx=0.04)
        self.direction_origin.insert(0, 'City A')
        #destination
        self.direction_dest = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        labelText_Dest=StringVar()
        labelText_Dest.set("Destination:")
        labelDir_Dest=Label(bottom_label, textvariable=labelText_Dest, height=4, bg=BG_GRAY, font=FONT)
        labelDir_Dest.place(relwidth=0.07, relheight=0.03, rely=0.08, relx=0.16)
        self.direction_dest.place(relwidth=0.12, relheight=0.03, rely=0.08, relx=0.23)
        self.direction_dest.insert(0, 'City B')
        #mode - optional field list
        self.variable = StringVar()
        self.variable.set("") # default value
        self.direction_mode = OptionMenu(bottom_label, self.variable, "driving", "walking", "bicycling", "transit")
        labelText_Mode=StringVar()
        labelText_Mode.set("Mode(Optional):")
        labelDir_Mode=Label(bottom_label, textvariable=labelText_Mode, height=4, bg=BG_GRAY, font=FONT)
        labelDir_Mode.place(relwidth=0.1, relheight=0.03, rely=0.08, relx=0.5)
        self.direction_mode.place(relwidth=0.12, relheight=0.03, rely=0.08, relx=0.6)

        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

        #search place button
        search_button = Button(bottom_label, text="Search Place", font=FONT_BOLD, width=10, bg="Green",
                                command=lambda: self._on_enter_search(None))
        search_button.place(relx=0.77, rely=0.08, relheight=0.03, relwidth=0.11)

        #get directions button
        directions_button = Button(bottom_label, text="Get Directions", font=FONT_BOLD, width=10, bg="Blue",
                                command=lambda: self._on_enter_direct(None))
        directions_button.place(relx=0.88, rely=0.08, relheight=0.03, relwidth=0.11)

    # on enter pressed function defined
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
    
    #on click search button
    def _on_enter_search(self, event):
        msg = self.msg_entry.get()
        self._insert_search(msg, "You")

    #on click get directions
    def _on_enter_direct(self, event):
        origin = self.direction_origin.get()
        dest = self.direction_dest.get()
        mode = self.variable.get()
        self._insert_directions(origin, dest, mode)

    #Google places API search through places.py
    def _insert_search(self, msg, sender):
        if not msg:
            return
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        botResponse = findPlace(msg)
        msg2 = f"{bot_name}: {botResponse}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)

    #Google Direction API through places.py
    def _insert_directions(self, origin, dest, mode):
        if origin == "City A" or dest == "City B":
            return
        self.direction_origin.delete(0, END)
        self.direction_dest.delete(0, END)
        sender = "You"
        direction_msg = "Origin: " + origin + ", Destination: " + dest + ", Mode: " + mode
        msg1 = f"{sender}: {direction_msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        botResponse = getDirections(origin, dest, mode)
        msg2 = f"{bot_name}: {botResponse}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)

    def _insert_message(self, msg, sender):
        if not msg:
            return  # if there is no text entered
        msg = self.agent.spellCheck(msg)
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        intentions = self.agent.predictResponse(msg)
        botResponse = self.agent.getResponse(intentions)
        msg2 = f"{bot_name}: {botResponse}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)


if __name__ == "__main__":
    app = ChatApplication()
    app.run()
