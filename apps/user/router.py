from django.db import connections

class UserRouter:
    """
    A router to control all database operations on models in the
    auth_db application.
    """
    app_name = 'user'

    def db_for_read(self, model, **hints):
        """
        Attempts to read default models go to default database.
        """
        if model._meta.app_label == self.app_name:
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write default models go to default database.
        """
        if model._meta.app_label == self.app_name:
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the default app is involved.
        """
        if obj1._meta.app_label == self.app_name or \
           obj2._meta.app_label == self.app_name:
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the default app only appears in the default database.
        """
        if app_label == self.app_name:
            return db == 'default'
        return None
