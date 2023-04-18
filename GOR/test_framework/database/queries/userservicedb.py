from typing import Any, Union

from sqlalchemy.exc import ArgumentError

from test_framework.database.db.user_service import UserServiceDB
from test_framework.database.orm.base_config_db import BaseDB
from test_framework.database.orm.usersevicedb import Client, Contacts, Fingerprint, Verification


class QueriesUserService:
    def __init__(self, db: BaseDB = None):
        self.db = db or UserServiceDB()

    def select_all_data_from_table_client(self) -> Union[Client, Any]:
        with self.db.create_session() as session:
            return session.query(Client.id).first()

    def select_verification_code(self, ver_code) -> Union[Verification, Any]:
        with self.db.create_session() as session:
            return session.query(Verification.sms_verification_code).filter(
                Verification.sms_verification_code.ilike(ver_code)
            )

    def select_email_subscription_from_table_contacts_by_client_id(self, client_id) -> Union[Client, Any]:
        with self.db.create_session() as session:
            return session.query(Contacts.email_subscription).filter(Contacts.id_client == client_id)

    def find_fingerprint_by_client_id_from_table_fingerprint(self, client_id):
        with self.db.create_session() as session:
            request = session.query(Fingerprint.fingerprint).filter(Fingerprint.id_client == client_id).first()
            return request

    def delete_fingerprint_by_client_id_from_table_fingerprint(self, fingerprint):
        with self.db.create_session() as session:
            request = session.query(Fingerprint).filter(Fingerprint.fingerprint == fingerprint).first()
            session.delete(request)
            session.commit()
