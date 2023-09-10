#!/bin/bash
trap stop SIGTERM SIGINT SIGQUIT SIGHUP ERR

stop() {
  echo "Stopped"
  exit 0
}

/etc/init.d/xinetd start;
sleep infinity;
