from ldap3 import Server, Connection, ALL, SUBTREE
from ldap3.core.exceptions import LDAPException, LDAPBindError
 
def global_ldap_authentication(user_name, user_pwd):
    """
      Function: global_ldap_authentication
       Purpose: Make a connection to encrypted LDAP server.
       :params: ** Mandatory Positional Parameters
                1. user_name - LDAP user Name
                2. user_pwd - LDAP User Password
       :return: None
    """
 
    ldap_user_name = user_name.strip()
    ldap_user_pwd = user_pwd.strip()
    tls_configuration = Tls(validate=ssl.CERT_REQUIRED, version=ssl.PROTOCOL_TLSv1_2)
    server = Server('ldap://10.0.0.10:389', use_ssl=True, tls=tls_configuration)
    conn = Connection(server, user=ldap_user_name, password=ldap_user_pwd, authentication=NTLM,
                      auto_referrals=False)
    if not conn.bind():
        print(f" *** Cannot bind to ldap server: {conn.last_error} ")
    else:
        print(f" *** Successful bind to ldap server")
    return

global_ldap_authentication('mflores', 'Mauricio1010')