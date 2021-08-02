"""Model to manage graph data"""


class GraphModel:
    def __init__(self):
        self.graph_data = {}

    @property
    def data_groups(self):
        return self.graph_data.keys()

    @property
    def all_data(self):
        return self.graph_data

    def add_data_point(self, x, y, name: str):
        """Add data point to graph data.

        :param x: x-coordinate
        :param y: y-coordinate
        :param name: name for data group
        """

        if name not in self.graph_data:
            self.graph_data[name] = {
                "x": [],
                "y": [],
            }

        self.graph_data[name]["x"].append(x)
        self.graph_data[name]["y"].append(y)

    def get_group_data(self, name):
        """Get the plot data for a given group.

        :param name: name of group to get data from
        :return: data dictionary associated with group
        """
        if name not in self.graph_data.keys():
            return None

        return self.graph_data[name]

    def clear_data(self):
        """Clear graph data."""
        self.graph_data = {}
