import pytest

# Simple Strings
class TestSimpleString:
    # Serialize tests
    def test_serialize_simple_string(self):
        assert serialize_simple_string("OK") == b"+OK\r\n"

    def test_serialize_simple_string_empty(self):
        assert serialize_simple_string_empty("") == b"+\r\n"

    def test_serialize_simple_string_invalid_input():
        with pytest.raises(TypeError):
            serialize_simple_string(123)

    # Parse tests

    def test_parse_simple_string(self):
        assert parse_simple_string(b"+OK\r\n") == "O

    def test_parse_simple_string_empty(self):
        assert parse_simple_string_empty(b"+\r\n") == ""

    def test_parse_simple_string_invalid_prefix():
        with pytest.raises(ValueError):
            parse_simple_string(b"-OK\r\n")

# Bulk Strings
class TestBulkStrings:

#Serialize tests
    def test_serialize_bulk_string(self):
        assert serialize_bulk_string("hello world") == b"$11\r\nhello world\r\n"

    def test_serialize_bulk_string_empty(self):
        assert serialize_bulk_string_empty("") == b"$0\r\n\r\n"

    def test_serialize_bulk_string_null(self):
        assert serialize_bulk_string_null(None) == b"$-1\r\n"

    def test_serialize_bulk_string_invalid_input():
        with pytest.raises(TypeError):
            serialize_bulk_string(123)

#Parse tests
    def test_parse_bulk_string(self):
        assert parse_bulk_string(b"$11\r\nhello world\r\n") == "hello world"

    def test_parse_bulk_string_empty(self):
        assert parse_bulk_string_empty(b"$0\r\n\r\n") == ""

    def test_parse_bulk_string_null(self):
        assert parse_bulk_string_null(b"$-1\r\n") is None

    def test_parse_bulk_string_invalid_prefix():
        with pytest.raises(ValueError):
            parse_bulk_string(b"+hello world\r\n")


# Array Tests
class TestArrays:
    # Serialize tests
    def test_serialize_array(self):
        assert serialize_array(["echo", "hello world"]) == b"*2\r\n$4\r\necho\r\n$11\r\nhello world\r\n"

    def test_serialize_array_empty(self):
        assert serialize_array([]) == b"*0\r\n"

    def test_serialize_array_null(self):
        assert serialize_array(None) == b"*-1\r\n"


    def test_serialize_invalid_array(self):
        with pytest.raises(TypeError):
            serialize_simple_string(123)

    # Parse tests
    def test_parse_array(self):
        assert parse_array(b"*2\r\n$4\r\necho\r\n$11\r\nhello world\r\n") == ["echo", "hello world"]

    def test_parse_array_empty(self):
        assert parse_array(b"*0\r\n") == []

    def test_parse_array_null(self):
        assert parse_array(b"*-1\r\n") is None

#Integer Tests
class TestInteger:
    def test_serialize_integer(self):
        assert serialize_integer(1000) == b":1000\r\n"

    def test_parse_integer(self):
        assert parse_integer(b":1000\r\n") == 1000

    def test_serialize_integer_negative(self):
        assert serialize_integer(-1000) == b":-1000\r\n"

    def test_parse_integer_negative(self):
        assert parse_integer(b":-1000\r\n") == -1000

    def test_serialize_integer_zero(self):
        assert serialize_integer(0) == b":0\r\n"

    def test_parse_integer_zero(self):
        assert parse_integer(b":0\r\n") == 0



