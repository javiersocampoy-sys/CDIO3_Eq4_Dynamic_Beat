#include "ESP32_NOW.h"
#include "WiFi.h"

#define CHANNEL 6
#define NODE_ID 1   // Cambiar en cada nodo

typedef struct {
  uint8_t id;
  float valor;
} mensaje_t;

mensaje_t mensaje;

class BroadcastPeer : public ESP_NOW_Peer {
public:
  BroadcastPeer(uint8_t channel, wifi_interface_t iface)
  : ESP_NOW_Peer(ESP_NOW.BROADCAST_ADDR, channel, iface, nullptr) {}

  bool begin() {
    if (!ESP_NOW.begin() || !add()) {
      Serial.println("Error iniciando ESP-NOW");
      return false;
    }
    return true;
  }

  bool sendData(uint8_t *data, size_t len) {
    return send(data, len);
  }
};

BroadcastPeer peer(CHANNEL, WIFI_IF_STA);

void setup() {
  Serial.begin(115200);

  WiFi.mode(WIFI_STA);
  WiFi.setChannel(CHANNEL);

  if (!peer.begin()) {
    Serial.println("Fallo crítico");
    while(true);
  }

  Serial.println("Nodo listo");
}

void loop() {

  mensaje.id = NODE_ID;
  mensaje.valor = random(0,100);

  peer.sendData((uint8_t*)&mensaje, sizeof(mensaje));
  Serial.println(mensaje.id);
  Serial.println(mensaje.valor);
  delay(1000);
}