# Mac Commands

Curated list of commands to make my work/life more productive using my Mac.

## Search files and directories

### find

Search all files with extension `png`.

```bash
find $(pwd) -type f -name '*.png'
```

Search and rename (replace `-` with `_`)

```bash
find $d -depth -name '*-*.png' \
  -execdir bash -c 'mv -- "$1" "${1//-/_}"' bash {} \;
```

Search and iterate through using a `while`

```bash
find $(pwd) -type f -name '*.png' -print0 |
  while IFS= read -r -d '' file; do
    java -jar plantuml.1.2019.5.jar -encodesprite 16z $file > "${file%.*}.puml"
  done
```

### Count elements

wc. Print byte, word, and line counts, count the number of bytes, whitespace-separated words, and newlines in each given FILE, or standard input if none are ...


```bash
total=$(find $(pwd) -type f -name '*.png' | wc -l)
```

```bash
echo "1\n2\n3\n" | wc -l
```

`"${file%.*}.puml"` creates a new files with extension `puml` without having to use `mv` or `rename`.

## Shortcuts

| Key/Command | Description                                                 |
|-------------|-------------------------------------------------------------|
| Tab         | Auto-complete files and folder names                        |
| Ctrl + A    | Go to the beginning of the line you are currently typing on |
| Ctrl + E    | Go to the end of the line you are currently typing on       |
| Ctrl + U    | Clear the line before the cursor                            |
| Ctrl + K    | Clear the line after the cursor                             |
| Ctrl + W    | Delete the word before the cursor                           |
| Ctrl + T    | Swap the last two characters before the cursor              |
| Esc + T     | Swap the last two words before the cursor                   |
| Ctrl + R    | Lets you search through previously used commands            |
| Ctrl + L or Command + K | Clears the Screen                               |
| Ctrl + C    | Kill whatever you are running                               |
| Ctrl + D    | Exit the current shell                                      |

## Core commands

| Key/Command    | Description                                                                  |
|----------------|------------------------------------------------------------------------------|
| cd             | Home directory                                                               |
| cd [folder]    | Change directory                                                             |
| cd ~           | Home directory, e.g. 'cd ~/folder/'                                          |
| cd /           | Root of drive                                                                |
| ls             | Short listing                                                                |
| ls -l          | Long listing                                                                 |
| ls -a          | Listing incl. hidden files                                                   |
| ls -lh         | Long listing with Human readable file sizes                                  |
| ls -R          | Entire content of folder recursively                                         |
| sudo [command] | Run command with the security privileges of the superuser (Super User DO) |
| open [file]    | Opens a file                                                                 |
| open .         | Opens the directory                                                          |
| top            | Displays active processes. Press q to quit                                   |
| nano [file]    | Opens the Terminal it's editor                                               |
| pico [file]    | Opens the Terminal it's editor                                               |
| q              | Exit                                                                         |
| clear          | Clear screen                                                                 |

## Environment

| Key/Command | Description                 | Example                            |
|-------------|-----------------------------|------------------------------------|
| printenv    | Print environment variables | printenv [OPTION]... [VARIABLE]... |

## Command History

| Key/Command | Description                                                    |
|-------------|----------------------------------------------------------------|
| history n   | Shows the stuff typed - add a number to limit the last n items |
| ctrl-r      | Interactively search through previously typed commands         |
| ![value]    | Execute the last command typed that starts with 'value'        |
| !!          | Execute the last command typed                                 |

## File Management

| Key/Command              | Description                          |
|--------------------------|--------------------------------------|
| touch [file]             | Create new file                      |
| pwd                      | Full path to working directory       |
| ..                       | Parent/enclosing directory, e.g.     |
| ls -l ..                 | Long listing of parent directory     |
| cd ../../                | Move 2 levels up                     |
| .                        | Current folder                       |
| cat                      | Concatenate to screen                |
| rm [file]                | Remove a file, e.g. rm [file] [file] |
| rm -i [file]             | Remove with confirmation             |
| rm -r [dir]              | Remove a directory and contents      |
| rm -f [file]             | Force removal without confirmation   |
| rm -i [file]             | Will display prompt before           |
| cp [file] [newfile]      | Copy file to file                    |
| cp [file] [dir]          | Copy file to directory               |
| mv [file] [new filename] | Move/Rename, e.g. mv -v [file] [dir] |

## DIRECTORY MANAGEMENT

| Key/Command          | Description                                             |
|----------------------|---------------------------------------------------------|
| mkdir [dir]          | Create new directory                                    |
| mkdir -p [dir]/[dir] | Create nested directories                               |
| rmdir [dir]          | Remove directory ( only operates on empty directories ) |
| rm -R [dir]          | Remove directory and contents                           |

## Pipes

Allows to combine multiple commands that generate output

| Key/Command | Description                                               |
|-------------|-----------------------------------------------------------|
| more        | Output content delivered in screensize chunks             |
| > [file]    | Push output to file, keep in mind it will get overwritten |
| >> [file]   | Append output to existing file                            |
| <           | Tell command to read content from a fi                    |

## Help

| Key/Command      | Description                               |
|------------------|-------------------------------------------|
| [command] -h     | Offers help                               |
| [command] --help | Offers help                               |
| [command] help   | Offers help                               |
| reset            | Resets the terminal display               |
| man [command]    | Show the help for 'command'               |
| whatis [command] | Gives a one-line description of 'command' |

## Compress and uncompress files and folders

### Zip

| Key/Command                                    | Description |
|------------------------------------------------|-------------|
| zip -r archive_name.zip `<folder_to_compress>` | To compress |
| unzip archive_name.zip                         | To extract  |

Exclude `_MACOSX` or `._Filename` and .ds store files, use the “-X” option

`zip -r -X archive_name.zip folder_to_compress`

### TAR.GZ

Note: Where `.` is the folder

| Key/Command                    | Description |
|--------------------------------|-------------|
|tar -zcvf archive_name.tar.gz . | To compress |
| tar -zxvf archive_name.tar.gz  | To extract  |

### TAR.BZ2

Better compression than both tar.gz and zip.

| Key/Command                                       | Description |
|---------------------------------------------------|-------------|
| tar -jcvf archive_name.tar.bz2 folder_to_compress | To compress |
| tar -jxvf archive_name.tar.bz2                    | To extract  |

## cURL

```bash
bash: curl [options...] <url>
```

see: [cURL guide](/curl)

## Processes

### List all Linux/OSX processes

```bash
bash$ ps -ef -A

  UID   PID  PPID   C STIME   TTY           TIME CMD
    0     1     0   0 31Jul18 ??        50:13.64 /sbin/launchd
...
```

```bash
bash$ ps -ef | grep node
```

```bash
bash$ kill 1111
```
