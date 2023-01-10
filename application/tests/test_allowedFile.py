ALLOWED_EXTENSIONS={'png','jpg','jpeg'}

def allowed_file(filename):
    namelist=filename.split('.')
    if len(namelist)==2:
        return(namelist[1] in ALLOWED_EXTENSIONS)
    return(False)

def test_allowed_file():
    assert(allowed_file('picture.png')==True)
    assert(allowed_file('picture.jpg')==True)
    assert(allowed_file('picture.jpeg')==True)
    assert(allowed_file('picture.jqsdpj')==False)
    assert(allowed_file('picture')==False)
    assert(allowed_file('picture.')==False)
    assert(allowed_file('pic.ture.jpeg')==False)
    assert(allowed_file('ù*+-*(_çàjls*ù^ù')==False)
    assert(allowed_file('')==False)
    assert(allowed_file('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.jpg')==True)