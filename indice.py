from tkinter import ttk
from tkinter import *
from tkinter import tkintermapview
from tkinter import mapview
import json


class ListaDeEventosApp(ttk,Tk):
    def _init_(self):
        super()._init_()
        self.title("Tour Musical") 
        self.geometry("800,600")

        self.events = self.load_events()
        self.filtered_events = self.events

        self.create_widgets()

    def create_widgets(self):
        self.event_listbox = ttk.Listbox(self)
        self.event_listbox.pack(side=ttk.LEFT, fill=ttk.BOTH, expand=True)
        self.event_listbox.bind("<<ListboxSelect>>", self.show_event_details)
        self.event_details_label = ttk.Label(self, text="Detalles del evento")
        self.event_details_label.pack()

        self.map_view = mapview(self, width=400, height=400)
        self.map_view.pack(side=ttk.RIGHT, fill=ttk.BOTH, expand=True)

        self.load_event_list()

    def load_events(self):
        with open("eventos.json") as f:
            return json.load(f)

    def load_event_list(self):
        self.event_listbox.delete(0, ttk.END)
        for event in self.filtered_events:
            self.event_listbox.insert(ttk.END, event["nombre"])

    def show_event_details(self, event):
        selected_index = self.event_listbox.curselection()
        if selected_index:
            selected_event = self.filtered_events[selected_index[0]]
            self.event_details_label.config(text=f"Nombre: {selected_event['nombre']}\nArtista: {selected_event['artista']}\nGénero: {selected_event['genero']}\nUbicación: {selected_event['ubicacion']}")
            self.map_view.show_location(selected_event["ubicacion"])
def create_widgets(self):
        self.event_listbox = ttk.Listbox(self)
        self.event_listbox.pack(side=ttk.LEFT, fill=ttk.BOTH, expand=True)
        self.event_listbox.bind("<<ListboxSelect>>", self.show_event_details)

        self.event_details_label = ttk.Label(self, text="Detalles del evento")
        self.event_details_label.pack()

        self.map_view = mapview(self, width=400, height=400)
        self.map_view.pack(side=ttk.RIGHT, fill=ttk.BOTH, expand=True)

        self.load_event_list()

        self.review_button = ttk.Button(self, text="Escribir Reseña", command=self.write_review)
        self.review_button.pack()

        self.history_button = ttk.Button(self, text="Historial de Eventos Asistidos", command=self.show_attended_events)
        self.history_button.pack()

        self.mood_label = ttk.Label(self, text="Estado de Ánimo del Comentario")
        self.mood_label.pack()

        self.positive_button = ttk.Button(self, text="😃", command=lambda: self.set_mood("positivo"))
        self.positive_button.pack(side=ttk.LEFT)

        self.negative_button = ttk.Button(self, text="😔", command=lambda: self.set_mood("negativo"))
        self.negative_button.pack(side=ttk.LEFT)

def load_events(self):
        with open("eventos.json") as f:
            return json.load(f)

def load_event_list(self):
        self.event_listbox.delete(0, ttk.END)
        for event in self.filtered_events:
            self.event_listbox.insert(ttk.END, event["nombre"])

def show_event_details(self, event):
        selected_index = self.event_listbox.curselection()
        if selected_index:
            selected_event = self.filtered_events[selected_index[0]]
            self.event_details_label.config(text=f"Nombre: {selected_event['nombre']}\nArtista: {selected_event['artista']}\nGénero: {selected_event['genero']}\nUbicación: {selected_event['ubicacion']}")
            self.map_view.show_location(selected_event["ubicacion"])

def write_review(self):
        selected_index = self.event_listbox.curselection()
        if selected_index:
            selected_event = self.filtered_events[selected_index[0]]
            review_window = ttk.Toplevel(self)
            review_window.title("Escribir Reseña")
            review_window.geometry("400x300")

            review_label = ttk.Label(review_window, text=f"Reseña para {selected_event['nombre']}")
            review_label.pack()

            review_text = ttk.Text(review_window)
            review_text.pack()

            submit_button = ttk.Button(review_window, text="Enviar", command=lambda: self.submit_review(selected_event, review_text.get("1.0", ttk.END)))
            submit_button.pack()

def submit_review(self, event, review):
        # Aquí puedes guardar la reseña y la calificación en tu base de datos
        print(f"Reseña enviada para {event['nombre']}: {review}")

def show_attended_events(self):
        # Aquí puedes mostrar el historial de eventos a los que ha asistido el usuario
        print("Historial de eventos asistidos")

def set_mood(self, mood):
        self.mood_label.config(text=f"Estado de Ánimo del Comentario: {mood}")
app = ListaDeEventosApp()
app.mainloop()
