from other_code.input import due, submitted, latePenalty

def test_fileType(grade = 100):
    if(submitted > due):
        grade = grade * latePenalty
    assert submitted > due
