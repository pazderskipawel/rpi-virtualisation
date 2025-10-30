# Dockerized Klipper for Ender V3 SE

This is a containerized version of the [Klipper Guide by Athemis](https://athemis.me/projects/klipper_guide/) project.

## Components

The setup consists of the following containers:

- **Klipper**: The core 3D printer firmware that runs on the host and communicates with the printer. It handles all motion planning and motor control.

- **Moonraker**: An API web server that interfaces with Klipper. It provides a unified interface for managing the 3D printer, handling file management, configuration, and status updates.

- **Fluidd**: A modern web interface for Klipper that provides a user-friendly way to control and monitor your 3D printer. It communicates with Moonraker to provide real-time status updates and control.

- **Traefik**: A reverse proxy that handles routing between the different services, particularly managing the web-based connections between Moonraker and Fluidd.

## Config files used here are combined files from:

- https://github.com/bootuz-dinamon/ender3-v3-se-full-klipper/
- https://github.com/shubham0x13/ender-3-v3-se-klipper
