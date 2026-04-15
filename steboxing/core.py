from typing import Dict, List, Tuple

_HORIZONTAL_CHARS = {
    "thin": "─",
    "bold": "━",
    "double": "═",
}

_VERTICAL_CHARS = {
    "thin": "│",
    "bold": "┃",
    "double": "║",
}

_CORNER_CHARS = {
    "top_left": {
        ("thin", "thin"): "┌",
        ("bold", "bold"): "┏",
        ("double", "double"): "╔",
        ("bold", "thin"): "┍",
        ("thin", "bold"): "┎",
        ("double", "thin"): "╒",
        ("thin", "double"): "╓",
    },
    "top_right": {
        ("thin", "thin"): "┐",
        ("bold", "bold"): "┓",
        ("double", "double"): "╗",
        ("bold", "thin"): "┑",
        ("thin", "bold"): "┒",
        ("double", "thin"): "╕",
        ("thin", "double"): "╖",
    },
    "bottom_left": {
        ("thin", "thin"): "└",
        ("bold", "bold"): "┗",
        ("double", "double"): "╚",
        ("bold", "thin"): "┕",
        ("thin", "bold"): "┖",
        ("double", "thin"): "╘",
        ("thin", "double"): "╙",
    },
    "bottom_right": {
        ("thin", "thin"): "┘",
        ("bold", "bold"): "┛",
        ("double", "double"): "╝",
        ("bold", "thin"): "┙",
        ("thin", "bold"): "┚",
        ("double", "thin"): "╛",
        ("thin", "double"): "╜",
    },
}

_ROUND_CORNERS = {
    "top_left": "╭",
    "top_right": "╮",
    "bottom_left": "╰",
    "bottom_right": "╯",
}

_SUPPORTED_BOX_TYPES = (
    "thin",
    "double",
    "bold",
    "round",
    "bold_top_and_bottom",
    "double_top_and_bottom",
    "bold_left_and_right",
    "double_left_and_right",
    "bold_top_only",
    "double_top_only",
    "bold_bottom_only",
    "double_bottom_only",
    "bold_right_only",
    "double_right_only",
    "bold_left_only",
    "double_left_only",
    "bold_left_and_top",
    "double_left_and_top",
    "bold_right_and_top",
    "double_right_and_top",
    "bold_right_and_bottom",
    "double_right_and_bottom",
    "bold_left_and_bottom",
    "double_left_and_bottom",
    "bold_but_bottom",
    "double_but_bottom",
    "bold_but_left",
    "double_but_left",
    "bold_but_top",
    "double_but_top",
    "bold_but_right",
    "double_but_right",
    "bold_corners_only",
    "double_corners_only",
    "bold_chain",
    "double_chain"
)


