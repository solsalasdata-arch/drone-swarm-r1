# Deep RL for Autonomous Drone Swarm Path Planning 🚁

Este repositorio contiene el framework desarrollado para mi Trabajo Final de la **Licenciatura en Ciencia de Datos (UCASAL)**. La investigación se centra en la planificación de rutas autónomas y coordinación de enjambres mediante **Deep Reinforcement Learning**.

---

## 📄 Documentación y Recursos
Para entender la base teórica y los resultados, podés consultar:
* 📕 **[Trabajo Final Completo (PDF)](.TRABAJO%20FINAL%20CORRECCIONES%20DICTAMEN%20(1).docx)** * **[Presentación de Defensa (DOCX/PPTX)](./%E2%80%9CAprendizaje%20por%20refuerzo%20profundo%20para%20la%20planificaci%C3%B3n%20aut%C3%B3noma%20de%20rutas%20en%20enjambres%20de%20drones%20un%20marco%20te%C3%B3rico%20y%20experimental%E2%80%9D.pdf)**

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
