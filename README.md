# steboxing

A Python library for drawing Unicode text boxes around strings — supports 36 border styles using thin, bold, double, and round line characters.

## Installation

```bash
pip install -e .
```

## Build and publish (modern flow)

Do not run `python setup.py ...` directly.

Build distributions:

```bash
python -m pip install --upgrade build
python -m build
```

Upload to PyPI:

```bash
python -m pip install --upgrade twine
python -m twine upload dist/*
```

## Usage

```python
from steboxing import boxing

print(boxing("Hello, World!", box_type="thin"))
```

```
┌───────────────┐
│ Hello, World! │
└───────────────┘
```

Multi-line strings are supported:

```python
print(boxing("Line one\nLine two\nLine three", box_type="double"))
```

```
╔════════════╗
║ Line one   ║
║ Line two   ║
║ Line three ║
╚════════════╝
```

`box_type` defaults to `"thin"` if omitted.

## Box styles

| `box_type`                | Preview                      |
|---------------------------|------------------------------|
| `thin`                    | `┌─┐ │ │ └─┘`                |
| `double`                  | `╔═╗ ║ ║ ╚═╝`                |
| `bold`                    | `┏━┓ ┃ ┃ ┗━┛`                |
| `round`                   | `╭─╮ │ │ ╰─╯`                |
| `bold_top_and_bottom`     | `┍━┑ │ │ ┕━┙`                |
| `double_top_and_bottom`   | `╒═╕ │ │ ╘═╛`                |
| `bold_left_and_right`     | `┎─┒ ┃ ┃ ┖─┚`                |
| `double_left_and_right`   | `╓─╖ ║ ║ ╙─╜`                |
| `bold_top_only`           | `┍━┑ │ │ └─┘`                |
| `double_top_only`         | `╒═╕ │ │ └─┘`                |
| `bold_bottom_only`        | `┌─┐ │ │ ┕━┙`                |
| `double_bottom_only`      | `┌─┐ │ │ ╘═╛`                |
| `bold_right_only`         | `┌─┒ │ ┃ └─┚`                |
| `double_right_only`       | `┌─╖ │ ║ └─╜`                |
| `bold_left_only`          | `┎─┐ ┃ │ ┖─┘`                |
| `double_left_only`        | `╓─┐ ║ │ ╙─┘`                |
| `bold_left_and_top`       | `┏━┑ ┃ │ ┖─┘`                |
| `double_left_and_top`     | `╔═╕ ║ │ ╙─┘`                |
| `bold_right_and_top`      | `┍━┓ │ ┃ └─┚`                |
| `double_right_and_top`    | `╒═╗ │ ║ └─╜`                |
| `bold_right_and_bottom`   | `┌─┒ │ ┃ ┕━┛`                |
| `double_right_and_bottom` | `┌─╖ │ ║ ╘═╝`                |
| `bold_left_and_bottom`    | `┎─┐ ┃ │ ┗━┙`                |
| `double_left_and_bottom`  | `╓─┐ ║ │ ╚═╛`                |
| `bold_but_bottom`         | `┏━┓ ┃ ┃ ┖─┚`                |
| `double_but_bottom`       | `╔═╗ ║ ║ ╙─╜`                |
| `bold_but_left`           | `┍━┓ │ ┃ ┕━┛`                |
| `double_but_left`         | `╒═╗ │ ║ ╘═╝`                |
| `bold_but_top`            | `┎─┒ ┃ ┃ ┗━┛`                |
| `double_but_top`          | `╓─╖ ║ ║ ╚═╝`                |
| `bold_but_right`          | `┏━┑ ┃ │ ┗━┙`                |
| `double_but_right`        | `╔═╕ ║ │ ╚═╛`                |
| `bold_corners_only`       | `┏─┓ │ │ ┗─┛`                |
| `double_corners_only`     | `╔─╗ │ │ ╚─╝`                |
| `bold_chain`              | `┏─━─┓` alternating sides    |
| `double_chain`            | `╔─═─╗` alternating sides    |

## Error handling

Passing an invalid `box_type` raises a `ValueError` listing all valid options:

```python
boxing("text", box_type="unknown")
# ValueError: box_type not supported: unknown. Use one of: thin, double, bold, ...
```

## License

MIT
