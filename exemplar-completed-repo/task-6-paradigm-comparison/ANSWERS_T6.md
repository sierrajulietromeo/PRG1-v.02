# Task 6: Paradigm Comparison, Answers

Complete this alongside `BRIEF_T6.md`.

## Guided comparison

### 1. Where is the data for a single book stored?

**Procedural version**

> Each book is a dictionary inside the `books` list, like `{"title": ..., "author": ..., "checked_out": False}`.

**Object-oriented version**

> Each book is an instance of the `Book` class, and all of the instances are stored inside `Library`'s `self.books` list.

### 2. How is "check out a book" implemented?

**Procedural version**

> The `check_out_book(books, title)` function loops through the list looking for a matching title that isn't already checked out, then sets `book["checked_out"] = True`.

**Object-oriented version**

> `Library` has a `check_out_book` method that finds the matching `Book` object by looping through `self.books`, then calls `book.check_out()` on it, which is a method that belongs to the `Book` class itself.

### 3. Trace: checking out an already checked-out book

**Procedural version**

> The loop's `if` condition checks `not book["checked_out"]` as well as the title, so once a book is already checked out that condition is `False` and it's skipped, eventually returning `False` at the end of the function once every book has been checked.

**Object-oriented version**

> `Library.check_out_book` still finds the book by title, but only calls `book.check_out()` if `not book.checked_out`. Even if it did call it anyway, `Book.check_out()` checks `self.checked_out` itself and would return `False`, so there's effectively two separate checks happening.

### 4. Adding a new field, e.g. genre

**Procedural version**

> I'd need to add a `"genre": genre` entry into the dictionary everywhere a book gets created, which in this program is just inside `add_book`, but if there were more places in a bigger program where books get built, I'd have to remember to update all of them.

**Object-oriented version**

> I'd just add `self.genre = genre` once inside `Book`'s `__init__` method, and then every book created from then on automatically has a genre without needing to change anywhere else.

## Written reflection

### 1. A genuine OOP advantage, for this specific problem

> The OOP version keeps each book responsible for its own `checked_out` status, so it's harder to accidentally change a book's data from somewhere else in the program by mistake, because you always have to go through the `Book` object's own methods to do it.

### 2. A genuine procedural advantage, for this specific problem

> The procedural version is a bit simpler to read for a program this small. You can see all the logic for checking a book out in one function without needing to understand classes and objects first, which is extra setup that isn't really needed for a program this size.

### 3. Which version would be easier to extend, and why?

> I think the OOP version would be easier to grow, because you could create `DVD` and `Equipment` classes that work similarly to `Book` but with their own extra details, whereas with the procedural version you'd probably end up with a lot of `if item_type == "DVD"` style checks scattered through the same functions, which would get messy fairly quickly once there were multiple branches and item types involved.
