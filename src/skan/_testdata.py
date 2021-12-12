import numpy as np


tinycycle = np.array([[0, 1, 0],
                      [1, 0, 1],
                      [0, 1, 0]], dtype=bool)


tinyline = np.array([0, 1, 1, 1, 0], dtype=bool)


skeleton0 = np.array([[0, 0, 0, 1, 0, 0, 0],
                      [0, 0, 0, 1, 0, 0, 0],
                      [0, 0, 0, 1, 0, 0, 0],
                      [1, 1, 1, 1, 1, 1, 1]], dtype=bool)


skeleton1 = np.array([[0, 1, 1, 1, 1, 1, 0],
                      [1, 0, 0, 0, 0, 0, 1],
                      [0, 1, 1, 0, 1, 1, 0],
                      [1, 0, 0, 1, 0, 0, 0],
                      [1, 0, 0, 0, 1, 1, 1]], dtype=bool)


_zeros1 = np.zeros_like(skeleton1)
skeleton2 = np.column_stack((skeleton1, _zeros1))
skeleton2 = np.row_stack((skeleton2, skeleton2[:, ::-1]))

skeleton3d = np.array([[[1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0]],
                       [[0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 1],
                        [0, 0, 0, 0, 1],
                        [0, 0, 1, 0, 1],
                        [1, 1, 0, 1, 0]],
                       [[0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0]],
                       [[0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0]],
                       [[0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 1],
                        [1, 0, 1, 0, 1],
                        [0, 0, 0, 0, 1]]], dtype=bool)

topograph1d = np.array([3., 2., 3.])

skeleton4 = np.array([[1, 0, 0, 0, 0],
                      [0, 1, 1, 1, 1],
                      [0, 1, 0, 0, 0],
                      [0, 1, 0, 0, 0]], dtype=bool)

junction_first = np.array([[0, 1, 1, 1, 1],
                           [1, 1, 0, 0, 0],
                           [1, 0, 1, 0, 0],
                           [1, 0, 0, 1, 0],
                           [1, 0, 0, 0, 1]], dtype=bool)