#!/bin/bash

if ! [ "$(ping -c 1 -W 10 google.com)" ]; then
	# Offline
	sudo hwclock -s # Load from RTC
else
	# Online
	date
	sudo hwclock -w # Write to RTC
fi
