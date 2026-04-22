from pathlib import Path

import pytest

from gentlii_foundations.html_security import UnsafeHtmlError, assert_safe_publish_html


def test_assert_safe_publish_html_accepts_plain_static_markup():
    assert_safe_publish_html("<html><body><h1>Safe</h1><p>Static content</p></body></html>")


def test_assert_safe_publish_html_rejects_active_content_patterns():
    with pytest.raises(UnsafeHtmlError) as exc_info:
        assert_safe_publish_html(
            """
            <html>
              <body onload="alert('xss')">
                <a href="javascript:alert('xss')">Click</a>
                <script>alert('xss')</script>
              </body>
            </html>
            """
        )

    assert "<script" in str(exc_info.value)
    assert "onload=" in str(exc_info.value)
    assert "javascript:" in str(exc_info.value)


def test_assert_safe_publish_html_rejects_embedded_browsing_contexts():
    with pytest.raises(UnsafeHtmlError) as exc_info:
        assert_safe_publish_html("<iframe src='https://example.com'></iframe>")

    assert "<iframe" in str(exc_info.value)

