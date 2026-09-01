# Task 7: Open Research Task and Oral Walkthrough, Marking Scheme

Companion to `BRIEF_T7.md` | Module code PRG1

100 marks total, 35% of the module assignment (57 marks, 20%, for the open research task; 43 marks, 15%, for the oral walkthrough). There is no fixed correct answer, starter file, or test suite; your solution is marked against your own stated scope, not a reference implementation.

For each of the eight criteria below, the band whose description best fits your submission is awarded; you do not need to satisfy every sentence in a band to fall into it. Marks across all eight criteria are added for your score out of 100.

## Part 1: Open research task, 57 marks

### Functional correctness (21 marks)

| Band | Descriptor |
|---|---|
| Fail (<40%), 0-8 | Program does not run, or does not correctly compute the time conversion even for your own simplest stated scenario. Core logic is absent or fundamentally broken. |
| Pass (40-59%), 9-12 | Program runs and is correct for straightforward cases matching your stated scope, but fails on some cases within that same scope, or the scope itself is set so narrowly that little has genuinely been solved. |
| Merit (60-69%), 13-14 | Program reliably and correctly computes the time conversion across the range of cases you have defined as in scope, including simple variations such as different location pairs. |
| Distinction (70-79%), 15-16 | Program is correct and robust across your stated scope, and also handles at least one non-trivial case correctly without being explicitly prompted to, for example a case near a boundary condition. |
| Outstanding (80%+), 17-21 | Program is correct, robust, and demonstrably tested against a deliberately chosen range of cases, including edge cases, with evidence in the code, comments, or written note that you actively tried to break your own solution. |

### Edge cases and scope decisions (11 marks)

| Band | Descriptor |
|---|---|
| Fail (<40%), 0-4 | No evidence you considered any case beyond the single simplest example. Scope is undefined, or you cannot describe what your program does and does not handle. |
| Pass (40-59%), 5-6 | Scope is stated, but only the simplest case has genuinely been considered; edge cases such as crossing midnight, crossing a date boundary, or unusual input are not mentioned or are dismissed without reasoning. |
| Merit (60-69%), 7 | At least one genuine edge case has been identified and reasoned about, even if not fully handled in the code, with a plausible explanation of the decision. |
| Distinction (70-79%), 8 | Multiple relevant edge cases are identified and reasoned about, with sensible, explained decisions about which are handled and which are explicitly out of scope. |
| Outstanding (80%+), 9-11 | Edge cases are identified, reasoned about, and the scope decisions demonstrate genuine judgement about what a real version of this tool would need to consider, going beyond the obvious. |

### Code quality (11 marks)

| Band | Descriptor |
|---|---|
| Fail (<40%), 0-4 | Code is very difficult to follow; naming, structure and organisation do not reflect any deliberate design choice appropriate to the size of the problem. |
| Pass (40-59%), 5-6 | Code is readable with effort; naming and structure are present but inconsistent or not well matched to the size and shape of the problem. |
| Merit (60-69%), 7 | Code is clearly organised, with sensible naming and structure appropriate to the size of the problem and the language chosen. |
| Distinction (70-79%), 8 | Code is well organised and easy to follow, with naming, structure and any comments genuinely aiding understanding rather than padding it. |
| Outstanding (80%+), 9-11 | Code quality is professional in standard: clear, appropriately structured, and the choices made (functions, classes, files, or otherwise) are proportionate and well justified for a problem of this size, not over- or under-engineered. |

### Written note (14 marks)

| Band | Descriptor |
|---|---|
| Fail (<40%), 0-5 | Written note is missing, extremely thin, or does not address what was asked (problem interpretation, assumptions, research, reflection). |
| Pass (40-59%), 6-8 | Written note covers the basics required but is generic or superficial; assumptions are stated without reasoning, and research, including any AI use, is mentioned without real detail of what was asked or how the answer was used. |
| Merit (60-69%), 9 | Written note clearly covers problem interpretation, assumptions with reasoning, and research including any AI use, with your own reasoning visible alongside what was found or generated. |
| Distinction (70-79%), 10-11 | Written note is specific and well-reasoned throughout, with clear evidence of independent thought: assumptions are justified, research including AI use is critically evaluated rather than just reported, and you reflect honestly on what you would do differently. |
| Outstanding (80%+), 12-14 | Written note reads as a genuine, reflective account of a real piece of independent problem-solving: assumptions, research and reflection are all specific to this problem, critically engaged with, and demonstrate the kind of judgement this task is designed to assess. |

