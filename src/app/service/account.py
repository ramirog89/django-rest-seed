from src.app.models.account import AccountManager

class AccountService:
  accountManager = AccountManager()

  def getAll(self):
    return self.accountManager.getAllAccounts()

  def getSpecificAccount(self):
    return self.accountManager.getAllAccounts()