from svglib.svglib import svg2rlg

def round_bounds(drawing):
     left, bottom, right, top = drawing.getBounds()
     return round(left, 1), round(bottom, 1), round(right, 1), round(top, 1)

def get_metadata_for_svg(file_obj, drawing=None):
    try:
        drawing = svg2rlg(file_obj.file)
    except Exception:
        _width, _height , _bounds = None, None, None
    if drawing:
        _width, _height = drawing.width, drawing.height
        _bounds = round_bounds(drawing)
    return  _width, _height, _bounds
