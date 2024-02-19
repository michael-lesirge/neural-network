import numpy as np

MAX_ROTATIONS = 4

ALL_SHAPES: list["TetrominoBlockShape"] = []
COLOR_MAP: dict[int, str | tuple[int, int, int]] = {}


class TetrominoBlockShape:

    def __init__(self, name: str, color: tuple[int, int, int] | str, shape: list[list[int]] | np.ndarray, rotator = np.rot90) -> None:

        self.name = name
        self.id = len(ALL_SHAPES) + 1

        ALL_SHAPES.append(self)
        COLOR_MAP[self.id] = color

        shape = np.array(shape, dtype=np.uint8)

        self.rotations: list[np.ndarray] = []
        for i in range(MAX_ROTATIONS):
            self.rotations.append(shape)
            shape = rotator(shape)
            if np.array_equal(shape, self.rotations[0]):
                break

    def get_name(self) -> str: return self.name

    def get_color(self) -> str: return COLOR_MAP[self.id]

    def get_id(self) -> str: return self.id

    def get_num_of_rotations(self) -> int: return len(self.rotations)
    
    def get_largest_dimension(self) -> int: return max(self.rotations[0].shape)


TetrominoBlockShape("I", (0, 240, 240), [
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]),

TetrominoBlockShape("O", (240, 240, 0), [
    [1, 1],
    [1, 1],
]),

TetrominoBlockShape("L", (240, 160, 0), [
    [1, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
]),

TetrominoBlockShape("J", (0, 0, 240), [
    [0, 1, 1],
    [0, 1, 0],
    [0, 1, 0],
]),

TetrominoBlockShape("T", (160, 0, 240), [
    [0, 1, 0],
    [1, 1, 1],
    [0, 0, 0],
]),

TetrominoBlockShape("Z", (240, 0, 0), [
    [0, 0, 0],
    [1, 1, 0],
    [0, 1, 1],
]),

TetrominoBlockShape("S", (0, 240, 0), [
    [0, 0, 0],
    [0, 1, 1],
    [1, 1, 0],
]),


def main() -> None:
    states = [" .", "██"]

    for shape in ALL_SHAPES:
        print(shape.name + ": ")
        for i, orientations in enumerate(shape.rotations):
            print()
            print("\n".join(
                "".join(states[value] for value in row) for row in orientations
            ))
        print()


if __name__ == "__main__":
    main()
