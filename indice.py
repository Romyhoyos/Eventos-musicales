from tkinter import tk
from tkinter import *
from tkinter import tkintermapview
from tkinter import mapview
import json


class ListaDeEventosApp(tk,Tk):
    def _init_(self):
        super()._init_()
        self.title("Tour Musical")
        self.geometry("800,600")

        self.events = self.load_events()
        self.filtered_events = self.events

        self.create_widgets()

    def create_widgets(self):
        self.event_listbox = tk.Listbox(self)
        self.event_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.event_listbox.bind("<<ListboxSelect>>", self.show_event_details)
        self.event_details_label = tk.Label(self, text="Detalles del evento")
        self.event_details_label.pack()

        self.map_view = mapview(self, width=400, height=400)
        self.map_view.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.load_event_list()

    def load_events(self):
        with open("eventos.json") as f:
            return json.load(f)

    def load_event_list(self):
        self.event_listbox.delete(0, tk.END)
        for event in self.filtered_events:
            self.event_listbox.insert(tk.END, event["nombre"])

    def show_event_details(self, event):
        selected_index = self.event_listbox.curselection()
        if selected_index:
            selected_event = self.filtered_events[selected_index[0]]
            self.event_details_label.config(text=f"Nombre: {selected_event['nombre']}\nArtista: {selected_event['artista']}\nGénero: {selected_event['genero']}\nUbicación: {selected_event['ubicacion']}")
            self.map_view.show_location(selected_event["ubicacion"])

app = ListaDeEventosApp()
app.mainloop()