from serum import inject, dependency

from src.app.persistence.repositories.account import AccountRepository
from src.app.service.serializer.account import AccountDTO


@dependency
class AccountService:
    @inject
    def __init__(self, account_repo: AccountRepository):
        self.account_repo = account_repo

    def get_by_id(self, pk):
        return self.account_repo.get_by_id(pk=pk)

    def get_all(self):
        return self.account_repo.get_accounts()

    def create(self, entity):
        created_account = self.account_repo.save(entity.data)
        return AccountDTO(created_account).data

    def update(self, entity, pk):
        updated_account = self.account_repo.update(entity.data, pk)
        return AccountDTO(updated_account).data

    def delete(self, pk):
        self.account_repo.delete(pk)