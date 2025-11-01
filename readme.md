# ⚡ Decentralized Power Tracker

## 🌍 Why Decentralized?
Decentralization ensures transparency, accountability, and trust in power distribution monitoring.
- **Tamper-proof data:** No single authority can alter or hide information.
- **Public transparency:** Citizens can monitor the government’s performance and track how effectively power stations handle complaints.
- **Trust-building:** Data immutability ensures fair handling of outages and complaints.

---

## ⚙️ Implementation & Scaling

The system can be deployed in **three stages** to balance cost and scalability:

### 1. Transformer-Level Installation
- Installed at **local distribution transformers** or feeder pillars (serving 20–100 houses).
- Ideal for **city-wide pilot projects**.

### 2. Street/Cluster-Level Installation
- Deployed at **street-level distribution points** serving 10–20 homes.
- Offers localized monitoring for smaller areas.

### 3. Per-House Installation
- Placed **inside or near smart meters / main breakers**.
- Enables fine-grained tracking at the household level.

---

## 🧠 Tech Stack

### **Frontend**
- **Framework:** Nuxt / Vue
- **Mapping:** Leaflet.js
- **Government UI:**
  - Authenticated panel for officials
  - Resolve/unresolve complaints
  - Record action audit trail (who, when, notes)

### **Backend**
- **Framework:** Python FastAPI
- **Database:** MongoDB

#### **Blockchain & Data Integrity**
1. Every 15–30 minutes, backend collects data:
   ```
   (house_id, power_status, timestamp)
   ```
2. Each record is **hashed (SHA-256)**.
3. **Merkle Tree** built from all hashes → compute **Merkle Root**.
4. Upload full JSON batch to **IPFS** → get **CID**.
5. Push to **Ethereum Smart Contract**, storing:
   - Merkle Root
   - Area ID
   - IPFS link
   - Timestamp

🔍 To verify a record:
Retrieve the IPFS JSON → verify hash inclusion using Merkle proof.

---

## 📡 IoT Setup

Each IoT device reports:
```
latitude
longitude
power_status (ON/OFF)
timestamp
device_signature
```

### Suggested Hardware
- **NB-IoT Module:** SIM7020E
- **Network Example:** Bharti Airtel NB-IoT + Secure Meters (used for 1.3M smart meters in Bihar)

---

## 🔒 IoT Security & Anti-Tampering

### **Hardware Security**
- Use boards with **TPM or Secure Element chips** (e.g., ESP32 + ATECC608A).

### **Secure Boot**
- Device boots only **signed firmware**.
- Prevents flashing of malicious code.
- Encrypt all firmware and communication.

### **Secure Network**
- Use **TLS (HTTPS/MQTT over SSL)** or **DTLS** for constrained networks.
- Prevents packet interception or modification.

---

## 🧩 Summary

| Component | Technology | Purpose |
|------------|-------------|----------|
| Frontend | Nuxt/Vue + Leaflet | Map & Admin UI |
| Backend | FastAPI + MongoDB | API & Data Management |
| Blockchain | Ethereum + IPFS | Immutable Audit Trail |
| IoT | SIM7020E / ESP32 | Power Status Detection |
| Security | TPM, Secure Boot, TLS | Anti-Tampering & Data Protection |

---

## 🪄 Vision
To create a **transparent, tamper-proof, and community-accessible power monitoring system** — enabling citizens to trust the data they see and governments to act with accountability.