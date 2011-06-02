DataTree
========

_This project is a work in progress and not ready for use yet._

Summary
-------
DataTree is a DSL for creating structured documents in python inspired by Rubys 
Builder, but supporting many structured output formats (planned).

Example
-------
A small example: 

	from datatree import Node

    author = Node('author')
    author.name('Terry Pratchett')
    author.genre('Fantasy/Comedy')
    author // "Only 2 books listed"
    with author.novels(count=2) as novels:
        novels.novel('Small Gods', year=1992)
        novels.novel('The Fifth Elephant', year=1999)

    print author.render() 

Which produces the XML:

    <author>
        <name>Terry Pratchett</name>
        <genre>Fantasy/Comedy</genre>
        <!-- Only 2 books listed -->
        <novels count="2">
            <novel year="1992">Small Gods</novel>
            <novel year="1999">The Fifth Elephant</novel>
        </novels>
    </author>

Or the JSON:

    {
        "author": {
            "name": "Terry Pratchett", 
            "genre": "Fantasy/Comedy", 
            "novels": [
                "Small Gods", 
                "The Fifth Elephant"
            ]
        }
    }

Or the YAML:

    author:
      genre: Fantasy/Comedy
      name: Terry Pratchett
      novels: [Small Gods, The Fifth Elephant]


License
-------
This work is licensed under the Creative Commons Attribution 3.0 Unported 
License. You can view a copy of this license [here][license].

[license]: http://creativecommons.org/licenses/by/3.0/ "Creative Commons Attribution 3.0 Unported License"