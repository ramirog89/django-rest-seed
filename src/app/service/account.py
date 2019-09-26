from src.app.models.account import AccountManager


class AccountService:
    accountManager = AccountManager()

    def getById(self, pk):
        return self.accountManager.getById(pk=pk)

    def getAll(self):
        return self.accountManager.getAllAccounts()

    def getSpecificAccount(self):
        return self.accountManager.getById(pk=1)
