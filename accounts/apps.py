from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'


    def ready(self):
        '''
        Import signals into the apps
        '''
        import accounts.signals
