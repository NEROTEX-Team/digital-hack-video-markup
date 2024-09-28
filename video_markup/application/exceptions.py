class VideoMarkupException(Exception):
    message: str

    def __init__(self, message: str | None = None) -> None:
        self.message = message or "Unknown error"
        super().__init__(message)


class DuplicateObjectException(VideoMarkupException):
    def __init__(self, message: str | None = None) -> None:
        super().__init__(message=message or "Duplicate object")


class EntityNotFoundError(VideoMarkupException):
    def __init__(self, object_id: str, message: str | None = None) -> None:
        super().__init__(message=message or f"Entity {object_id} not found")
