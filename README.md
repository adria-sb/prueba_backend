# Project Name

A brief description of your project, its purpose, and what it does.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/prueba_backend.git
    ```
2. Navigate to the project directory:
    ```bash
    cd prueba_backend
    ```
3. Install dependencies:
    ```bash
    npm install
    ```

## Usage

1. Start the development server:
    ```bash
    npm run dev
    ```
2. Open your browser and navigate to `http://localhost:3000`.

## Endpoints

### 1. **GET** `/battery/status`

Devuelve el estado actual de la batería.

**Respuesta:**
```json
{
  "chargePercent": 75,
  "maxCapacity": 10,
  "lastUpdated": "2025-04-25T14:10:00.000Z"
}
```

---

### 2. **POST** `/battery/charge`

Carga la batería con una cantidad específica en kWh.

**Body:**
```json
{
  "amount": 3.5
}
```

**Errores posibles:**
- Si `amount` excede la capacidad máxima.
- Si el `amount` es inválido (negativo, no numérico).

---

### 3. **POST** `/battery/discharge`

Descarga energía de la batería.

**Body:**
```json
{
  "amount": 2.0
}
```

**Errores posibles:**
- Si `amount` es mayor a la carga actual.
- Si el `amount` es inválido.

---

### 4. **GET** `/battery/history`

Devuelve los últimos 20 eventos de carga o descarga.

**Respuesta:**
```json
[
  {
    "type": "charge",
    "amount": 1.5,
    "timestamp": "2025-04-25T14:10:00.000Z"
  },
  {
    "type": "discharge",
    "amount": 0.5,
    "timestamp": "2025-04-25T14:15:00.000Z"
  }
]
```
