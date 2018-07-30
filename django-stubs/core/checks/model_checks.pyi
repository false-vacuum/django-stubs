# Stubs for django.core.checks.model_checks (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

from django.apps.registry import Apps
from django.core.checks.messages import Error, Warning
from typing import Any, List, Optional, Set, Tuple

def check_all_models(app_configs: None = ..., **kwargs: Any) -> List[Warning]: ...
def _check_lazy_references(
    apps: Apps, ignore: Optional[Set[Tuple[str, str]]] = ...
) -> List[Error]: ...
def check_lazy_references(app_configs: None = ..., **kwargs: Any) -> List[Any]: ...