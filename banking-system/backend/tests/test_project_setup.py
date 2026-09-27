from banking_system import __version__


def test_project_imports() -> None:
    assert isinstance(__version__, str)
