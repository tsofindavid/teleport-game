from random import randint, choice
from string import ascii_uppercase, ascii_lowercase
from typing import List

from classes.teleport import Teleport, TeleportType


class TeleportsGenerator:
    _count = None
    _max_point = None
    _exist_points = set()
    _exist_labels = set()

    def __init__(self, count: int, max_point: int) -> None:
        self._count = count
        self._max_point = max_point

    def _generate_teleport_point(self) -> int:
        point = randint(1, self._max_point - 1)

        if point in self._exist_points:
            return self._generate_teleport_point()

        self._exist_points.add(point)

        return point

    def _generate_teleport_label(self, upper_case: bool) -> str:
        if upper_case:
            label = choice(ascii_uppercase)
        else:
            label = choice(ascii_lowercase)

        if label in self._exist_labels:
            return self._generate_teleport_label(upper_case)

        self._exist_labels.add(label)

        return label

    def _generate_teleport(self, type: TeleportType) -> Teleport:

        points = [
            self._generate_teleport_point(),
            self._generate_teleport_point(),
        ]

        label = None

        if type == TeleportType.RED:
            label = self._generate_teleport_label(False)
            points.sort(reverse=True)

        if type == TeleportType.GREEN:
            label = self._generate_teleport_label(True)
            points.sort(reverse=False)

        return Teleport(type, label, points[0], points[1])

    def generate(self) -> List[Teleport]:
        teleports = []

        for _ in range(self._count):
            teleports.append(self._generate_teleport(TeleportType.RED))
            teleports.append(self._generate_teleport(TeleportType.GREEN))

        return teleports
