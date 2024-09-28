from video_markup.adapters.database.base import Base, IdentifableMixin, TimestampedMixin


class Video(IdentifableMixin, TimestampedMixin, Base):
    __tablename__ = "videos"
