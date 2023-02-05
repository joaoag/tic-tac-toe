class Board:
    xy_divider = "-----|-----|-----"

    def __init__(self):
        self.cells = {
            1: " ",
            2: " ",
            3: " ",
            4: " ",
            5: " ",
            6: " ",
            7: " ",
            8: " ",
            9: " ",
        }

    def update_board(self, character: str, position: int):
        self.cells[position] = character

    def get_board(self) -> str:
        board = f"""
  {self.cells[1]}  |  {self.cells[2]}  |  {self.cells[3]}  
{self.xy_divider}
  {self.cells[4]}  |  {self.cells[5]}  |  {self.cells[6]}  
{self.xy_divider}
  {self.cells[7]}  |  {self.cells[8]}  |  {self.cells[9]}  
"""
        return board

    def get_cells(self, cells: tuple) -> set[str]:
        first, second, third = cells
        return {self.cells[first], self.cells[second], self.cells[third]}
