from src.app.models.account import AccountManager

class AccountService:
  def getSpecificAccount():
    return AccountManager.getAllAccounts()