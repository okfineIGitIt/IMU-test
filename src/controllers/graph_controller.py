"""Controller for graph view and model"""
import pickle

from src.models.graph_model import GraphModel
from src.views.graph_view import GraphFrame


class GraphController:
    def __init__(self, frame, window):
        self._view = GraphFrame(frame, window)
        self._model = GraphModel()

        self.connect_ui_elements()

    def connect_ui_elements(self):
        self._view.save_button["command"] = self.save_graph_data

    def add_data_point(self, x, y, line_name: str):
        """Add data point to line

        :param x: x-coordinate
        :param y: y-coordinate
        :param line_name: name of line to add to
        :return:
        """
        self._model.add_data_point(x, y, line_name)
        self._view.add_data_point_to_plot(x, y, line_name)

    def clear_graph(self):
        """Clear data from graph"""
        self._view.clear_plot()
        self._model.clear_data()  # TODO: give option to save before clearing

    def save_graph_data(self):
        """Save all current data plotted on the graph"""
        with open("../tests/test_data.pickle", "wb") as fp:
            pickle.dump(self._model.graph_data, fp)
