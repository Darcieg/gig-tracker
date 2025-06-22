from pathlib import Path
import csv

def save_gig_to_csv(gig_data: dict, filename="data/gigs.csv"):
    file_path = Path(filename)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_exists = file_path.exists()

    with file_path.open(mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=gig_data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(gig_data)