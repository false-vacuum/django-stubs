from typing import Any, Dict, List, Optional, Sequence, Set, Tuple, TypeVar, Union

from django.db.models.manager import Manager

from django.core.checks.messages import CheckMessage

class ModelBase(type): ...

_Self = TypeVar("_Self", bound="Model")

class Model(metaclass=ModelBase):
    class DoesNotExist(Exception): ...
    class MultipleObjectsReturned(Exception): ...
    class Meta: ...
    _meta: Any
    _default_manager: Manager[Model]
    pk: Any = ...
    def __init__(self: _Self, *args, **kwargs) -> None: ...
    def delete(self, using: Any = ..., keep_parents: bool = ...) -> Tuple[int, Dict[str, int]]: ...
    def full_clean(self, exclude: Optional[List[str]] = ..., validate_unique: bool = ...) -> None: ...
    def clean(self) -> None: ...
    def clean_fields(self, exclude: List[str] = ...) -> None: ...
    def validate_unique(self, exclude: List[str] = ...) -> None: ...
    def save(
        self,
        force_insert: bool = ...,
        force_update: bool = ...,
        using: Optional[str] = ...,
        update_fields: Optional[Union[Sequence[str], str]] = ...,
    ) -> None: ...
    def save_base(
        self,
        raw: bool = ...,
        force_insert: bool = ...,
        force_update: bool = ...,
        using: Optional[str] = ...,
        update_fields: Optional[Union[Sequence[str], str]] = ...,
    ): ...
    def refresh_from_db(self: _Self, using: Optional[str] = ..., fields: Optional[List[str]] = ...) -> _Self: ...
    def get_deferred_fields(self) -> Set[str]: ...
    @classmethod
    def check(cls, **kwargs: Any) -> List[CheckMessage]: ...
    def __getstate__(self) -> dict: ...

class ModelStateFieldsCacheDescriptor: ...

class ModelState:
    db: None = ...
    adding: bool = ...
    fields_cache: ModelStateFieldsCacheDescriptor = ...
