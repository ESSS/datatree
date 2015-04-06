


def test_json():
    from datatree import Tree

    tree = Tree()
    with tree.author() as author:
        author.name('Terry Pratchett')
        author.genre('Fantasy/Comedy')
        author // 'Only 2 books listed'
        with author.novels(count=2) as novels:
            novels.novel('Small Gods', year=1992)
            novels.novel('The Fifth Elephant', year=1999)
            novels.novel("Guards! Guards!", year=1989)

    assert tree.render('json', pretty=True, sort_keys=True) == '''{
    "author": {
        "genre": "Fantasy/Comedy",\b
        "name": "Terry Pratchett",\b
        "novels": [
            "Small Gods",\b
            "The Fifth Elephant",\b
            "Guards! Guards!"
        ]
    }
}'''.replace('\b', ' ')
