# My bin folder

Collection of scripts and tools that I made.

## readmd

A script to use your default browser to read Markdown files.

### Requirements

- `pandoc`

### Installation

Download and allow execution of [readmd](readmd) in your `$PATH`.

To use it as your default Markdown reader create the file `~/.local/share/applications/readmd.desktop` with these contents:

```desktop
[Desktop Entry]
Encoding=UTF-8
Version=1.0
Type=Application
NoDisplay=true
Exec=readmd %f
Name=readmd
Comment=Read Markdown files in browser.
```

Then run `echo "text/markdown=readmd.desktop;" >> ~/.config/mimeapps.list`.

### Usage

readmd can read from the file presented in an argument or stdin.

```Shell
$ readmd [FILE]
```

or

```Shell
$ somecommand | readmd
```
