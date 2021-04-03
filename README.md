## Aim

This lab is meant to get students more accustomed to the technologies used in designing and implementing an embedded module as part of an IoT system and RESTful API server.

## Requirements

### Client

For the final part of the system you're meant to build, you'll have to send status updates from each tank's location. You'll have to design a circuit that consists of an atmega based microcontroller (eg. Atmega328p) and an ESP8266 WiFi module.

Your goal is to continuously send POST requests to your server from the embedded circuit. 

Your POST request should send a JSON object as payload.