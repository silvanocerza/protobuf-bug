import custom_message

message = custom_message.CustomMessage(
    name="name",
)

chat = custom_message.Chat(messages=[message])

data = type(chat).to_dict(
    chat,
    including_default_value_fields=False,
)

print(data)
assert data == {
    "messages": [
        {
            "name": "name",
        }
    ]
}
