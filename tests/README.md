# 🎸 Gig Tracker

A lightweight Streamlit app for tracking gig economy work—designed to calculate earnings, mileage, and real-world profitability with clarity and precision.

Originally built to support part-time driving and delivery work, this tool helps answer the key question: _Is this worth my time?_

---

## 🚀 Features

- Input your gig details (vendor, pay, mileage, time, notes)
- Save to CSV (with append logic and formatting safeguards)
- Auto-calculate total pay, duration, and $/hour rate
- Run unit tests to ensure CSV storage works correctly
- Clean modular logic with support for future analytics

---

## 📂 Project Structure
```
gig-tracker/
├── app.py                 # Streamlit app
├── logic/                 # Business logic modules
│   ├── calculations.py
│   └── storage.py
├── tests/                 # Unit tests
│   ├── test_storage.py
│   ├── test_calculations.py (optional)
│   ├── sample_data/
│   │   └── test_input_gig.csv
│   └── test_output/
├── docs/                  # Auto-generated (optional)
├── requirements.txt
└── README.md
```
ImportError: cannot import name 'save_gig_to_csv' from 'logic.storage' (c:\Users\darci\gig-tracker\logic\storage.py)

File "c:\Users\darci\gig-tracker\app.py", line 4, in <module>
    from logic.storage import save_gig_to_csv