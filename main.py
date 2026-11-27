#!/usr/bin/env python3
"""make.fun bounty entry: Funniest Autocorrect Fail.

Autocorrect meant well. It corrected one word, and in doing so
ruined a perfectly good message — in one line.
"""

FAIL = "I texted my boss 'great job on the launch' and autocorrect sent 'great job on the lunch' — so now I am in charge of catering, and the launch is still waiting."


def fail():
    """Return the funniest autocorrect fail."""
    return FAIL


def main():
    print(fail())


if __name__ == "__main__":
    main()
