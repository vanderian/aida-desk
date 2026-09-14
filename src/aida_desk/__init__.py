"""aida desk — the client's page, served by their own tenant at `/`.

One static page, plain HTML and JS, calling the tenant's `/api/v1/…` on
its own origin: sign in with the admin key and your name, then
conversation, memory review and ratification, sources, monitoring. It is
also the reference client: what the page does is what an integration
does, against the same OpenAPI spec the tenant serves at
`/api/v1/openapi.json`.

The package holds nothing but the page and the spec; postbox serves the
page, this repository publishes it.
"""

from importlib.metadata import version as _installed_version
from pathlib import Path

__version__ = _installed_version("aida-desk")


def page() -> bytes:
    return (Path(__file__).parent / "app.html").read_bytes()