def _repeat_pattern(pattern: str, width: int) -> str:
    if width <= 0:
        return ""

    repeats = (width // len(pattern)) + 1
    return (pattern * repeats)[:width]


def _resolve_sides(box_type: str) -> Dict[str, str]:
    if box_type in {"thin", "round"}:
        return {"top": "thin", "right": "thin", "bottom": "thin", "left": "thin"}

    if box_type.startswith("bold"):
        variant = "bold"
    elif box_type.startswith("double"):
        variant = "double"
    else:
        raise ValueError(f"box_type not supported: {box_type}")

    if box_type == variant:
        return {"top": variant, "right": variant, "bottom": variant, "left": variant}

    suffix = box_type[len(variant) + 1 :]
    sides = {"top": "thin", "right": "thin", "bottom": "thin", "left": "thin"}

    if suffix == "top_and_bottom":
        sides["top"]    = variant
        sides["bottom"] = variant
    elif suffix == "left_and_right":
        sides["left"]  = variant
        sides["right"] = variant
    elif suffix == "top_only":
        sides["top"] = variant
    elif suffix == "bottom_only":
        sides["bottom"] = variant
    elif suffix == "right_only":
        sides["right"] = variant
    elif suffix == "left_only":
        sides["left"] = variant
    elif suffix == "left_and_top":
        sides["left"] = variant
        sides["top"]  = variant
    elif suffix == "right_and_top":
        sides["right"] = variant
        sides["top"]   = variant
    elif suffix == "right_and_bottom":
        sides["right"]  = variant
        sides["bottom"] = variant
    elif suffix == "left_and_bottom":
        sides["left"]   = variant
        sides["bottom"] = variant
    elif suffix == "but_bottom":
        sides = {"top": variant, "right": variant, "bottom": "thin", "left": variant}
    elif suffix == "but_left":
        sides = {"top": variant, "right": variant, "bottom": variant, "left": "thin"}
    elif suffix == "but_top":
        sides = {"top": "thin", "right": variant, "bottom": variant, "left": variant}
    elif suffix == "but_right":
        sides = {"top": variant, "right": "thin", "bottom": variant, "left": variant}
    elif suffix in {"corners_only", "chain"}:
        pass
    else:
        raise ValueError(f"box_type not supported: {box_type}")

    return sides


def _build_standard_box(lines: List[str], max_len: int, box_type: str) -> Tuple[str, str, List[str]]:
    width = max_len + 2
    sides = _resolve_sides(box_type)

    if box_type == "round":
        top_left     = _ROUND_CORNERS["top_left"]
        top_right    = _ROUND_CORNERS["top_right"]
        bottom_left  = _ROUND_CORNERS["bottom_left"]
        bottom_right = _ROUND_CORNERS["bottom_right"]
    elif box_type.endswith("corners_only"):
        variant      = "bold" if box_type.startswith("bold") else "double"
        top_left     = _CORNER_CHARS["top_left"][(variant, variant)]
        top_right    = _CORNER_CHARS["top_right"][(variant, variant)]
        bottom_left  = _CORNER_CHARS["bottom_left"][(variant, variant)]
        bottom_right = _CORNER_CHARS["bottom_right"][(variant, variant)]
    else:
        top_left     = _CORNER_CHARS["top_left"][(sides["top"], sides["left"])]
        top_right    = _CORNER_CHARS["top_right"][(sides["top"], sides["right"])]
        bottom_left  = _CORNER_CHARS["bottom_left"][(sides["bottom"], sides["left"])]
        bottom_right = _CORNER_CHARS["bottom_right"][(sides["bottom"], sides["right"])]

    top_border    = top_left + (_HORIZONTAL_CHARS[sides["top"]] * width) + top_right
    bottom_border = bottom_left + (_HORIZONTAL_CHARS[sides["bottom"]] * width) + bottom_right
    boxed_lines   = [
        f"{_VERTICAL_CHARS[sides['left']]} {line.ljust(max_len)} {_VERTICAL_CHARS[sides['right']]}"
        for line in lines
    ]

    return top_border, bottom_border, boxed_lines


def _build_chain_box(lines: List[str], max_len: int, box_type: str) -> Tuple[str, str, List[str]]:
    width = max_len + 2
    variant = "bold" if box_type.startswith("bold") else "double"
    top_border = (
        _CORNER_CHARS["top_left"][(variant, variant)]
        + _repeat_pattern(_HORIZONTAL_CHARS["thin"] + _HORIZONTAL_CHARS[variant], width)
        + _CORNER_CHARS["top_right"][(variant, variant)]
    )
    bottom_border = (
        _CORNER_CHARS["bottom_left"][(variant, variant)]
        + _repeat_pattern(_HORIZONTAL_CHARS["thin"] + _HORIZONTAL_CHARS[variant], width)
        + _CORNER_CHARS["bottom_right"][(variant, variant)]
    )
    boxed_lines = []

    for index, line in enumerate(lines):
        side_type = variant if index % 2 else "thin"
        vertical  = _VERTICAL_CHARS[side_type]
        boxed_lines.append(f"{vertical} {line.ljust(max_len)} {vertical}")

    return top_border, bottom_border, boxed_lines


def boxing(string: str, box_type: str = "thin") -> str:
    if box_type not in _SUPPORTED_BOX_TYPES:
        supported = ", ".join(_SUPPORTED_BOX_TYPES)
        raise ValueError(f"box_type not supported: {box_type}. Use one of: {supported}")

    lines   = string.splitlines() or [""]
    max_len = max(len(line) for line in lines)

    if box_type.endswith("chain"):
        top_border, bottom_border, boxed_lines = _build_chain_box(lines, max_len, box_type)
    else:
        top_border, bottom_border, boxed_lines = _build_standard_box(lines, max_len, box_type)

    return "\n".join([top_border] + boxed_lines + [bottom_border])