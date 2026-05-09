#include "ESP32_NOW.h"
#include "WiFi.h"
#include <vector>
#include <string.h>

#define CHANNEL 6

// ================= LED RGB (ANODO COMUN) =================
const int pinRojo = 4;
const int pinVerde = 15;
const int pinAzul = 2;

// ================= MENSAJE =================
typedef struct {
  uint8_t id;
  char estado[20];
} mensaje_t;

mensaje_t mensaje;

// ================= ANTI-REBOTE =================
unsigned long ultimoTiempo[5] = {0};
const unsigned long TIEMPO_REBOTE = 500;

// ================= MAPEO =================
char obtenerLetra(uint8_t id) {
  switch (id) {
    case 1: return 'A';
    case 2: return 'B';
    case 3: return 'C';
    case 4: return 'D';
    default: return '?';
  }
}

const char* obtenerColor(uint8_t id) {
  switch (id) {
    case 1: return "AZUL";
    case 2: return "VERDE";
    case 3: return "ROJO";
    case 4: return "AMARILLO";
    default: return "DESCONOCIDO";
  }
}

// ================= CONTROL RGB =================
void setColor(uint8_t id) {
  // Apagar todos primero
  digitalWrite(pinRojo, HIGH);
  digitalWrite(pinVerde, HIGH);
  digitalWrite(pinAzul, HIGH);

  switch (id) {
    case 1: // AZUL
      digitalWrite(pinAzul, LOW);
      break;

    case 2: // VERDE
      digitalWrite(pinVerde, LOW);
      break;

    case 3: // ROJO
      digitalWrite(pinRojo, LOW);
      break;

    case 4: // AMARILLO (rojo + verde)
      digitalWrite(pinRojo, LOW);
      digitalWrite(pinVerde, LOW);
      break;
  }
}

// ================= ESP-NOW =================
class ReceiverPeer : public ESP_NOW_Peer {
public:
  ReceiverPeer(const uint8_t *mac_addr)
  : ESP_NOW_Peer(mac_addr, CHANNEL, WIFI_IF_STA, nullptr) {}

  bool begin() {
    return add();
  }

  void onReceive(const uint8_t *data, size_t len, bool broadcast) override {

    memcpy(&mensaje, data, sizeof(mensaje));

    if (strcmp(mensaje.estado, "mano detectado") != 0) return;

    unsigned long ahora = millis();

    if (mensaje.id < 1 || mensaje.id > 4) return;

    if (ahora - ultimoTiempo[mensaje.id] < TIEMPO_REBOTE) {
      return;
    }

    ultimoTiempo[mensaje.id] = ahora;

    // ===== ACCION RGB =====
    setColor(mensaje.id);

    // ===== SERIAL =====
    char letra = obtenerLetra(mensaje.id);
    const char* color = obtenerColor(mensaje.id);

    Serial.print("Nodo ");
    Serial.print(mensaje.id);
    Serial.print(" (");
    Serial.print(color);
    Serial.print(") -> ");
    Serial.println(letra);
  }
};

// ================= REGISTRO DINÁMICO =================
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

// ================= SETUP =================
void setup() {
  Serial.begin(115200);

  // RGB
  pinMode(pinRojo, OUTPUT);
  pinMode(pinVerde, OUTPUT);
  pinMode(pinAzul, OUTPUT);

  // Apagar todo (ánodo común)
  digitalWrite(pinRojo, HIGH);
  digitalWrite(pinVerde, HIGH);
  digitalWrite(pinAzul, HIGH);

  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  WiFi.setChannel(CHANNEL);

  if (!ESP_NOW.begin()) {
    Serial.println("Error iniciando ESP-NOW");
    while(true);
  }

  ESP_NOW.onNewPeer(register_new_peer, nullptr);

  Serial.println("Receptor listo");
}

// ================= LOOP =================
void loop() {
  delay(200);
}
