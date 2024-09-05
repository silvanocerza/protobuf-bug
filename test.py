import custom_message

message = custom_message.CustomMessage(
    name="name",
    description="description",
    parameters=custom_message.Schema(
        type_=custom_message.Type.STRING,
        format_="format",
        title="title",
    ),
)

chat = custom_message.Chat(messages=[message])

data = type(chat).to_dict(
    chat,
    including_default_value_fields=False,
    use_integers_for_enums=False,
)

print(data)
assert data == {
    "messages": [
        {
            "name": "name",
            "description": "description",
            "parameters": {"type_": "STRING", "format_": "format", "title": "title"},
        }
    ]
}
