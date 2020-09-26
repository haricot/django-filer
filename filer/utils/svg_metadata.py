from svglib.svglib import svg2rlg


def get_metadata_for_svg(file_obj):
    try:
        drawing = svg2rlg(file_obj.file)
        _width, _height = drawing.width, drawing.height
        _bounds = [left, bottom, right, top] =  drawing.getBounds()
    except Exception:
        _width, _height, _bounds = None, None, None
    return  _width, _height, _bounds
