from pathlib import Path
import tinycss2

CSS_FILE = Path('style.css')

def load_css():
    assert CSS_FILE.exists(), f"{CSS_FILE} css file does not exist"
    return CSS_FILE.read_text(encoding='utf-8')

def test_css_file_is_not_empty():
    css = load_css()
    assert css.strip(), "CSS file is empty"


def test_css_syntax():
    css = load_css()
    rules = tinycss2.parse_stylesheet(
        css,
        skip_comments=True,
        skip_whitespace=True
    )
    errors = [
        rule for rule in rules
        if rule.type == "error"
    ]

    assert not errors, "\n".join(
        f"CSS syntax error: {error.message}"
        for error in errors
    )


def test_css_declarations():
    css = load_css()

    rules = tinycss2.parse_stylesheet(
        css,
        skip_comments=True,
        skip_whitespace=True
    )

    errors = []

    for rule in rules:
        if rule.type == "qualified-rule":
            declarations = tinycss2.parse_declaration_list(
                rule.content,
                skip_comments=True,
                skip_whitespace=True
            )

            for declaration in declarations:
                if declaration.type == "error":
                    errors.append(declaration.message)

    assert not errors, "\n".join(errors)


def test_required_css_properties():
    css = load_css()

    assert "background-color" in css
    assert "font-size" in css
    assert "color" in css








