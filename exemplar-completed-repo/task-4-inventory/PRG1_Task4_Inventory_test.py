"""
Automated checks for Task 4: Test-Driven Completion (Inventory Tracker).

Run with: pytest PRG1_Task4_Inventory_test.py

This file is part of the specification for Task 4, alongside the
docstrings already in PRG1_Task4_Inventory_starter.py. Place your
completed starter file in the same folder as this test file, then
run pytest. You do not need to change anything in this file.
"""

import importlib.util
import sys
from pathlib import Path

MODULE_PATH = Path(__file__).parent / "PRG1_Task4_Inventory_starter.py"


def load_submission():
    spec = importlib.util.spec_from_file_location("submission", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules["submission"] = module
    spec.loader.exec_module(module)
    return module


submission = load_submission()


# ---- functions that already worked before you started: a quick regression check ----

def test_existing_functions_still_work():
    inventory = submission.create_inventory()
    submission.add_stock(inventory, "Widget", 10)
    submission.add_stock(inventory, "Widget", 5)
    assert submission.get_quantity(inventory, "Widget") == 15
    assert submission.get_quantity(inventory, "Unknown") == 0


# ---- remove_stock ----

def test_remove_stock_succeeds_with_enough_stock():
    inventory = submission.create_inventory()
    submission.add_stock(inventory, "Widget", 10)
    result = submission.remove_stock(inventory, "Widget", 3)
    assert result is True
    assert submission.get_quantity(inventory, "Widget") == 7


def test_remove_stock_fails_with_insufficient_stock():
    inventory = submission.create_inventory()
    submission.add_stock(inventory, "Gadget", 2)
    result = submission.remove_stock(inventory, "Gadget", 100)
    assert result is False
    # Stock must be left unchanged when removal fails.
    assert submission.get_quantity(inventory, "Gadget") == 2


def test_remove_stock_fails_for_unknown_item():
    inventory = submission.create_inventory()
    submission.add_stock(inventory, "Widget", 10)
    result = submission.remove_stock(inventory, "Sprocket", 1)
    assert result is False
    assert submission.get_quantity(inventory, "Sprocket") == 0


def test_remove_stock_exact_amount_succeeds():
    inventory = submission.create_inventory()
    submission.add_stock(inventory, "Widget", 5)
    result = submission.remove_stock(inventory, "Widget", 5)
    assert result is True
    assert submission.get_quantity(inventory, "Widget") == 0


# ---- low_stock_items ----

def test_low_stock_items_finds_matches():
    inventory = submission.create_inventory()
    submission.add_stock(inventory, "Widget", 10)
    submission.add_stock(inventory, "Gadget", 2)
    submission.add_stock(inventory, "Sprocket", 1)
    result = submission.low_stock_items(inventory, 2)
    assert set(result) == {"Gadget", "Sprocket"}


def test_low_stock_items_no_matches_returns_empty_list():
    inventory = submission.create_inventory()
    submission.add_stock(inventory, "Widget", 10)
    assert submission.low_stock_items(inventory, 2) == []


def test_low_stock_items_empty_inventory():
    inventory = submission.create_inventory()
    assert submission.low_stock_items(inventory, 5) == []


# ---- integration: functions used together ----

def test_functions_work_together():
    inventory = submission.create_inventory()
    submission.add_stock(inventory, "Widget", 10)
    submission.remove_stock(inventory, "Widget", 8)
    assert submission.get_quantity(inventory, "Widget") == 2
    assert "Widget" in submission.low_stock_items(inventory, 2)


if __name__ == "__main__":
    import pytest
    sys.exit(pytest.main([__file__, "-v"]))
