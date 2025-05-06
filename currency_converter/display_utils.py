def print_table(headers, rows):
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    # Print header
    header_row = " | ".join([str(headers[i]).ljust(col_widths[i]) for i in range(len(headers))])
    print(header_row)
    print("-+-".join(["-" * w for w in col_widths]))

    # Print rows
    for row in rows:
        row_str = " | ".join([str(row[i]).ljust(col_widths[i]) for i in range(len(row))])
        print(row_str)
