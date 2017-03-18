# inc_with

Run command with giving parameters incrementally.

Make an interactive session of the given command line. In the session,
you can give parameters to the command line in an incremental way,
that is, every time you type a character, the command line executed repeatedly.
To quit the session, type `[ESC]`.

Usage:
  inc_with [-u] COMMAND

Option:
  -u    Exec command with `unbuffer` to avoid losing ansi escape sequence.

## License

Public Domain.
