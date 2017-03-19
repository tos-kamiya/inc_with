# inc_with

Run command with giving parameters incrementally.

Make an interactive session of the given command line. In the session,
you can give parameters to the command line in an incremental way,
that is, every time you type a character, the command line executed repeatedly.
To quit the session, type `[ESC]`.

Usage: inc_with COMMAND

## Sample Usage

Make [ripgrep](https://github.com/BurntSushi/ripgrep) an incremental text search tool.

```sh
$ inc_with rg -m 200
```

Here, `rg`'s option `-m 200` specifies an upper limit of results (lines).

## Installation

Run `sudo python3 setup.py install`. A script `inc_with` will be copied in a directory
for executables, such as `/usr/local/bin/`.

## License

Public Domain.
