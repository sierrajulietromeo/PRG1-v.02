# Task 4: Test-Driven Completion, Marking Scheme

Companion to `BRIEF_T4.md` | Module code PRG1

20 marks total, 15% of the module assignment: 8 for code correctness, 12 for explaining your approach across 4 questions.

## Part 1: Code correctness, 8 marks

Run `pytest PRG1_Task4_Inventory_test.py -v` against the submission.

| Group | Marks | Covers |
|---|---|---|
| Existing functions unaffected | 1 | `test_existing_functions_still_work`. |
| `remove_stock` | 3 | The 4 `remove_stock` tests (sufficient stock, insufficient stock, unknown item, exact amount). |
| `low_stock_items` | 2 | The 3 `low_stock_items` tests (matches, no matches, empty inventory). |
| Integration and code quality | 2 | `test_functions_work_together`; `remove_stock` genuinely calls `get_quantity` rather than the dict directly; given functions untouched. |

## Part 2: Explain your approach, 12 marks

| Marks | What it shows |
|---|---|
| 9-12 | All four answers correct, specific to this program, clearly reasoned. |
| 5-8 | Some answers correct and specific; others incomplete or generic. |
| 0-4 | Mostly incorrect, generic, or restates the code without addressing why. |
