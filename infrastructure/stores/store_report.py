import abc

class DoesNotExist(Exception):
    """Exception to be raised when an entity is not found in storage."""
    pass

class Store(abc.ABC):
    @abc.abstractmethod
    def get_all_reports(self):
        pass

    @abc.abstractmethod
    def get_report_by_id(self, id):
        pass

    @abc.abstractmethod
    def create_report(self, data):
        pass

    @abc.abstractmethod
    def update_report(self, id, data):
        pass

    @abc.abstractmethod
    def delete_report(self, id):
        pass