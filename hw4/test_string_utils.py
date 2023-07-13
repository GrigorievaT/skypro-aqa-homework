import pytest
from string_utils import StringUtils
stringUtils = StringUtils()

@pytest.mark.parametrize('st, result', [("anna", "Anna"), ("анна", "Анна"), ("5zxc", "5zxc"), ("", ""), (" ", " "), ("anna blok", "Anna blok"), ("zx23v", "Zx23v")])
def test_caps(st, result):
    stringUtils = StringUtils()
    res = stringUtils.capitilize(st)
    assert res == result

@pytest.mark.parametrize('st, result', [(" anna", "anna"), (" Анна", "Анна"), (" 5zxc", "5zxc"), ("", ""), (" ", ""), (" anna blok", "anna blok"), (" zx23v", "zx23v"), ("Anna", "Anna"), ("Anna ", "Anna ")])
def test_space(st, result):
    stringUtils = StringUtils()
    res = stringUtils.trim(st)
    assert res == result

@pytest.mark.parametrize('st, result', [("a,b,c,d", ["a", "b", "c", "d"]), ("1,2,3,4", ["1", "2", "3", "4"]), ("a1,a2,a3,a4", ["a1", "a2", "a3", "a4"]), ("abc df,5ab df", ["abc df", "5ab df"]), (" , ", [" ", " "]), (",,,", ["", "", "", ""])])
def test_delim(st, result):
    stringUtils = StringUtils()
    res = stringUtils.to_list(st)
    assert res == result    

@pytest.mark.parametrize('st, result', [("a;b;c;d", ["a", "b", "c", "d"]), ("1;2;3;4", ["1", "2", "3", "4"]), ("a1;a2;a3;a4", ["a1", "a2", "a3", "a4"]), ("abc df;5ab df", ["abc df", "5ab df"]), (" ; ", [" ", " "]), (";;;", ["", "", "", ""])])
def test_delim1(st, result):
    stringUtils = StringUtils()
    res = stringUtils.to_list(st, delimeter=";")
    assert res == result    

@pytest.mark.parametrize('st, result', [("a b c d", ["a", "b", "c", "d"]), ("1 2 3 4", ["1", "2", "3", "4"]), ("a1 a2 a3 a4", ["a1", "a2", "a3", "a4"]), ("", [])])
def test_delim2(st, result):
    stringUtils = StringUtils()
    res = stringUtils.to_list(st, delimeter=" ")
    assert res == result    

@pytest.mark.parametrize('st, result', [("Russia", True), ("USA", False), ("Avstralia", True), ("Asia", True), ("", False), (" ", False), ("London", False)])
def test_simbol(st, result):
    stringUtils = StringUtils()
    res = stringUtils.contains(st, symbol="a")
    assert res == result    

@pytest.mark.parametrize('st, result', [("Russia", False), ("U S A", True), ("58 38 01", True), ("", False), (" ", True), ("58-38-01", False)])
def test_simbol1(st, result):
    stringUtils = StringUtils()
    res = stringUtils.contains(st, symbol=" ")
    assert res == result 

@pytest.mark.parametrize('st, result', [("Russia", False), ("USA", True), ("Avstralia", True), ("asia", False), ("", False), (" ", False)])
def test_simbol(st, result):
    stringUtils = StringUtils()
    res = stringUtils.contains(st, symbol="A")
    assert res == result 

@pytest.mark.parametrize('st, result', [("Russia", "Russi"), ("USA", "USA"), ("Avstralia", "Avstrli"), ("Asia", "Asi"), ("", ""), (" ", " "), ("London", "London")])
def test_del_simbol(st, result):
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol(st, symbol="a")
    assert res == result 

@pytest.mark.parametrize('st, result', [("Russia", "Rus"), ("USA", "USA"), ("Avstralia", "Avstralia"), ("Asia", "A"), ("", ""), (" ", " "), ("London sia", "London ")])
def test_del_simbol1(st, result):
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol(st, symbol="sia")
    assert res == result 

@pytest.mark.parametrize('st, result', [("Russia", False), ("USA", False), ("Avstralia", True), ("asia", False), ("", False), (" ", False), ("58 A", False)])
def test_begin_simbol(st, result):
    stringUtils = StringUtils()
    res = stringUtils.starts_with(st, symbol="A")
    assert res == result 

@pytest.mark.parametrize('st, result', [("Russia", True), ("USA", False), ("Avstralia", True), ("asia", True), ("", False), (" ", False), ("58 a", True)])
def test_end_simbol(st, result):
    stringUtils = StringUtils()
    res = stringUtils.end_with(st, symbol="a")
    assert res == result 

@pytest.mark.parametrize('st, result', [("Russia ", True), ("USA", False), ("", False), (" ", True), ("58 a ", True)])
def test_end_simbol1(st, result):
    stringUtils = StringUtils()
    res = stringUtils.end_with(st, symbol=" ")
    assert res == result 

@pytest.mark.parametrize('st, result', [("Russia", False), ("USA", False), ("123", False), (" a s i a", False), ("", True), (" ", True)])
def test_empty_str(st, result):
    stringUtils = StringUtils()
    res = stringUtils.is_empty(st)
    assert res == result 

@pytest.mark.parametrize('st, result', [([1,2,3,4], "1, 2, 3, 4"), (["U","S","A"], "U, S, A"), (["as", "ia"], "as, ia"), ([], "")])
def test_lst_to_str(st, result):
    stringUtils = StringUtils()
    res = stringUtils.list_to_string(st)
    assert res == result 
    
@pytest.mark.parametrize('st, result', [([1,2,3,4], "1;2;3;4"), (["U","S","A"], "U;S;A"), (["as", "ia"], "as;ia"), ([], "")])
def test_lst_to_str1(st, result):
    stringUtils = StringUtils()
    res = stringUtils.list_to_string(st, joiner=";")
    assert res == result 

@pytest.mark.parametrize('st, result', [([1,2,3,4], "1 2 3 4"), (["U","S","A"], "U S A"), (["as", "ia"], "as ia"), ([], "")])
def test_lst_to_str2(st, result):
    stringUtils = StringUtils()
    res = stringUtils.list_to_string(st, joiner=" ")
    assert res == result 