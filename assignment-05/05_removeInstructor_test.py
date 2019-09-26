from other_code.input import instructors

def test_removeInstructors(instructor = 'goggins'):
    assert instructor in instructors
    if(instructor in instructors):
        instructors.remove(instructor)
