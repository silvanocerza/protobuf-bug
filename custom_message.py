import proto

__protobuf__ = proto.module(
    package="custom_package",
    manifest={
        "CustomMessage",
    },
)


class CustomMessage(proto.Message):
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
