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

| `box_type`                | Preview                                        |
|---------------------------|------------------------------------------------|
| `thin`                    | `┌───────┐`<br>`│ lines │`<br>`└───────┘`      |
| `double`                  | `╔═══════╗`<br>`║ lines ║`<br>`╚═══════╝`      |
| `bold`                    | `┏━━━━━━━┓`<br>`┃ lines ┃`<br>`┗━━━━━━━┛`      |
| `round`                   | `╭───────╮`<br>`│ lines │`<br>`╰───────╯`      |
| `bold_top_and_bottom`     | `┍━━━━━━━┑`<br>`│ lines │`<br>`┕━━━━━━━┙`      |
| `double_top_and_bottom`   | `╒═══════╕`<br>`│ lines │`<br>`╘═══════╛`      |
| `bold_left_and_right`     | `┎───────┒`<br>`┃ lines ┃`<br>`┖───────┚`      |
| `double_left_and_right`   | `╓───────╖`<br>`║ lines ║`<br>`╙───────╜`      |
| `bold_top_only`           | `┍━━━━━━━┑`<br>`│ lines │`<br>`└───────┘`      |
| `double_top_only`         | `╒═══════╕`<br>`│ lines │`<br>`└───────┘`      |
| `bold_bottom_only`        | `┌───────┐`<br>`│ lines │`<br>`┕━━━━━━━┙`      |
| `double_bottom_only`      | `┌───────┐`<br>`│ lines │`<br>`╘═══════╛`      |
| `bold_right_only`         | `┌───────┒`<br>`│ lines ┃`<br>`└───────┚`      |
| `double_right_only`       | `┌───────╖`<br>`│ lines ║`<br>`└───────╜`      |
| `bold_left_only`          | `┎───────┐`<br>`┃ lines │`<br>`┖───────┘`      |
| `double_left_only`        | `╓───────┐`<br>`║ lines │`<br>`╙───────┘`      |
| `bold_left_and_top`       | `┏━━━━━━━┑`<br>`┃ lines │`<br>`┖───────┘`      |
| `double_left_and_top`     | `╔═══════╕`<br>`║ lines │`<br>`╙───────┘`      |
| `bold_right_and_top`      | `┍━━━━━━━┓`<br>`│ lines ┃`<br>`└───────┚`      |
| `double_right_and_top`    | `╒═══════╗`<br>`│ lines ║`<br>`└───────╜`      |
| `bold_right_and_bottom`   | `┌───────┒`<br>`│ lines ┃`<br>`┕━━━━━━━┛`      |
| `double_right_and_bottom` | `┌───────╖`<br>`│ lines ║`<br>`╘═══════╝`      |
| `bold_left_and_bottom`    | `┎───────┐`<br>`┃ lines │`<br>`┗━━━━━━━┙`      |
| `double_left_and_bottom`  | `╓───────┐`<br>`║ lines │`<br>`╚═══════╛`      |
| `bold_but_bottom`         | `┏━━━━━━━┓`<br>`┃ lines ┃`<br>`┖───────┚`      |
| `double_but_bottom`       | `╔═══════╗`<br>`║ lines ║`<br>`╙───────╜`      |
| `bold_but_left`           | `┍━━━━━━━┓`<br>`│ lines ┃`<br>`┕━━━━━━━┛`      |
| `double_but_left`         | `╒═══════╗`<br>`│ lines ║`<br>`╘═══════╝`      |
| `bold_but_top`            | `┎───────┒`<br>`┃ lines ┃`<br>`┗━━━━━━━┛`      |
| `double_but_top`          | `╓───────╖`<br>`║ lines ║`<br>`╚═══════╝`      |
| `bold_but_right`          | `┏━━━━━━━┑`<br>`┃ lines │`<br>`┗━━━━━━━┙`      |
| `double_but_right`        | `╔═══════╕`<br>`║ lines │`<br>`╚═══════╛`      |
| `bold_corners_only`       | `┏───────┓`<br>`│ lines │`<br>`┗───────┛`      |
| `double_corners_only`     | `╔───────╗`<br>`│ lines │`<br>`╚───────╝`      |
| `bold_chain`              | `┏─━─━─━─┓`<br>`│ lines │`<br>`┗─━─━─━─┛`      |
| `double_chain`            | `╔─═─═─═─╗`<br>`│ lines │`<br>`╚─═─═─═─╝`      |

## Error handling

Passing an invalid `box_type` raises a `ValueError` listing all valid options:

```python
boxing("text", box_type="unknown")
# ValueError: box_type not supported: unknown. Use one of: thin, double, bold, ...
```

## License

MIT