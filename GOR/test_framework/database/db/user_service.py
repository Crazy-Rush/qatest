from test_framework.database.orm.base_config_db import BaseDB


class UserServiceDB(BaseDB):
    user = "gor_qa"
    password = "GoRQa123"
    host = "172.17.1.19"
    database = "userservice-dev"
