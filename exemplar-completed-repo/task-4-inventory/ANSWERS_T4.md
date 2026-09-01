# Task 4: Test-Driven Completion, Answers

Complete this alongside `BRIEF_T4.md`.

## Explain your approach

### 1. Why does `remove_stock` call `get_quantity` instead of reading `inventory[item_name]` directly?

> Because `get_quantity` already handles items that haven't been added yet, it just returns 0 for those instead of crashing. If I used `inventory[item_name]` directly and the item wasn't a key in the dictionary yet, Python would raise a `KeyError` and stop the whole program instead of just returning `False` like it's meant to.

### 2. Trace `remove_stock` on an item never added to the inventory

> `get_quantity` would return 0, since the item isn't in the inventory. Then the condition `current >= quantity` compares 0 against whatever quantity was asked for, which is `False` for any quantity above 0, so the function returns `False` straight away and the inventory is left completely unchanged.

### 3. Difference between `inventory["Sprocket"]` and `inventory.get("Sprocket", 0)`

> Square brackets raise a `KeyError` if `"Sprocket"` isn't already a key in the dictionary. `.get()` is safer because if the key isn't there it just returns the default value you gave it, 0 in this case, instead of crashing the program.

### 4. Why does the `<=` threshold boundary matter in `low_stock_items`?

> If an inventory had `Gadget` at quantity 5 and the threshold was also 5, using `<` would mean `5 < 5` is `False`, so `Gadget` wouldn't be flagged as low stock even though it's sitting exactly on the threshold. The spec says "at or below" the threshold, which means it should be included, so `<=` is needed instead of `<`.
