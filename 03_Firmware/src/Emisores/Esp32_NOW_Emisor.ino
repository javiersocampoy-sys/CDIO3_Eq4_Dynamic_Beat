#include "ESP32_NOW.h"
#include "WiFi.h"
#include <Arduino.h>
#include <U8g2lib.h>
#include <Wire.h>

// Configuración de pantalla para tu modelo (Pines 6 y 5)
U8G2_SSD1306_72X40_ER_F_HW_I2C u8g2(U8G2_R0, /* reset=*/ U8X8_PIN_NONE, /* clock=*/ 6, /* data=*/ 5);

#define CHANNEL 6
#define NODE_ID 1 

const int echoPin = 1; 
const int trigPin = 2; 

typedef struct {
  uint8_t id;
  char estado[20];
} mensaje_t;

mensaje_t mensaje;

class BroadcastPeer : public ESP_NOW_Peer {
public:
  BroadcastPeer(uint8_t channel, wifi_interface_t iface)
  : ESP_NOW_Peer(ESP_NOW.BROADCAST_ADDR, channel, iface, nullptr) {}

  bool begin() {
    if (!ESP_NOW.begin() || !add()) return false;
    return true;
  }

  bool sendData(uint8_t *data, size_t len) {
    return send(data, len);
  }
};

BroadcastPeer peer(CHANNEL, WIFI_IF_STA);

void setup() {
  Serial.begin(115200);
  u8g2.begin();

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  WiFi.mode(WIFI_STA);
  WiFi.setChannel(CHANNEL);

  if (!peer.begin()) {
    while(true) {
        Serial.println("Error ESP-NOW");
        delay(1000);
    }
  }
}

void loop() {
  // Medir distancia
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duracion = pulseIn(echoPin, HIGH);
  float distancia = duracion * 0.034 / 2;

  // Mostrar en pantalla
  u8g2.clearBuffer();
  u8g2.drawFrame(0, 0, 72, 40); 
  u8g2.setFont(u8g2_font_6x10_tf);
  u8g2.drawStr(5, 12, "DISTANCIA:");
  
  u8g2.setCursor(15, 30);
  if (distancia > 400 || distancia < 2) {
    u8g2.print("--- cm");
  } else {
    u8g2.print(distancia, 1);
    u8g2.print(" cm");
  }
  u8g2.sendBuffer();

  // Envío si hay obstáculo
  if (distancia > 0 && distancia < 15.0) {
    mensaje.id = NODE_ID;
    strcpy(mensaje.estado, "mano detectado"); 
    peer.sendData((uint8_t*)&mensaje, sizeof(mensaje));
    delay(500); 
  }

  delay(100);
}
