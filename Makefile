usage:
	@echo "Omega Playground"

shell:
	picocom --baud 115200 /dev/ttyUSB0

ssh:
	ssh -oHostKeyAlgorithms=+ssh-rsa -oPubkeyAcceptedAlgorithms=+ssh-rsa root@$(OMEGA_ADDR)
