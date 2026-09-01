# Task 4: Test-Driven Completion

Worth 15% of the module assignment | Individual work | Module code PRG1

## What you're doing

`PRG1_Task4_Inventory_starter.py` is a working inventory tracker for a small warehouse. It can already create an inventory, add stock, and look up how much of an item is held. Run it now, before changing anything; it works.

The warehouse also needs to remove stock when items are shipped out, and to flag items that are running low. That part is not built yet. As with Task 3, the specification here is not written out in prose: it is written as a set of automated tests, in `PRG1_Task4_Inventory_test.py`. Your job is to add the missing functionality so that every test passes, using the existing functions rather than working around them.

Do not change `PRG1_Task4_Inventory_test.py`, and do not change the behaviour of the functions that already work.

More marks are available for explaining your extension than for the code passing on its own. Working code is necessary but not sufficient here; see "Explain your approach" below before you consider this task finished.

## What's already there

These functions are complete and already correct. Read them before you start.

| Function | What it does |
|---|---|
| `create_inventory()` | Returns a new, empty inventory. |
| `add_stock(inventory, item_name, quantity)` | Adds `quantity` units of `item_name` to `inventory`, creating the entry if it does not already exist. Changes `inventory` in place. |
| `get_quantity(inventory, item_name)` | Returns the quantity of `item_name` in `inventory`, or 0 if it is not in the inventory at all. |

## What you need to add

Two new functions, currently left as `pass`:

| Function | What it needs to do |
|---|---|
| `remove_stock(inventory, item_name, quantity)` | Remove `quantity` units of `item_name` from `inventory`, if there is enough stock. Return `True` and update `inventory` if successful. Return `False` and leave `inventory` unchanged if there is not enough stock, or if `item_name` is not in the inventory at all. Use `get_quantity` to check the current stock level; do not read `inventory[item_name]` directly. |
| `low_stock_items(inventory, threshold)` | Return a list of every item name in `inventory` whose quantity is at or below `threshold`. Return an empty list if none match. |

## Run the tests

With both files in the same folder, run:

`pytest PRG1_Task4_Inventory_test.py -v`

One test passes immediately, before you change anything: this confirms the existing functions still work. The rest will fail until you have added the two new functions.

## A note on approach

`remove_stock` should call `get_quantity` rather than checking `inventory[item_name]` directly. This matters for more than just style: if you check the dict directly for an item that has never been added, Python raises an error, whereas `get_quantity` is already written to handle that case safely and return 0.

## Explain your approach

This section carries more of the marks for this task than the code itself. Passing tests shows your code works; these questions show you understand why. Answer in `ANSWERS_T4.md`, in your own words, specific to this program.

1. Explain why `remove_stock` calls `get_quantity` instead of reading `inventory[item_name]` directly. What would go wrong if it didn't, and for which items specifically?
2. Without running it, work out what happens when you call `remove_stock` on an item that has never been added to the inventory. Walk through your code line by line: what does `get_quantity` return, what does your condition check, and what does the function return and change as a result?
3. In your own words, explain the difference between how a dictionary behaves when you access a missing key with square brackets, for example `inventory["Sprocket"]`, versus with `.get()`, for example `inventory.get("Sprocket", 0)`. Why does that difference matter for this program specifically?
4. `low_stock_items` must include items exactly at the threshold, not only below it. Give a specific example inventory and threshold where using `<` instead of `<=` would produce a different, wrong result, and explain why the specification's "at or below" wording matters in practice.

## If you used an AI tool

AI tool use on this task does not need to be logged separately. At the end of the module you will complete one short reflection, `PRG1_AI_Use_Reflection`, covering AI use across the whole assignment. It is mandatory to submit, but not marked.

## Submission

Submit your completed `PRG1_Task4_Inventory_starter.py` file, alongside `ANSWERS_T4.md` with the four questions above answered. Do not submit a modified version of the test file.
