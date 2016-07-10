import spur

shell = spur.SshShell(hostname="169.254.130.233", username="pi", password="raspberry",missing_host_key=spur.ssh.MissingHostKey.accept)
result = shell.run(["python3", "blah.py"])
print int(float(result.output))
