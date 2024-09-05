# Protobuf serialization bug

This is repo reproduces an issue with `protobuf` and `proto-plus`.

This bug appears only on Windows.

To reproduce the issue:

1. `pip install bad_requirements.py`
2. `python test.py`

`good_requirements.txt` contains requirements that do not cause the issue when calling `python test.py`.
