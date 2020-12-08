# Fritzbox Agent

This is a small agent, publishing network traffic information to a [Drogue IoT](https://drogue.io) instance.

## Installing

* Create a systemd unit (`/etc/systemd/system/fritzbox-agent.service`):

  ~~~ini
  [Unit]
  Description=Fritzbox Agent
  
  [Service]
  Restart=on-failure
  ExecStartPre=/usr/bin/rm -f /%t/%n-pid /%t/%n-cid
  ExecStart=/usr/bin/podman run --conmon-pidfile /%t/%n-pid --cidfile /%t/%n-cid -e PASSWORD=fritzbox-password -e DEVICE_ID=box2 -e ENDPOINT_USER=box2 -e ENDPOINT_PASSWORD=boxy123456 -e ENDPOINT=https://http-endpoint-drogue-iot.apps.wonderful.iot-playground.org -d localhost/fritzbox-agent:latest
  ExecStop=/usr/bin/sh -c "/usr/bin/podman rm -f `cat /%t/%n-cid`"
  KillMode=none
  Type=forking
  PIDFile=/%t/%n-pid
  
  [Install]
  WantedBy=multi-user.target
  ~~~

  Be sure to replace the environment variables:

    * `PASSWORD` – The password of the Fritzbox
    * `DEVICE_ID` – Device ID in Drogue Cloud
    * `ENDPOINT` – HTTP endpoint in Drogue Cloud
    * `ENDPOINT_USER` – User part of the device credentials
    * `ENDPOINT_PASSWORD` – Password part of the device credentials

* Reload the daemon:

  ~~~shell
  sudo systemctl daemon-reload
  ~~~

* Activate the unit

  ~~~shell
  sudo systemctl enable --now fritzbox-agent.service
  ~~~