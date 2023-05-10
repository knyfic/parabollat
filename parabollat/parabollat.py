import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import matplotlib.pyplot as plt
import numpy as np

def draw_parabola(a, b, c, x):
    y = a * (x**2) + b * x + c
    return y

class ParabolaApp(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Parabola Graph")
        self.set_default_size(350, 300)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        num_graphs_label = Gtk.Label(label="How many graphs do you want to draw?")
        vbox.pack_start(num_graphs_label, False, False, 0)

        self.num_graphs_entry = Gtk.Entry()
        vbox.pack_start(self.num_graphs_entry, False, False, 0)

        button = Gtk.Button(label="Draw graph")
        button.connect("clicked", self.on_button_clicked)
        vbox.pack_start(button, False, False, 0)

        self.connect("delete-event", Gtk.main_quit)

    def on_button_clicked(self, button):
        num_graphs = int(self.num_graphs_entry.get_text())

        dialog = Gtk.Dialog(title="Parabola Values", parent=self, buttons=(Gtk.STOCK_OK, Gtk.ResponseType.OK))
        grid = Gtk.Grid(column_homogeneous=True, row_homogeneous=True, column_spacing=10, row_spacing=10)
        dialog.vbox.add(grid)

        entry_a_list = []
        entry_b_list = []
        entry_c_list = []

        for i in range(num_graphs):
            label_a = Gtk.Label(label=f"{i+1}. a value for the graph:")
            entry_a = Gtk.Entry()
            label_b = Gtk.Label(label=f"{i+1}. b value for the graph:")
            entry_b = Gtk.Entry()
            label_c = Gtk.Label(label=f"{i+1}. c value for the graph:")
            entry_c = Gtk.Entry()

            entry_a_list.append(entry_a)
            entry_b_list.append(entry_b)
            entry_c_list.append(entry_c)

            grid.attach(label_a, 0, i, 1, 1)
            grid.attach(entry_a, 1, i, 1, 1)
            grid.attach(label_b, 2, i, 1, 1)
            grid.attach(entry_b, 3, i, 1, 1)
            grid.attach(label_c, 4, i, 1, 1)
            grid.attach(entry_c, 5, i, 1, 1)

        dialog.show_all()
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            graphs = []

            for i in range(num_graphs):
                a = float(entry_a_list[i].get_text())
                b = float(entry_b_list[i].get_text())
                c = float(entry_c_list[i].get_text())
                graphs.append((a, b, c))

            self.draw_graphs(graphs)

        dialog.destroy()

    def draw_graphs(self, graphs):
        x = np.linspace(-10, 10, 100)

        plt.figure()

        for i, (a, b, c) in enumerate(graphs):
            y = draw_parabola(a, b, c, x)
            plt.plot(x, y, label=f'Parabola {i+1}')

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'{len(graphs)} Parabola graph')
        plt.legend()
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    app = ParabolaApp()
    app.show_all()
    Gtk.main()
