from typing import Literal

from europarser.models import OutputType

MimeType = Literal["text/csv", "application/json", "text/plain", "text/xml"]


def get_mimetype(output_type: OutputType) -> MimeType:
    if output_type == "csv":
        return "text/csv"
    elif output_type == "json":
        return "application/json"
    elif output_type == "txt":
        return "text/plain"
    elif output_type == "xml":
        return "text/xml"
