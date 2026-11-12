
import tkinter as tk
from tkinter import messagebox, ttk
from collections import deque


class PrinterQueue:

    def __init__(self, root):
        self.root = root
        self.root.title("3D-Drucker Warteschlange")
        self.root.geometry("950x580")
        self.root.minsize(750, 450)
        self.root.configure(bg="#F1F5F9")

        self.my_queue = deque()
        self.timer_id = None
        self.current_task = None

        # Farben
        self.bg_color = "#F1F5F9"
        self.primary = "#2563EB"
        self.dark = "#172554"
        self.text_color = "#1E293B"

        # Tabellen-Design
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Treeview",
            background="white",
            foreground=self.text_color,
            rowheight=42,
            fieldbackground="white",
            font=("Arial", 10),
            borderwidth=0
        )

        style.configure(
            "Treeview.Heading",
            background="#E2E8F0",
            foreground="#334155",
            font=("Arial", 10, "bold"),
            relief="flat",
            padding=12
        )

        style.map(
            "Treeview",
            background=[("selected", "#DBEAFE")],
            foreground=[("selected", "#1E40AF")]
        )

        self.create_ui()

    # ---------------------------------
    # OBERFLÄCHE
    # ---------------------------------

    def create_ui(self):

        # HEADER
        header = tk.Frame(
            self.root,
            bg=self.dark,
            height=130
        )
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text="3D-Drucker Warteschlange",
            font=("Arial", 22, "bold"),
            bg=self.dark,
            fg="white"
        ).pack(anchor="w", padx=30, pady=(25, 5))

        tk.Label(
            header,
            text="Verwalte deine Druckaufträge ganz einfach.",
            font=("Arial", 11),
            bg=self.dark,
            fg="#BFDBFE"
        ).pack(anchor="w", padx=32)

        # HAUPTBEREICH
        main = tk.Frame(
            self.root,
            bg=self.bg_color
        )
        main.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=20
        )

        # OBERE LEISTE
        top = tk.Frame(main, bg=self.bg_color)
        top.pack(fill="x", pady=(0, 15))

        tk.Label(
            top,
            text="Deine Aufträge",
            font=("Arial", 16, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        ).pack(side="left")

        # HINZUFÜGEN BUTTON
        add_button = tk.Button(
            top,
            text="+  Auftrag hinzufügen",
            command=self.add_task,
            bg=self.primary,
            fg="white",
            activebackground="#1D4ED8",
            activeforeground="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            bd=0,
            padx=18,
            pady=11,
            cursor="hand2"
        )

        add_button.pack(side="right", padx=(10, 0))

        # PAPIERKORB BUTTON
        # Schwarzes Papierkorb-Symbol auf hellem Hintergrund
        self.delete_button = tk.Canvas(
            top,
            width=46,
            height=40,
            bg="#FEE2E2",
            highlightthickness=0,
            cursor="hand2"
        )

        self.delete_button.pack(side="right")

        # Papierkorb zeichnen
        self.delete_button.create_arc(
            17, 5, 29, 15,
            start=0,
            extent=180,
            style="arc",
            outline="black",
            width=3
        )

        self.delete_button.create_line(
            11, 15, 35, 15,
            fill="black",
            width=3
        )

        self.delete_button.create_polygon(
            13, 18,
            33, 18,
            30, 35,
            16, 35,
            fill="black",
            outline="black"
        )

        # Drei helle Streifen im Papierkorb
        for x in [19, 23, 27]:
            self.delete_button.create_line(
                x, 21, x, 32,
                fill="#FEE2E2",
                width=2
            )

        self.delete_button.bind(
            "<Button-1>",
            lambda event: self.delete_task()
        )

        # HOVER-EFFEKT
        self.delete_button.bind(
            "<Enter>",
            lambda event: self.delete_button.config(
                bg="#FECACA"
            )
        )

        self.delete_button.bind(
            "<Leave>",
            lambda event: self.delete_button.config(
                bg="#FEE2E2"
            )
        )

        # TABELLE
        table_card = tk.Frame(
            main,
            bg="white",
            highlightbackground="#E2E8F0",
            highlightthickness=1
        )

        table_card.pack(fill="both", expand=True)

        columns = (
            "number",
            "task",
            "name",
            "duration",
            "status"
        )

        self.task_list = ttk.Treeview(
            table_card,
            columns=columns,
            show="headings",
            selectmode="browse"
        )

        self.task_list.heading("number", text="NR.")
        self.task_list.heading("task", text="AUFTRAGSNAME")
        self.task_list.heading("name", text="KUNDE")
        self.task_list.heading("duration", text="DAUER (SEK.)")
        self.task_list.heading("status", text="STATUS")

        self.task_list.column(
            "number", width=55, anchor="center"
        )

        self.task_list.column(
            "task", width=250, anchor="w"
        )

        self.task_list.column(
            "name", width=180, anchor="w"
        )

        self.task_list.column(
            "duration", width=120, anchor="center"
        )

        self.task_list.column(
            "status", width=180, anchor="center"
        )

        # STATUSFARBEN
        self.task_list.tag_configure(
            "active",
            foreground="#15803D",
            background="#F0FDF4"
        )

        self.task_list.tag_configure(
            "waiting",
            foreground="#B45309",
            background="white"
        )

        self.task_list.tag_configure(
            "alternate",
            foreground="#B45309",
            background="#F8FAFC"
        )

        scrollbar = ttk.Scrollbar(
            table_card,
            orient="vertical",
            command=self.task_list.yview
        )

        self.task_list.configure(
            yscrollcommand=scrollbar.set
        )

        self.task_list.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(10, 0),
            pady=10
        )

        scrollbar.pack(
            side="right",
            fill="y",
            pady=10,
            padx=(0, 10)
        )

        # FOOTER
        footer = tk.Frame(
            main,
            bg=self.bg_color
        )

        footer.pack(
            fill="x",
            pady=(12, 0)
        )

        self.info_label = tk.Label(
            footer,
            text="0 Aufträge in der Warteschlange",
            font=("Arial", 9),
            bg=self.bg_color,
            fg="#64748B"
        )

        self.info_label.pack(side="left")

        tk.Label(
            footer,
            text="3D PRINT MANAGER",
            font=("Arial", 9, "bold"),
            bg=self.bg_color,
            fg="#94A3B8"
        ).pack(side="right")

        self.update_list()

    # ---------------------------------
    # AUFTRAG HINZUFÜGEN
    # ---------------------------------

    def add_task(self):

        popup = tk.Toplevel(self.root)
        popup.title("Neuer Auftrag")
        popup.geometry("400x430")
        popup.configure(bg="white")
        popup.resizable(False, False)
        popup.transient(self.root)
        popup.grab_set()

        tk.Label(
            popup,
            text="Neuen Auftrag erstellen",
            font=("Arial", 17, "bold"),
            bg="white",
            fg=self.dark
        ).pack(pady=(25, 5))

        tk.Label(
            popup,
            text="Trage hier deine Druckinformationen ein.",
            font=("Arial", 9),
            bg="white",
            fg="#64748B"
        ).pack(pady=(0, 20))

        def create_field(label):

            tk.Label(
                popup,
                text=label,
                font=("Arial", 10, "bold"),
                bg="white",
                fg=self.text_color
            ).pack(
                anchor="w",
                padx=40,
                pady=(10, 5)
            )

            entry = tk.Entry(
                popup,
                font=("Arial", 11),
                bg="#F8FAFC",
                fg=self.text_color,
                relief="flat",
                highlightthickness=1,
                highlightbackground="#CBD5E1",
                highlightcolor=self.primary
            )

            entry.pack(
                fill="x",
                padx=40,
                ipady=9
            )

            return entry

        name_entry = create_field("Dein Name")
        task_entry = create_field("Name des Auftrags")
        duration_entry = create_field(
            "Druckdauer in Sekunden"
        )

        def save_task():

            name = name_entry.get().strip()
            task = task_entry.get().strip()
            duration = duration_entry.get().strip()

            if not name or not task or not duration:

                messagebox.showwarning(
                    "Fehler",
                    "Bitte alle Felder ausfüllen!",
                    parent=popup
                )

                return

            try:

                duration = float(
                    duration.replace(",", ".")
                )

                if duration <= 0:
                    raise ValueError

            except ValueError:

                messagebox.showwarning(
                    "Fehler",
                    "Bitte eine gültige Druckdauer eingeben!",
                    parent=popup
                )

                return

            new_task = {
                "name": name,
                "task": task,
                "duration": duration
            }

            self.my_queue.append(new_task)

            popup.destroy()

            self.update_list()

            if self.current_task is None:
                self.start_next_task()

        tk.Button(
            popup,
            text="Auftrag speichern",
            command=save_task,
            bg=self.primary,
            fg="white",
            activebackground="#1D4ED8",
            activeforeground="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            bd=0,
            cursor="hand2"
        ).pack(
            fill="x",
            padx=40,
            pady=25,
            ipady=10
        )

    # ---------------------------------
    # AUFTRAG LÖSCHEN
    # ---------------------------------

    def delete_task(self):

        selected = self.task_list.selection()

        # Prüfen, ob ein Auftrag ausgewählt wurde
        if not selected:

            messagebox.showwarning(
                "Kein Auftrag ausgewählt",
                "Bitte wähle zuerst einen Auftrag aus!",
                parent=self.root
            )

            return

        # Ausgewählte Tabellenzeile auslesen
        item = self.task_list.item(selected[0])
        values = item["values"]

        index = int(values[0]) - 1

        if index < 0 or index >= len(self.my_queue):
            return

        task = self.my_queue[index]

        # Sicherheitsabfrage
        answer = messagebox.askyesno(
            "Auftrag löschen",
            f"Möchtest du den Auftrag "
            f"'{task['task']}' wirklich löschen?",
            parent=self.root
        )

        if not answer:
            return

        # Wenn der laufende Auftrag gelöscht wird
        if index == 0 and self.current_task is not None:

            # Timer abbrechen
            if self.timer_id is not None:

                self.root.after_cancel(
                    self.timer_id
                )

                self.timer_id = None

            self.current_task = None

        # Auftrag aus der Warteschlange entfernen
        del self.my_queue[index]

        # Tabelle aktualisieren
        self.update_list()

        # Falls nötig nächsten Auftrag starten
        if self.current_task is None:
            self.start_next_task()

    # ---------------------------------
    # NÄCHSTEN AUFTRAG STARTEN
    # ---------------------------------

    def start_next_task(self):

        if not self.my_queue:

            self.current_task = None
            self.update_list()

            return

        self.current_task = self.my_queue[0]

        self.update_list()

        # Sekunden in Millisekunden umrechnen
        duration_ms = int(
            self.current_task["duration"] * 1000
        )

        self.timer_id = self.root.after(
            duration_ms,
            self.timer_finished
        )

    # ---------------------------------
    # TIMER BEENDET
    # ---------------------------------

    def timer_finished(self):

        self.timer_id = None

        if self.current_task is None:
            return

        answer = messagebox.askyesno(
            "Druck abgeschlossen?",
            f"Ist '{self.current_task['task']}' "
            f"fertig gedruckt?",
            parent=self.root
        )

        if answer:

            self.my_queue.popleft()

            self.current_task = None

            self.update_list()

            self.start_next_task()

        else:

            # Bei Nein wird die Dauer erneut gewartet
            duration_ms = int(
                self.current_task["duration"] * 1000
            )

            self.timer_id = self.root.after(
                duration_ms,
                self.timer_finished
            )

    # ---------------------------------
    # TABELLE AKTUALISIEREN
    # ---------------------------------

    def update_list(self):

        # Alte Zeilen entfernen
        for item in self.task_list.get_children():

            self.task_list.delete(item)

        # Warteschlange neu eintragen
        for index, task in enumerate(
            self.my_queue,
            start=1
        ):

            if index == 1:

                status = "●  In Bearbeitung"
                tag = "active"

            else:

                status = "●  Wartet"

                if index % 2 == 0:
                    tag = "waiting"
                else:
                    tag = "alternate"

            self.task_list.insert(
                "",
                tk.END,
                values=(
                    index,
                    task["task"],
                    task["name"],
                    f"{task['duration']:g}",
                    status
                ),
                tags=(tag,)
            )

        # Anzahl aktualisieren
        count = len(self.my_queue)

        self.info_label.config(
            text=f"{count} Aufträge in der Warteschlange"
        )


# ---------------------------------
# PROGRAMM STARTEN
# ---------------------------------

root = tk.Tk()

app = PrinterQueue(root)

root.mainloop()
