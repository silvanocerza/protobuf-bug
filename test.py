import custom_message

message = custom_message.CustomMessage(
    name="name",
)

data = type(message).to_dict(
    message,
    including_default_value_fields=False,
)

print(data)
assert data == {"name": "name"}
