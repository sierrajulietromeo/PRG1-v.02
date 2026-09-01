# Task 7: Open Research Task, Written Note

Complete this alongside `BRIEF_T7.md`.

### What you understood the problem to require

> I understood it as needing to take a time the user gives me for their own city, and work out what the time would be in a different city at that same moment, using the difference in time zones between the two.

### Assumptions you made, and why

> I assumed the user would type the time in 24-hour format like 14:30 rather than allowing for am/pm, mainly because it's simpler to parse and avoids extra work checking for "am"/"pm" text. I also assumed I only need to support a fixed list of cities rather than every city in the world, since building or finding a complete list of every time zone felt like far more than this task needed. I did not account for daylight saving time changes; I used fixed offsets, because working out exactly when DST starts and ends in different countries seemed like a lot of extra complexity for the size of this task, so I've flagged it as a known limitation instead.

### What you researched, and where, including any AI tool use

> I looked up the actual UTC offsets for the cities I picked using a search engine, to make sure they were accurate. I also asked an AI tool how to handle a time going past midnight or before 00:00 when you add or subtract hours, because my first attempt was giving me answers like 25:30 or -2:15, which obviously aren't real times. It suggested converting everything into total minutes and using the modulo operator to wrap the result back into a normal 24-hour range, which is the approach I used in `convert_time`. I tested it myself afterwards with a few times close to midnight to check it actually worked correctly before trusting it, rather than assuming it was right just because it sounded confident.

### What you would do differently with more time

> I would look at using a proper time zone library instead of my own fixed-offset dictionary, since that would handle daylight saving time correctly and support far more cities without me having to hardcode them all in by hand. I would also add proper handling for when the user types the time in the wrong format, since right now it would just crash rather than giving a helpful message. I'd also want to make it clear to the user when the converted time falls on a different day, since my program doesn't currently say that.
