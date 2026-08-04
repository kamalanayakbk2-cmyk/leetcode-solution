class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if only 1 row or string length is less than numRows, no conversion needed
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list of empty strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False

        # Iterate through characters and place them in the correct row
        for char in s:
            rows[current_row] += char
            
            # Reverse direction when reaching top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            # Move to the next row depending on direction
            current_row += 1 if going_down else -1

        # Join all rows to form the final result
        return ''.join(rows)