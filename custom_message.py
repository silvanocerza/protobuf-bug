from typing import MutableSequence

import proto
from google.protobuf import struct_pb2  # type: ignore

__protobuf__ = proto.module(
    package="custom_package",
    manifest={
        "Chat",
        "CustomMessage",
        "Type",
        "Schema",
    },
)


class Chat(proto.Message):
    messages: MutableSequence["CustomMessage"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="CustomMessage",
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
    parameters: "Schema" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Schema",
    )


class Type(proto.Enum):
    TYPE_UNSPECIFIED = 0
    STRING = 1
    NUMBER = 2
    INTEGER = 3
    BOOLEAN = 4
    ARRAY = 5
    OBJECT = 6


class Schema(proto.Message):
    type_: "Type" = proto.Field(
        proto.ENUM,
        number=1,
        enum="Type",
    )
    format_: str = proto.Field(
        proto.STRING,
        number=7,
    )
    title: str = proto.Field(
        proto.STRING,
        number=24,
    )
    description: str = proto.Field(
        proto.STRING,
        number=8,
    )
    nullable: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    default: struct_pb2.Value = proto.Field(
        proto.MESSAGE,
        number=23,
        message=struct_pb2.Value,
    )
    items: "Schema" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Schema",
    )
    min_items: int = proto.Field(
        proto.INT64,
        number=21,
    )
    max_items: int = proto.Field(
        proto.INT64,
        number=22,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
