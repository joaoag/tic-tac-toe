class Board:
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

    xy_divider = "-----|-----|-----"
