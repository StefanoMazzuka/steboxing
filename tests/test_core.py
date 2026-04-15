import unittest
from unittest import result
from steboxing.core import boxing

class TestBoxing(unittest.TestCase):
    def test_wrong_box_type(self):
        self.assertRaises(ValueError, lambda: boxing("hello\nworld!", box_type="wrong"))

    def test_thin(self):
        result_empty   = boxing("", box_type="thin")
        result_correct = boxing("hello\nworld!", box_type="thin")

        expected_empty = (
            "┌──┐\n"
            "│  │\n"
            "└──┘"
        )  
        expected_correct = (
            "┌────────┐\n"
            "│ hello  │\n"
            "│ world! │\n"
            "└────────┘"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)

    def test_double(self):
        result_empty   = boxing("", box_type="double")
        result_correct = boxing("hello\nworld!", box_type="double")

        expected_empty = (
            "╔══╗\n"
            "║  ║\n"
            "╚══╝"
        )  
        expected_correct = (
            "╔════════╗\n"
            "║ hello  ║\n"
            "║ world! ║\n"
            "╚════════╝"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_bold(self):
        result_empty   = boxing("", box_type="bold")
        result_correct = boxing("hello\nworld!", box_type="bold")

        expected_empty = (
            "┏━━┓\n"
            "┃  ┃\n"
            "┗━━┛"
        )  
        expected_correct = (
            "┏━━━━━━━━┓\n"
            "┃ hello  ┃\n"
            "┃ world! ┃\n"
            "┗━━━━━━━━┛"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_round(self):
        result_empty   = boxing("", box_type="round")
        result_correct = boxing("hello\nworld!", box_type="round")

        expected_empty = (
            "╭──╮\n"
            "│  │\n"
            "╰──╯"
        )  
        expected_correct = (
            "╭────────╮\n"
            "│ hello  │\n"
            "│ world! │\n"
            "╰────────╯"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_bold_top_and_bottom(self):
        result_empty   = boxing("", box_type="bold_top_and_bottom")
        result_correct = boxing("hello\nworld!", box_type="bold_top_and_bottom")

        expected_empty = (
            "┍━━┑\n"
            "│  │\n"
            "┕━━┙"
        )  
        expected_correct = (
            "┍━━━━━━━━┑\n"
            "│ hello  │\n"
            "│ world! │\n"
            "┕━━━━━━━━┙"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_double_top_and_bottom(self):
        result_empty   = boxing("", box_type="double_top_and_bottom")
        result_correct = boxing("hello\nworld!", box_type="double_top_and_bottom")

        expected_empty = (
            "╒══╕\n"
            "│  │\n"
            "╘══╛"
        )  
        expected_correct = (
            "╒════════╕\n"
            "│ hello  │\n"
            "│ world! │\n"
            "╘════════╛"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_bold_left_and_right(self):
        result_empty   = boxing("", box_type="bold_left_and_right")
        result_correct = boxing("hello\nworld!", box_type="bold_left_and_right")

        expected_empty = (
            "┎──┒\n"
            "┃  ┃\n"
            "┖──┚"
        )  
        expected_correct = (
            "┎────────┒\n"
            "┃ hello  ┃\n"
            "┃ world! ┃\n"
            "┖────────┚"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_double_left_and_right(self):
        result_empty   = boxing("", box_type="double_left_and_right")
        result_correct = boxing("hello\nworld!", box_type="double_left_and_right")

        expected_empty = (
            "╓──╖\n"
            "║  ║\n"
            "╙──╜"
        )  
        expected_correct = (
            "╓────────╖\n"
            "║ hello  ║\n"
            "║ world! ║\n"
            "╙────────╜"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_bold_top_only(self):
        result_empty   = boxing("", box_type="bold_top_only")
        result_correct = boxing("hello\nworld!", box_type="bold_top_only")

        expected_empty = (
            "┍━━┑\n"
            "│  │\n"
            "└──┘"
        )  
        expected_correct = (
            "┍━━━━━━━━┑\n"
            "│ hello  │\n"
            "│ world! │\n"
            "└────────┘"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_double_top_only(self):
        result_empty   = boxing("", box_type="double_top_only")
        result_correct = boxing("hello\nworld!", box_type="double_top_only")

        expected_empty = (
            "╒══╕\n"
            "│  │\n"
            "└──┘"
        )  
        expected_correct = (
            "╒════════╕\n"
            "│ hello  │\n"
            "│ world! │\n"
            "└────────┘"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_bold_bottom_only(self):
        result_empty   = boxing("", box_type="bold_bottom_only")
        result_correct = boxing("hello\nworld!", box_type="bold_bottom_only")

        expected_empty = (
            "┌──┐\n"
            "│  │\n"
            "┕━━┙"
        )  
        expected_correct = (
            "┌────────┐\n"
            "│ hello  │\n"
            "│ world! │\n"
            "┕━━━━━━━━┙"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_double_bottom_only(self):
        result_empty   = boxing("", box_type="double_bottom_only")
        result_correct = boxing("hello\nworld!", box_type="double_bottom_only")

        expected_empty = (
            "┌──┐\n"
            "│  │\n"
            "╘══╛"
        )  
        expected_correct = (
            "┌────────┐\n"
            "│ hello  │\n"
            "│ world! │\n"
            "╘════════╛"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_bold_right_only(self):
        result_empty   = boxing("", box_type="bold_right_only")
        result_correct = boxing("hello\nworld!", box_type="bold_right_only")

        expected_empty = (
            "┌──┒\n"
            "│  ┃\n"
            "└──┚"
        )  
        expected_correct = (
            "┌────────┒\n"
            "│ hello  ┃\n"
            "│ world! ┃\n"
            "└────────┚"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_double_right_only(self):
        result_empty   = boxing("", box_type="double_right_only")
        result_correct = boxing("hello\nworld!", box_type="double_right_only")

        expected_empty = (
            "┌──╖\n"
            "│  ║\n"
            "└──╜"
        )  
        expected_correct = (
            "┌────────╖\n"
            "│ hello  ║\n"
            "│ world! ║\n"
            "└────────╜"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_bold_left_only(self):
        result_empty   = boxing("", box_type="bold_left_only")
        result_correct = boxing("hello\nworld!", box_type="bold_left_only")

        expected_empty = (
            "┎──┐\n"
            "┃  │\n"
            "┖──┘"
        )  
        expected_correct = (
            "┎────────┐\n"
            "┃ hello  │\n"
            "┃ world! │\n"
            "┖────────┘"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_double_left_only(self):
        result_empty   = boxing("", box_type="double_left_only")
        result_correct = boxing("hello\nworld!", box_type="double_left_only")

        expected_empty = (
            "╓──┐\n"
            "║  │\n"
            "╙──┘"
        )  
        expected_correct = (
            "╓────────┐\n"
            "║ hello  │\n"
            "║ world! │\n"
            "╙────────┘"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_bold_left_and_top(self):
        result_empty   = boxing("", box_type="bold_left_and_top")
        result_correct = boxing("hello\nworld!", box_type="bold_left_and_top")

        expected_empty = (
            "┏━━┑\n"
            "┃  │\n"
            "┖──┘"
        )  
        expected_correct = (
            "┏━━━━━━━━┑\n"
            "┃ hello  │\n"
            "┃ world! │\n"
            "┖────────┘"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_double_left_and_top(self):
        result_empty   = boxing("", box_type="double_left_and_top")
        result_correct = boxing("hello\nworld!", box_type="double_left_and_top")

        expected_empty = (
            "╔══╕\n"
            "║  │\n"
            "╙──┘"
        )  
        expected_correct = (
            "╔════════╕\n"
            "║ hello  │\n"
            "║ world! │\n"
            "╙────────┘"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_bold_right_and_top(self):
        result_empty   = boxing("", box_type="bold_right_and_top")
        result_correct = boxing("hello\nworld!", box_type="bold_right_and_top")

        expected_empty = (
            "┍━━┓\n"
            "│  ┃\n"
            "└──┚"
        )  
        expected_correct = (
            "┍━━━━━━━━┓\n"
            "│ hello  ┃\n"
            "│ world! ┃\n"
            "└────────┚"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_double_right_and_top(self):
        result_empty   = boxing("", box_type="double_right_and_top")
        result_correct = boxing("hello\nworld!", box_type="double_right_and_top")

        expected_empty = (
            "╒══╗\n"
            "│  ║\n"
            "└──╜"
        )  
        expected_correct = (
            "╒════════╗\n"
            "│ hello  ║\n"
            "│ world! ║\n"
            "└────────╜"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_bold_right_and_bottom(self):
        result_empty   = boxing("", box_type="bold_right_and_bottom")
        result_correct = boxing("hello\nworld!", box_type="bold_right_and_bottom")

        expected_empty = (
            "┌──┒\n"
            "│  ┃\n"
            "┕━━┛"
        )  
        expected_correct = (
            "┌────────┒\n"
            "│ hello  ┃\n"
            "│ world! ┃\n"
            "┕━━━━━━━━┛"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_double_right_and_bottom(self):
        result_empty   = boxing("", box_type="double_right_and_bottom")
        result_correct = boxing("hello\nworld!", box_type="double_right_and_bottom")

        expected_empty = (
            "┌──╖\n"
            "│  ║\n"
            "╘══╝"
        )  
        expected_correct = (
            "┌────────╖\n"
            "│ hello  ║\n"
            "│ world! ║\n"
            "╘════════╝"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_bold_left_and_bottom(self):
        result_empty   = boxing("", box_type="bold_left_and_bottom")
        result_correct = boxing("hello\nworld!", box_type="bold_left_and_bottom")

        expected_empty = (
            "┎──┐\n"
            "┃  │\n"
            "┗━━┙"
        )  
        expected_correct = (
            "┎────────┐\n"
            "┃ hello  │\n"
            "┃ world! │\n"
            "┗━━━━━━━━┙"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_double_left_and_bottom(self):
        result_empty   = boxing("", box_type="double_left_and_bottom")
        result_correct = boxing("hello\nworld!", box_type="double_left_and_bottom")

        expected_empty = (
            "╓──┐\n"
            "║  │\n"
            "╚══╛"
        )  
        expected_correct = (
            "╓────────┐\n"
            "║ hello  │\n"
            "║ world! │\n"
            "╚════════╛"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_bold_but_bottom(self):
        result_empty   = boxing("", box_type="bold_but_bottom")
        result_correct = boxing("hello\nworld!", box_type="bold_but_bottom")

        expected_empty = (
            "┏━━┓\n"
            "┃  ┃\n"
            "┖──┚"
        )  
        expected_correct = (
            "┏━━━━━━━━┓\n"
            "┃ hello  ┃\n"
            "┃ world! ┃\n"
            "┖────────┚"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_double_but_bottom(self):
        result_empty   = boxing("", box_type="double_but_bottom")
        result_correct = boxing("hello\nworld!", box_type="double_but_bottom")

        expected_empty = (
            "╔══╗\n"
            "║  ║\n"
            "╙──╜"
        )  
        expected_correct = (
            "╔════════╗\n"
            "║ hello  ║\n"
            "║ world! ║\n"
            "╙────────╜"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_bold_but_left(self):
        result_empty   = boxing("", box_type="bold_but_left")
        result_correct = boxing("hello\nworld!", box_type="bold_but_left")

        expected_empty = (
            "┍━━┓\n"
            "│  ┃\n"
            "┕━━┛"
        )  
        expected_correct = (
            "┍━━━━━━━━┓\n"
            "│ hello  ┃\n"
            "│ world! ┃\n"
            "┕━━━━━━━━┛"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_double_but_left(self):
        result_empty   = boxing("", box_type="double_but_left")
        result_correct = boxing("hello\nworld!", box_type="double_but_left")

        expected_empty = (
            "╒══╗\n"
            "│  ║\n"
            "╘══╝"
        )  
        expected_correct = (
            "╒════════╗\n"
            "│ hello  ║\n"
            "│ world! ║\n"
            "╘════════╝"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_bold_but_top(self):
        result_empty   = boxing("", box_type="bold_but_top")
        result_correct = boxing("hello\nworld!", box_type="bold_but_top")

        expected_empty = (
            "┎──┒\n"
            "┃  ┃\n"
            "┗━━┛"
        )  
        expected_correct = (
            "┎────────┒\n"
            "┃ hello  ┃\n"
            "┃ world! ┃\n"
            "┗━━━━━━━━┛"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_double_but_top(self):
        result_empty   = boxing("", box_type="double_but_top")
        result_correct = boxing("hello\nworld!", box_type="double_but_top")

        expected_empty = (
            "╓──╖\n"
            "║  ║\n"
            "╚══╝"
        )  
        expected_correct = (
            "╓────────╖\n"
            "║ hello  ║\n"
            "║ world! ║\n"
            "╚════════╝"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_bold_but_right(self):
        result_empty   = boxing("", box_type="bold_but_right")
        result_correct = boxing("hello\nworld!", box_type="bold_but_right")

        expected_empty = (
            "┏━━┑\n"
            "┃  │\n"
            "┗━━┙"
        )  
        expected_correct = (
            "┏━━━━━━━━┑\n"
            "┃ hello  │\n"
            "┃ world! │\n"
            "┗━━━━━━━━┙"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_double_but_right(self):
        result_empty   = boxing("", box_type="double_but_right")
        result_correct = boxing("hello\nworld!", box_type="double_but_right")

        expected_empty = (
            "╔══╕\n"
            "║  │\n"
            "╚══╛"
        )  
        expected_correct = (
            "╔════════╕\n"
            "║ hello  │\n"
            "║ world! │\n"
            "╚════════╛"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_bold_corners_only(self):
        result_empty   = boxing("", box_type="bold_corners_only")
        result_correct = boxing("hello\nworld!", box_type="bold_corners_only")

        expected_empty = (
            "┏──┓\n"
            "│  │\n"
            "┗──┛"
        )  
        expected_correct = (
            "┏────────┓\n"
            "│ hello  │\n"
            "│ world! │\n"
            "┗────────┛"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_double_corners_only(self):
        result_empty   = boxing("", box_type="double_corners_only")
        result_correct = boxing("hello\nworld!", box_type="double_corners_only")

        expected_empty = (
            "╔──╗\n"
            "│  │\n"
            "╚──╝"
        )  
        expected_correct = (
            "╔────────╗\n"
            "│ hello  │\n"
            "│ world! │\n"
            "╚────────╝"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_bold_chain(self):
        result_empty   = boxing("", box_type="bold_chain")
        result_correct = boxing("hello\nworld!", box_type="bold_chain")

        expected_empty = (
            "┏─━┓\n"
            "│  │\n"
            "┗─━┛"
        )  
        expected_correct = (
            "┏─━─━─━─━┓\n"
            "│ hello  │\n"
            "┃ world! ┃\n"
            "┗─━─━─━─━┛"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        
    def test_double_chain(self):
        result_empty   = boxing("", box_type="double_chain")
        result_correct = boxing("hello\nworld!", box_type="double_chain")

        expected_empty = (
            "╔─═╗\n"
            "│  │\n"
            "╚─═╝"
        )  
        expected_correct = (
            "╔─═─═─═─═╗\n"
            "│ hello  │\n"
            "║ world! ║\n"
            "╚─═─═─═─═╝"
        )

        self.assertTrue(result_empty   == expected_empty)
        self.assertTrue(result_correct == expected_correct)
        

if __name__ == "__main__":
    unittest.main()
