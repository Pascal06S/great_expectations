from __future__ import annotations

from great_expectations_v1.exceptions import GreatExpectationsTypeError


class InvalidRenderedContentError(GreatExpectationsTypeError):
    pass


class InlineRendererError(GreatExpectationsTypeError):
    pass


class RendererConfigurationError(GreatExpectationsTypeError):
    pass