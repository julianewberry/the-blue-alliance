from google.appengine.api.validation import ValidationError as ValidationError
from google.appengine.datastore.datastore_index import Index as Index, IndexDefinitions as IndexDefinitions, Property as Property
from typing import Any

MISSING_KIND: str
BAD_DIRECTION: str
BAD_MODE: str
NAME_MISSING: str
MODE_AND_DIRECTION_SPECIFIED: str
MODE_AND_ANCESTOR_SPECIFIED: str

def IndexesXmlToIndexDefinitions(xml_str): ...
def IsAutoGenerated(xml_str): ...

class IndexesXmlParser:
    indexes: Any
    errors: Any
    def Parse(self, xml_str): ...
    def ProcessIndexNode(self, node) -> None: ...
