# Task 2: Debugging, Part A, Answers

Complete this alongside `BRIEF_T2.md`.

## Fault log

### Fault 1

**What was wrong, and where**

> In `check_pin`, the condition was `if attempt != correct_pin: return True`, so the `!=` and `==` were the wrong way round.

**Why it caused incorrect behaviour, and how you fixed it**

> This meant entering the correct PIN returned `False` and entering a wrong PIN returned `True`, so the checker was doing the exact opposite of what it should. I fixed it by changing `!=` to `==` so it returns `True` when the attempt actually matches.

### Fault 2

**What was wrong, and where**

> The loop condition was `while attempts_made <= MAX_ATTEMPTS`.

**Why it caused incorrect behaviour, and how you fixed it**

> Because `attempts_made` starts at 0, using `<=` let the loop run one extra time, so the user actually got 4 attempts instead of 3. I changed it to `<` so the loop stops once 3 attempts have been used.

### Fault 3

**What was wrong, and where**

> There was nothing to stop the loop once the correct PIN had been entered, so it kept asking for more PINs even after printing "Access granted.", and it still printed "Account locked." at the very end regardless.

**Why it caused incorrect behaviour, and how you fixed it**

> The program never actually stopped after a correct entry, so it looked like it granted access but then locked you out anyway. I added an `access_granted` flag that gets set to `True` and a `break` when the PIN is correct, then only print "Account locked." if that flag is still `False` after the loop finishes.
