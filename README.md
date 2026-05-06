# 🔐 SmartWordlist Generator (SWG) – All-in-One Password Profiler

Generador avanzado de wordlists basado en patrones humanos para pruebas de seguridad ofensiva y auditorías de contraseñas.

> ⚠️ **Uso estrictamente educativo y autorizado.**
> Este proyecto está diseñado para **pentesting ético**, laboratorios de ciberseguridad y aprendizaje. El uso indebido puede ser ilegal.

---

## 🚀 Descripción

**SmartWordlist Generator (SWG)** crea un único archivo (`.txt`) con miles (o millones) de posibles contraseñas basadas en información personal, simulando cómo los humanos realmente construyen sus passwords.

A diferencia de generadores básicos, este script:

* Combina múltiples fuentes de datos personales
* Genera variaciones inteligentes (leet, fechas, patrones comunes)
* Produce combinaciones realistas utilizadas en ataques de diccionario avanzados
* Consolida todo en **un solo archivo optimizado**

---

## 🧩 Características

### 📌 Entrada de datos personalizable

Puedes incluir:

* Fecha de nacimiento
* Nombres y apellidos
* Mascotas
* Equipos favoritos
* Familiares
* Años importantes
* Datos adicionales relevantes

---

### 🔄 Generación avanzada

El sistema aplica:

* Variaciones de formato de fechas
* Transformaciones de texto:

  * MAYÚSCULAS / minúsculas
  * Capitalización
  * Texto invertido
* Leetspeak básico (`a → 4`, sufijos comunes, etc.)
* Sufijos frecuentes:

  * `123`, `1234`, `2024`, `2025`, `!`, etc.

---

### 🔗 Combinaciones inteligentes

Incluye:

* Palabras individuales enriquecidas
* Combinaciones de 2 palabras (`nombre+apellido`, etc.)
* Combinaciones de 3 palabras (controladas)
* Mezclas específicas como:

  * `nombre + fecha`
  * `nombre + mascota`
  * `apellido + año`
  * `fecha + equipo`

---

### ⚙️ Control de rendimiento

* Límites internos para evitar explosión combinatoria
* Manejo de errores:

  * Memoria insuficiente
  * Interrupción manual
* Filtrado automático (mínimo 4 caracteres)

---

## 🛠️ Instalación

```bash
git clone https://github.com/tuusuario/smartwordlist-generator.git
cd smartwordlist-generator
```

Requisitos:

* Python 3.8+

---

## ▶️ Uso

```bash
python3 wordlist_generator.py
```

El programa te pedirá datos opcionales. Puedes omitir cualquiera presionando `Enter`.

---

## 📂 Output

* Archivo `.txt` con todas las combinaciones generadas
* Nombre automático basado en cantidad de contraseñas
* Ejemplo:

```
wordlist_completa_250000_pass.txt
```

---

## 📊 Ejemplo de resultados

```
juan123
Juan2025
perez_1990
luna1234
juanperez2024
1990juan
```

---

## ⚠️ Consideraciones legales

Este software está diseñado exclusivamente para:

* Laboratorios educativos
* Auditorías de seguridad autorizadas
* Pruebas en sistemas propios

❌ No debe utilizarse para:

* Acceso no autorizado a sistemas
* Ataques reales sin consentimiento
* Actividades ilegales

El autor no se responsabiliza del mal uso.

---

## 🧪 Casos de uso educativos

* Simulación de ataques de diccionario
* Evaluación de políticas de contraseñas
* Enseñanza de OSINT aplicado a seguridad
* Red Team / Blue Team training

---

## 📉 Limitaciones

* No incluye inteligencia basada en machine learning
* Puede generar archivos muy grandes
* Dependiente de la calidad de los datos ingresados

---

## 🔮 Futuras mejoras

* Exportación en múltiples formatos
* Integración con herramientas como Hashcat


---

## 🤝 Contribuciones

Pull requests y mejoras son bienvenidas.



---

## 👨‍💻 Autor

hori12.86 y rootsite . 

---

## ⭐ Nota final

Las contraseñas humanas siguen patrones predecibles.
Este proyecto demuestra por qué usar:

* Passwords largos
* Gestores de contraseñas
* Autenticación multifactor (MFA)

es fundamental hoy en día.

---
