import sys


class Screen:
    def __init__(self, width: int = 40, height: int = 40):
        self.width = (width * 3) + 4
        self.height = (height * 2) + 4
        self.buffer = [[' ' for _ in range(width)] for _ in range(height)]

    def clear(self):
        self.buffer = [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def set(self, x, y, char):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.buffer[y][x] = char
        else:
            raise Exception(
                f'Arguments dose not match screen configuration. X: {x}, Y: {y} should be in range ({self.width}, {self.height}) ')

    def set_line(self, y: int, line: str):
        if 0 <= y < self.height:
            self.buffer[y] = list(line)

    def update(self):
        sys.stdout.write("\033[2J")
        sys.stdout.write("\033[H")

        for row in self.buffer:
            sys.stdout.write(''.join(row) + "\n")

        sys.stdout.flush()
