from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def run_ftp_server():
    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "password", "C:/ftp_directory", perm="elradfmw")  # Set FTP credentials and directory
    authorizer.add_anonymous("C:/ftp_directory", perm="elr")  # Allow anonymous read-only access

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer(("0.0.0.0", 21), handler)  # Host on port 21
    server.serve_forever()

if __name__ == "__main__":
    run_ftp_server()

