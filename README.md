# Deep RL for Autonomous Drone Swarm Path Planning 🚁

Este repositorio contiene el framework desarrollado para mi Trabajo Final de la **Licenciatura en Ciencia de Datos (UCASAL)**. La investigación se centra en la planificación de rutas autónomas y coordinación de enjambres mediante **Deep Reinforcement Learning**.

---

## 📄 Documentación y Recursos
Para entender la base teórica y los resultados, podés consultar:
* 📕 **[Trabajo Final Completo (PDF)](./Drone_Swarm_DRL_Salas.pdf)** * **[Presentación de Defensa (PDF)](./“Aprendizaje por refuerzo profundo para la planificación autónoma de rutas en enjambres de drones un marco teórico y experimental”.pdf)**

---

## 🚀 Resumen del Proyecto
El objetivo principal fue dotar a un grupo de agentes de la capacidad de aprender a navegar en entornos complejos sin intervención humana, logrando:
* **Tasa de éxito >90%** en misiones de navegación con obstáculos.
* Implementación del algoritmo **PPO** (Proximal Policy Optimization).
* Paradigma **CTDE** (Centralized Training, Decentralized Execution) para escalabilidad.

---

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.10+
* **Frameworks:** Gymnasium, Stable Baselines3.
* **Procesamiento:** NumPy, Pandas.

---

## 💻 Cómo ejecutar el entorno
1. Instalar dependencias: `pip install -r requirements.txt`
2. Ejecutar entrenamiento: `python train.py`
