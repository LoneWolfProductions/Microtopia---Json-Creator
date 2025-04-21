def cleanup_data(raw_sheet_rows):
    """
    Cleans and reshapes raw sheet rows to a list of dictionaries with headers.
    - Remove blank rows
    - Transpose
    - Remove blank rows again
    - Transpose back
    - Trim whitespace
    - Promote headers
    """
    if not raw_sheet_rows or not any(isinstance(row, list) and row for row in raw_sheet_rows):
        return []

    rows = [row for row in raw_sheet_rows if any(cell.strip() for cell in row if cell)]

    if not rows:
        return []

    max_len = max((len(row) for row in rows), default=0)
    if max_len == 0:
        return []

    padded = [row + [''] * (max_len - len(row)) for row in rows]
    rows = list(map(list, zip(*padded)))

    rows = [row for row in rows if any(cell.strip() for cell in row if cell)]

    if not rows:
        return []

    max_len = max((len(row) for row in rows), default=0)
    if max_len == 0:
        return []

    padded = [row + [''] * (max_len - len(row)) for row in rows]
    rows = list(map(list, zip(*padded)))

    rows = [
        [cell.strip() if isinstance(cell, str) else cell for cell in row]
        for row in rows
    ]

    if not rows or len(rows) < 2:
        return []

    headers = rows[0]
    data_rows = rows[1:]

    return [
        dict(zip(headers, row))
        for row in data_rows
        if len(row) == len(headers)
    ]
