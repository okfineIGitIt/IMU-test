from tkinter import Tk, Canvas, Frame, BOTH

import numpy as np


class Canvas3D(Frame):
    def __init__(self):
        super().__init__()
        self.shape_dict = {}
        self.canvas = Canvas(self)
        self.initUI()

    def initUI(self):
        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)
        self.canvas.pack(fill=BOTH, expand=1)
        self.canvas.create_polygon()


class Square:
    def __init__(self, origin: list, side_length):
        super().__init__()
        self.origin = origin
        self.side_length = side_length

    def generate_square_pts(self, closed_coords=True):
        sl = self.side_length
        x, y = self.origin
        pt1 = [x, y]
        pt2 = [x + sl, y]
        pt3 = [x + sl, y + sl]
        pt4 = [x, y + sl]

        pt_list = [pt1, pt2, pt3, pt4]
        if closed_coords:
            pt_list.append(pt1)

        return pt_list


def rotate_point_around_origin(x_o, y_o, x, y, angle):
    origin = np.array([x_o, y_o])
    pt = np.array([x, y])
    v = pt - origin

    angle = np.radians(angle)
    R = np.array([[np.cos(angle), -1 * np.sin(angle)], [np.sin(angle), np.cos(angle)]])

    v_p = np.matmul(v, R)
    v_p = v_p + origin
    v_p = np.around(v_p, 2)
    return v_p


def main():
    root = Tk()
    ex = Canvas3D()

    square = Square(origin=[5, 5], side_length=100)
    square_coords = square.generate_square_pts()
    for i in range(len(square_coords) - 1):
        start_pt = square_coords[i]
        end_pt = square_coords[i + 1]
        ex.canvas.create_line(
            start_pt[0], start_pt[1], end_pt[0], end_pt[1], tags=f"{i}"
        )

    root.geometry("400x250+300+300")
    root.mainloop()


if __name__ == "__main__":
    # res = rotate_point_around_origin(21, 6, 21, 7, -90)
    # print(res)
    main()