## Part 2: Oral walkthrough, 43 marks

8 to 10 minutes per student, shortly after submission. Remote, on the module's final (remote) day, or shortly after if you cannot make that day. Recorded, so a marker can revisit a borderline grade and a moderator can review afterwards.

### Explanation of own code (14 marks)

| Band | Descriptor |
|---|---|
| Fail (<40%), 0-5 | Cannot accurately describe what your own code does, or the walkthrough contradicts the actual submission. |
| Pass (40-59%), 6-8 | Can describe what the code does at a surface level, but explanations are vague, hesitant, or rely on reading from notes rather than genuine recall. |
| Merit (60-69%), 9 | Explains the code accurately and in your own words, covering the main logic without significant prompting. |
| Distinction (70-79%), 10-11 | Explains the code accurately, fluently and in detail, including why it is structured the way it is, without relying on notes. |
| Outstanding (80%+), 12-14 | Explains the code with complete fluency and precision, anticipating the marker's likely follow-up questions and addressing them unprompted. |

### Justification of design decisions (11 marks)

| Band | Descriptor |
|---|---|
| Fail (<40%), 0-4 | Cannot explain why any specific decision was made beyond "it worked" or similar. |
| Pass (40-59%), 5-6 | Can offer a reason for at least one design decision, though reasoning may be superficial or offered only after the fact. |
| Merit (60-69%), 7 | Justifies the main design decisions with genuine reasoning, showing they were deliberate choices rather than accidents. |
| Distinction (70-79%), 8 | Justifies design decisions with reasoning that shows awareness of alternatives and why the chosen approach was preferred. |
| Outstanding (80%+), 9-11 | Justifies design decisions with clear, confident reasoning, including honest acknowledgement of trade-offs and what you would reconsider. |

### Response to an on-the-spot change (11 marks)

| Band | Descriptor |
|---|---|
| Fail (<40%), 0-4 | Cannot engage meaningfully with the unseen variation put to you; response is confused, incorrect, or absent. |
| Pass (40-59%), 5-6 | Attempts to reason about the change, but reasoning is shallow, partially incorrect, or requires significant prompting to reach a workable answer. |
| Merit (60-69%), 7 | Reasons through the change correctly with some prompting, identifying broadly what would need to change and why. |
| Distinction (70-79%), 8 | Reasons through the change confidently and mostly independently, identifying specifically what would need to change in your code and why. |
| Outstanding (80%+), 9-11 | Reasons through the change fluently and independently, correctly identifying the specific changes required and any knock-on effects elsewhere in the program. |

### Overall authenticity (7 marks)

| Band | Descriptor |
|---|---|
| Fail (<40%), 0-2 | Responses feel rehearsed, generic, or inconsistent with your actual submission; little confidence you understand your own work. |
| Pass (40-59%), 3 | Responses are broadly consistent with the submission but feel somewhat scripted or uncertain in places. |
| Merit (60-69%), 4 | Responses are consistent with the submission and feel like genuine, if not fully fluent, understanding. |
| Distinction (70-79%), 5 | Responses are consistently genuine and specific to this submission, with no sign of a rehearsed or generic account. |
| Outstanding (80%+), 6-7 | Responses are unmistakably genuine throughout, reflecting deep, first-hand familiarity with every part of the submission. |

### What kinds of questions to expect

Questions are adapted to your own submission, not read from a fixed script. Expect a mix of:

- **Comprehension**, e.g. "Talk me through what happens when this program runs, from the top." "Where does the actual time conversion happen?"
- **Justification**, e.g. "Why did you take the input this way rather than another way?" "What would you do differently starting again?"
- **On-the-spot adaptation**, e.g. "How would this need to change to support a third location?" "What happens if a user enters a time zone that doesn't exist?"
- **AI-use follow-up**, where relevant, e.g. "What did you ask it, and how did you check what it gave you back was right?"

## AI-use evidence

Assessed directly here, as part of the written note (up to 14 marks, above) and possibly the oral walkthrough, unlike other tasks. This is separate from the whole-assignment `PRG1_AI_Use_Reflection`, which is not marked.
