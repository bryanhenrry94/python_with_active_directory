import test_ldap
#test_ldap.authenticate('10.0.0.11', 'mflores@edehsa.local', 'Mauricio1010')

from ldap3 import Server, Connection, ALL, SUBTREE
from ldap3.core.exceptions import LDAPException, LDAPBindError
 
# ldap server hostname and port
ldsp_server = f"ldap://10.0.0.10:389"
 
# dn
root_dn = "dc=example,dc=org"
 
# ldap user and password
ldap_user_name = 'mflores@edehsa.local'
ldap_password = 'Mauricio1010'
 
# user
user = f'cn={ldap_user_name},root_dn'

server = Server(ldsp_server, get_info=ALL)
 
connection = Connection(server,
                        user=user,
                        password=ldap_password,
                        auto_bind=True)
 
print(f" *** Response from the ldap bind is \n{connection}" )