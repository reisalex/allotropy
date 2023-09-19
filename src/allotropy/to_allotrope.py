import io
from pathlib import Path
from typing import Any

from allotropy.allotrope.allotrope import serialize_allotrope
from allotropy.parser_factory import PARSER_FACTORY, VendorType


def allotrope_from_io(
    contents: io.IOBase, filename: str, vendor_type: VendorType
) -> dict[str, Any]:
    parser = PARSER_FACTORY.create(vendor_type)
    return serialize_allotrope(parser.to_allotrope(contents, filename))


def allotrope_from_file(filepath: str, vendor_type: VendorType) -> dict[str, Any]:
    with open(filepath, "rb") as f:
        return allotrope_from_io(f, Path(filepath).name, vendor_type)