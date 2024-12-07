# Proyecto Juegos Florales - Pruebas Móviles

[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17295804)

## **Descripción General**
Este proyecto tiene como objetivo garantizar la calidad del aplicativo móvil "Juegos Florales", desarrollado para la Universidad Privada de Tacna. Las pruebas móviles realizadas abarcan funcionalidad, compatibilidad y rendimiento en dispositivos Android, utilizando herramientas como **Appium**, **Selenium**, **BrowserStack**, y generando reportes detallados con **Allure**.

El enfoque principal se centra en validar las funcionalidades críticas del sistema, automatizando las pruebas y optimizando los tiempos y recursos utilizados, alineándose con los estándares de calidad requeridos por la universidad.

---

## **Objetivos**
- **Validar** la funcionalidad y compatibilidad del aplicativo en múltiples dispositivos Android.
- **Automatizar** las pruebas móviles mediante herramientas modernas, reduciendo tiempos y errores.
- **Generar reportes detallados** con métricas clave y visualizaciones para análisis posterior.
- **Garantizar** la experiencia de usuario óptima en términos de usabilidad y rendimiento.

---

## **Requerimientos Funcionales**
| ID   | Descripción                                      | Prioridad |
|------|--------------------------------------------------|-----------|
| RF01 | Validación de inicio de sesión segura           | Alta      |
| RF02 | Pruebas automatizadas para la interacción       | Media     |
| RF03 | Validación de campos de texto                   | Alta      |
| RF04 | Generación de reportes detallados de ejecución  | Alta      |

---

## **Requerimientos No Funcionales**
| ID    | Descripción                                         | Prioridad |
|-------|-----------------------------------------------------|-----------|
| RNF01 | Seguridad en los datos utilizados en las pruebas    | Alta      |
| RNF02 | Ejecución de pruebas en menos de 2 minutos          | Alta      |
| RNF03 | Disponibilidad continua del sistema (99%)           | Alta      |
| RNF04 | Interoperabilidad con múltiples dispositivos Android | Alta      |

---

## **Herramientas Utilizadas**
1. **Appium**: Automatización de pruebas móviles.
2. **Selenium**: Automatización de pruebas web y móviles.
3. **BrowserStack**: Plataforma para pruebas en múltiples dispositivos y versiones.
4. **Allure**: Generación de reportes visuales detallados.

---

## **Arquitectura del Proyecto**
### **Modelo 4+1**
- **Vista Lógica**: Organización de subsistemas y paquetes.
- **Vista de Implementación**: Despliegue de herramientas para pruebas.
- **Vista de Procesos**: Validación de funcionalidades críticas.
- **Vista Física**: Uso de dispositivos físicos y emuladores.
- **Vista de Casos de Uso**: Interacciones entre usuarios y el sistema.

---

## **Diagramas del Proyecto**

### **Diagrama de Casos de Uso**
![Diagrama de Casos de Uso](path/to/use_case_diagram.png)

### **Diagrama de Secuencia**
![Diagrama de Secuencia](path/to/sequence_diagram.png)

### **Diagrama de Colaboración**
![Diagrama de Colaboración](path/to/collaboration_diagram.png)

### **Diagrama de Objetos**
![Diagrama de Objetos](path/to/object_diagram.png)

### **Diagrama de Clases**
![Diagrama de Clases](path/to/class_diagram.png)

### **Diagrama de Paquetes**
![Diagrama de Paquetes](path/to/package_diagram.png)

---

## **Estructura del Proyecto**
```plaintext
proyecto/
│
├── tests/
│   ├── test_login.py
│   ├── test_buttons.py
│   ├── test_fields.py
│   └── test_reports.py
│
├── utils/
│   ├── driver_setup.py
│   ├── des_capabilities.py
│   └── report_generator.py
│
├── requirements.txt
├── README.md
├── setup.cfg
└── setup.py
