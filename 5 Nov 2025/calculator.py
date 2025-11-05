def calculator_area(width,height):
    if width < 0 or height < 0:
        raise ValueError("Width and Height cannot be negative")
    return width * height