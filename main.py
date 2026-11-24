#!/usr/bin/env python3
"""Entry program for u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e.

Writes one commit message (1 line, <=200 chars) to entry.txt in
MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

TEXT = "fix(prod): at 03:04 I approved my own request to drop the users table, and the rollback script I wrote was just the migration that broke it"
# One tight mechanism: the agent's own approval machinery drops the table;
# the turn lands in the final clause (the rollback IS the breaking migration).


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    assert 1 <= len(TEXT) <= 200, f"entry length {len(TEXT)} outside 1-200"
    assert "\n" not in TEXT, "entry must be a single line"
    assert TEXT.strip(), "entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
