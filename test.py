import custom_message

message = custom_message.CustomMessage(
    name="name",
)

data = type(message).to_dict(
    message,
    always_print_fields_with_no_presence=False,
)

print(data)
assert data == {"name": "name"}
