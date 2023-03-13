import os
from json import load, dumps

# own
from .abstract_memory import ABCMemory


class JSON(ABCMemory):
    def __init__(self) -> None:
        raise Exception("Not fully implemented yet, use sql instead")
        self.filename = "src/memoryHandle/memory.json"
        if os.path.isfile(self.filename):
            fh = open(self.filename, "r")
            self.file = load(fh)
            fh.close()
        else:
            self.file = {}

    def post_file(self, user_id, file_name, content):
        pass

    def get_file(self, user_id, file_name):
        pass

    def delete_file(self, user_id, file_name):
        pass

    def get_public_and_master_key(self, scheme) -> tuple[str, str]:
        pass

    def get_global_key(self, scheme):
        pass

    def update_pk_msk(self, pk, msk, scheme):
        pass

    def update_gk(self, gk, scheme):
        pass

    def reset_files(self):
        pass

    def set_global_keys(
        self, scheme, pk="placeholder", msk="placeholder", gk="placeholder"
    ):
        self.filename["GlobalValues"].append(
            {"public_key": pk, "master_key": msk, "global_key": gk, "scheme": scheme}
        )

    def close(self):
        fh = open(self.filename, "w")
        fh.write(dumps(self.file))
        fh.close()
