# Lab Tutorials - BIT1054 Python

Lab tutorials for BIT1054 Fundamental of Computational Thinking (Python section), City University Malaysia.

Student: Islam Md Ashraful

## Contents

| Folder | Tutorial | Topic | How to run |
|---|---|---|---|
| `tutorial_1` | Week 2 | admission logic (AND/OR), truth table, flowchart, pseudocode | documentation only, see `w2_tutorial.md` |
| `week_3` | Week 3 | quiz average, pass/fail, repeat loop | `python Student_Ave_Calc.py` |
| `Tutorial_3` | Week 5 | cafe bill with two modules | `python main.py` inside the folder |
| `week_7` | Week 7 | bug fixing, input validation, pytest | `pytest` inside the folder (4 passed) |
| `week_8` | Week 8 | food delivery receipt, three modules | `python main.py` inside the folder |

## Repository Structure

```
python-lab-tutorials/
├── README.md
├── tutorial_1/                  week 2
│   ├── w2_tutorial.md
│   ├── admission_flowchart.drawio
│   └── admission_flowchart.png
├── week_3/                      week 3
│   ├── Student_Ave_Calc.py
│   └── w3_documentation.ipynb
├── Tutorial_3/                  week 5
│   ├── main.py
│   ├── utils.py
│   └── w5_documentation.md
├── week_7/                      week 7
│   ├── main.py
│   ├── food_order.py
│   ├── test_food_order.py
│   └── W7_documentation.txt
└── week_8/                      week 8
    ├── main.py
    ├── customer.py
    ├── receipt.py
    └── README.md
```

## Notes

- Each folder carries its own documentation: `w2_tutorial.md`, `w3_documentation.ipynb`, `w5_documentation.md`, `W7_documentation.txt` and `week_8/README.md`.
- Only the Python standard library is used, except pytest in `week_7` (`pip install pytest`).
- Each tutorial was committed separately following the git workflow from the lab document (git init, git add, git commit, git push).
