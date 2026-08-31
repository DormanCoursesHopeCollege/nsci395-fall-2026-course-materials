# Debugging checklist

## First state the mismatch

- What did you expect?
- What happened instead?
- Is this a Python error, a stale-notebook problem, or a scientifically wrong result?

## For a traceback

1. Read the final line.
2. Find the named cell and line.
3. Inspect the names on that line.
4. Check spelling, type, value, unit, and shape.
5. Test a smaller case.
6. Change one thing and run again.

## For code that runs but gives a suspicious answer

- Check units.
- Check inclusive and exclusive boundaries.
- Check which axis was averaged.
- Check whether a loop accumulates or overwrites.
- Check whether training and test data were separated before fitting.
- Check whether old output came from a previous variable value.
- Compare with a known-answer case or baseline.

## Before asking for help

Bring:

- the smallest relevant cell;
- the exact error or wrong output;
- the expected result;
- one or two things you tried.

## Before submission

Restart the kernel and run all cells. A notebook that works only because of hidden state is not reproducible.
