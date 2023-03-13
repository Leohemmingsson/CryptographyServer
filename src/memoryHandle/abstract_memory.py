from abc import ABC, abstractmethod


class ABCMemory(ABC):
    @abstractmethod
    def post_file(self, user_id, file_name, content):
        pass

    @abstractmethod
    def get_file(self, user_id, file_name):
        pass

    @abstractmethod
    def delete_file(self, user_id, file_name):
        pass

    @abstractmethod
    def get_public_and_master_key(self, scheme) -> tuple[str, str]:
        pass

    @abstractmethod
    def get_global_key(self, scheme):
        pass

    @abstractmethod
    def update_pk_msk(self, pk, msk, scheme):
        pass

    @abstractmethod
    def update_gk(self, gk, scheme):
        pass

    @abstractmethod
    def reset_files(self):
        pass

    @abstractmethod
    def set_global_keys(self, pk, msk, gk, scheme):
        pass

    @abstractmethod
    def close(self):
        pass
