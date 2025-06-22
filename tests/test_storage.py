import unittest
import csv
from pathlib import Path
from logic.storage import save_gig_to_csv


class TestStorage(unittest.TestCase):
    """Tests for verifying CSV input/output storage logic using sample data."""


    def setUp(self):
        self.input_file = Path("tests") / "sample_data" / "test_input_gig.csv"
        self.output_dir = Path("tests") / "test_output"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.output_file = self.output_dir / "test_gigs_output.csv"

    def tearDown(self):
        for file in self.output_dir.glob("*"):
            if file.is_file():
                file.unlink()

    def test_csv_roundtrip(self):
        """Tests that saving and reloading a gig CSV preserves row data exactly."""

        # Load input
        with self.input_file.open(newline="") as f_in:
            reader = csv.DictReader(f_in)
            input_rows = list(reader)
            for row in input_rows:
                save_gig_to_csv(row, filename=str(self.output_file))

        # Load output
        with self.output_file.open(newline="") as f_out:
            reader = csv.DictReader(f_out)
            output_rows = list(reader)

        # Verify roundtrip fidelity
        self.assertEqual(output_rows, input_rows)