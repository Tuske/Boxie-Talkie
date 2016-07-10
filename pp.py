import spur

shell = spur.SshShell(hostname="169.254.130.233", username="pi", password="raspberry",missing_host_key=spur.ssh.MissingHostKey.accept)
shell.run(["python3", "pp.py"])
