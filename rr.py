import spur
def rr():
    shell = spur.SshShell(hostname="169.254.130.233", username="pi", password="raspberry",missing_host_key=spur.ssh.MissingHostKey.accept)
    result = shell.spawn(["python3", "rr.py"])

