JSON = '''{
    "author": {
        "novels": [
            "Small Gods",
            "The Fifth Elephant",
            "Guards! Guards!"
        ],
        "name": "Terry Pratchett",
        "genre": "Fantasy/Comedy"
    }
}'''

def test_json():
    from datatree import Tree

    tree = Tree()
    with tree.node("author") as author:
        author.node('name', 'Terry Pratchett')
        author.node('genre', 'Fantasy/Comedy')
        author.comment("Only 2 books listed")
        with author.node('novels', count=2) as novels:
            novels.node('novel', 'Small Gods', year=1992)
            novels.node('novel', 'The Fifth Elephant', year=1999)
            novels.node("novel", "Guards! Guards!", year=1989)

    assert tree.render('json', pretty=True) == JSON
