#include "ESP32_NOW.h"
#include "WiFi.h"
#include <vector>
#include <string.h>

#define CHANNEL 6
const int ledPin = 2;

typedef struct {
  uint8_t id;
  char estado[20];
} mensaje_t;

mensaje_t mensaje;

volatile bool obstaculoDetectado = false;

class ReceiverPeer : public ESP_NOW_Peer {
public:
  ReceiverPeer(const uint8_t *mac_addr)
  : ESP_NOW_Peer(mac_addr, CHANNEL, WIFI_IF_STA, nullptr) {}

  bool begin() {
    return add();
  }

  void onReceive(const uint8_t *data, size_t len, bool broadcast) override {
    memcpy(&mensaje, data, sizeof(mensaje));

    Serial.print("Nodo: ");
    Serial.print(mensaje.id);
    Serial.print(" | Estado: ");
    Serial.println(mensaje.estado);

    if (strcmp(mensaje.estado, "mano detectado") == 0) {
      obstaculoDetectado = true;
    }
  }
};

std::vector<ReceiverPeer*> peers;

void register_new_peer(const esp_now_recv_info_t *info, const uint8_t *data, int len, void *arg) {
  if (memcmp(info->des_addr, ESP_NOW.BROADCAST_ADDR, 6) == 0) {
    ReceiverPeer *newPeer = new ReceiverPeer(info->src_addr);
    if (newPeer->begin()) {
      peers.push_back(newPeer);
      Serial.println("Nuevo nodo registrado");
    } else {
      Serial.println("Error registrando nodo");
      delete newPeer;
    }
  }
}

void setup() {
  Serial.begin(115200);

  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);

  WiFi.mode(WIFI_STA);
  WiFi.setChannel(CHANNEL);

  if (!ESP_NOW.begin()) {
    Serial.println("Error iniciando ESP-NOW");
    while(true);
  }

  ESP_NOW.onNewPeer(register_new_peer, nullptr);

  Serial.println("Receptor listo");
}

void loop() {
  if (obstaculoDetectado) {
    digitalWrite(ledPin, HIGH);
    delay(1000); 
    digitalWrite(ledPin, LOW);
    
    obstaculoDetectado = false; 
    memset(mensaje.estado, 0, sizeof(mensaje.estado)); 
  }
  
  delay(10); 
}
