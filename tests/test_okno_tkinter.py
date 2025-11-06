import pytest


# Ustaw backend bezokienkowy zanim zaimportujemy moduł aplikacji
import matplotlib

matplotlib.use("Agg", force=True)

from okno_tkinter import TkinterApp


@pytest.fixture()
def app():
    instance = TkinterApp()
    yield instance
    # Sprzątanie po testach: zamknij okno, zwolnij zasoby
    try:
        instance.root.destroy()
    except Exception:
        pass


def test_app_initializes(app):
    assert app.root is not None
    assert app.frame is not None
    assert app.label is not None
    assert app.figure is not None
    assert app.axis is not None
    assert app.canvas_widget is not None
    assert app.zamknij_btn is not None


def test_label_properties(app):
    assert app.label.cget("text") == "Witaj w Tkinter!"
    assert app.label.cget("fg") == "red"


def test_chart_has_line_and_legend(app):
    lines = app.axis.get_lines()
    assert len(lines) >= 1
    assert lines[0].get_label() == "y = x^2"


