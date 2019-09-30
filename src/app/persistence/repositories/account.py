from serum import dependency
from src.app.persistence.models import AccountModel


@dependency
class AccountRepository:

    def get_by_id(self, pk):
        return AccountModel.objects.get(pk=pk)

    def get_accounts(self):
        return AccountModel.objects.values()

    def save(self, account_entity):
        return AccountModel.objects.create(name=account_entity['name'],
                                           email=account_entity['email'])

    def update(self, account_entity, pk):
        account = AccountModel.objects.get(id=pk)
        account.name = account_entity['name']
        account.email = account_entity['email']
        account.save()
        return account

    def delete(self, pk):
        account = AccountModel.objects.get(id=pk)
        account.delete()