# contents-search-replace

Replace variable identifiers in a file with a toml map.

This was originally created to reference colors while working on my [starship.toml](https://starship.rs/), but I have since found myself using this barebones script constantly.


### Table of Contents

[Getting Started](#getting-started)\
[Usage](#usage)\
[Example](#example)



## Getting Started

To get started, all you need to do is prefix a variable name from your toml map with `&&`, from within your base file.

An example of this would be if we had a base file that contains

```
&&foo
```

To assign what `&&foo` means, we need to define it in the toml map file.

```toml
foo = "bar"
```

So now, when we run the script with that base file and toml map, we will replace `&&foo` in the base file with `bar`.


## Usage

Clone the repository

```shell
git clone "https://github.com/zettacache/contents-search-replace" "zetta-csr"
```

Run the repository

```
python3 -m zetta-csr [base_file] [toml_map] [output_path]


    [base_file]
        The file which contains the contents you wish to replace.
    
    [toml_map]
        The toml map you wish to apply to the base file.

    [output_path]
        The target path for the outputted file.
```


## Example

Let's assume our current directory looks like this

```
zetta-csr/
base_file.txt
map_file.toml
```

And the contents of our files looks like this

**base_file.txt**
```
Hello, world! I am excited to share &&repo_name.

From,
    &&author
```

**map_file.toml**
```toml
repo_name = "contents-search-replace"
author = "zettacache"
```

After we run the following command

```
python3 -m zetta-csr "base_file.txt" "map_file.toml" "output.txt"
```

We can see that `output.txt` is generated with the contents of

**output.txt**
```
Hello, world! I am excited to share contents-search-replace.

From,
    zettacache
```
