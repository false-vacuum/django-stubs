import threading
from collections.abc import Callable, Iterable
from typing import Any, TypeVar

from django.db.models.base import Model

from .config import AppConfig

ModelType = type[TypeVar("ModelType", bound=Model)]

class Apps:
    all_models: dict[str, dict[str, type[Model]]]
    app_configs: dict[str, AppConfig]
    stored_app_configs: list[Any]
    apps_ready: bool
    ready_event: threading.Event
    loading: bool
    _pending_operations: dict[tuple[str, str], list]
    models_ready: bool
    ready: bool
    def __init__(self, installed_apps: Iterable[AppConfig | str] | None = ...) -> None: ...
    def populate(self, installed_apps: Iterable[AppConfig | str] = ...) -> None: ...
    def check_apps_ready(self) -> None: ...
    def check_models_ready(self) -> None: ...
    def get_app_configs(self) -> Iterable[AppConfig]: ...
    def get_app_config(self, app_label: str) -> AppConfig: ...
    # it's not possible to support it in plugin properly now
    def get_models(self, include_auto_created: bool = ..., include_swapped: bool = ...) -> list[type[Model]]: ...
    def get_model(self, app_label: str, model_name: str | None = ..., require_ready: bool = ...) -> ModelType: ...
    def register_model(self, app_label: str, model: type[Model]) -> None: ...
    def is_installed(self, app_name: str) -> bool: ...
    def get_containing_app_config(self, object_name: str) -> AppConfig | None: ...
    def get_registered_model(self, app_label: str, model_name: str) -> type[Model]: ...
    def get_swappable_settings_name(self, to_string: str) -> str | None: ...
    def set_available_apps(self, available: Iterable[str]) -> None: ...
    def unset_available_apps(self) -> None: ...
    def set_installed_apps(self, installed: Iterable[str]) -> None: ...
    def unset_installed_apps(self) -> None: ...
    def clear_cache(self) -> None: ...
    def lazy_model_operation(self, function: Callable, *model_keys: Any) -> None: ...
    def do_pending_operations(self, model: type[Model]) -> None: ...

apps: Apps
