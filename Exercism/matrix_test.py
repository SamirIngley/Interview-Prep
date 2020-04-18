from matrix import Matrix_Rows_Columns

def test_correct_IO_datatype():
    input = '9 8 7\n5 3 2\n6 6 7'

    mat = Matrix_Rows_Columns(input)
    mat.rows()
    mat.columns()


def test_diff_length():
    new_input = '9 8 0 9\n5 3 2 9\n6 6 8 9'

    mat = Matrix_Rows_Columns(new_input)
    mat.rows()
    mat.columns()

if __name__ == "__main__":
    test_correct_IO_datatype()
    test_diff_length()    