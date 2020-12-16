# bookpam

BookPam is a typesetting system; it includes features designed for the production of technical documentation and book.
BookPam is available as free software.

## Features

- Support cover of book
- Auto generate Contents list
- Auto generator to HTML documents (with minimal style for title, block, etc.)
- Highlight one own language syntaxe
- Auto generate Functions list at bottom of book

### Examples

Watch web and html-based book at [here](https://basemax.github.io/bookpam/examples.html)

Pure pam file format avaiable at [here](examples.pam)

```
[cover]

[center]





{logo.png}




### GitHub Universe 2020 event

# Discussion about programming and a new tool



David Nolen
 
Maintainer of Clojurescript 



Jonan Scheffler

Director of Developer Relations, New Relic 



Spring 2020


Max Base, GitHub Repository

[/center]


[/cover]


[page]

# Lorem Ipsum

Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for previewing layouts and visual mockups.

....
....
....

[/page]
```

### Commands

- [center] [/center]
- [page] [/page]
- `#` `##` `###` `####` `#####` `######`
- `\n`: go to new line

# TODO

- Support RTL and LTR (`html[dir=rtl]{}`, `html[dir=ltr]{}`)
- Ability to set own font for book (Optional)
- Highlight multi language code syntaxes

---------

# Max Base

My nickname is Max, Programming language developer, Full-stack programmer. I love computer scientists, researchers, and compilers. ([Max Base](https://maxbase.org/))

## Asrez Team

A team includes some programmer, developer, designer, researcher(s) especially Max Base.

[Asrez Team](https://www.asrez.com/)
