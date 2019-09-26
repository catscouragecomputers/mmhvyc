from other_code.input import acceptedFileTypes, attachedFile

def test_fileType():
    assert [ele for ele in acceptedFileTypes if(ele in attachedFile)]
