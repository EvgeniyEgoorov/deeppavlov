import random
from typing import List


class KnightsTour:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.board = [[None] * h for i in range(w)]
        self.knight_tour = []

    def is_valid(self, pos: list, passed=False) -> bool:
        if not passed:
            return (
                    0 <= pos[0] < self.w
                    and 0 <= pos[1] < self.h
                    and self.board[pos[0]][pos[1]] is None
            )
        else:
            return 0 <= pos[0] < self.w and 0 <= pos[1] < self.h

    def possible_moves(self, pos: list) -> list:
        result = []
        moves = [[2, 1], [2, -1], [1, 2], [1, -2], [-2, 1], [-2, -1], [-1, 2], [-1, -2]]
        for move in moves:
            new_pos = [pos[0] + move[0], pos[1] + move[1]]
            if self.is_valid(new_pos):
                result.append(new_pos)
        if not result:
            for move in random.sample(moves, len(moves)):
                new_pos = [pos[0] + move[0], pos[1] + move[1]]
                if self.is_valid(new_pos, passed=True):
                    return [new_pos]
        return result

    def next_move(self, pos: list) -> list:
        result = None
        min_weight = 8  # the max number of options for the knight's next move
        neighbours = self.possible_moves(pos)
        for neighbour in neighbours:
            curr_weight = len(self.possible_moves(neighbour))
            if curr_weight < min_weight:
                result = neighbour
                min_weight = curr_weight
        return result

    def calculate_route(self, start_pos: list) -> list:
        move_counter = 0
        unique_cells = 0
        curr_pos = start_pos

        while unique_cells < self.w * self.h:
            self.knight_tour.append(curr_pos)
            if self.board[curr_pos[0]][curr_pos[1]] is None:
                unique_cells += 1
            self.board[curr_pos[0]][curr_pos[1]] = move_counter
            curr_pos = self.next_move(curr_pos)
            move_counter += 1


def main(desk_size: list) -> list:
    w = desk_size[0]
    h = desk_size[1]
    start_pos = [0, 0]
    kt = KnightsTour(w, h)
    kt.calculate_route(start_pos)
    return kt.knight_tour
