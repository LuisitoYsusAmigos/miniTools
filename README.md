# 🧰 MiniTools

Bienvenido a **MiniTools**, un conjunto de herramientas pequeñas pensadas para resolver tareas poco comunes, pero muy útiles en el día a día.  
Aquí encontrarás scripts simples que te ahorrarán tiempo en procesos repetitivos o específicos.

---

## 📦 Herramientas

### 1. psdExtract

**psdExtract** es una herramienta que permite extraer todas las imágenes contenidas dentro de archivos PSD.

### ⚙️ ¿Qué hace?

- Busca archivos `.psd` dentro de la carpeta `psd/`
- Extrae todas las capas como imágenes
- Guarda los resultados en la carpeta `img/`
- Crea una subcarpeta por cada PSD procesado
- Mantiene el nombre original del archivo
- Exporta en formato **PNG** o **WebP**

### 📁 Estructura

```
/psd        -> Coloca aquí tus archivos PSD
/img        -> Aquí se guardarán las imágenes extraídas
```

### ▶️ Uso básico

1. Coloca tus archivos `.psd` en la carpeta `psd/`
2. Ejecuta el script
3. Revisa la carpeta `img/` para ver los resultados

---

## 🚀 Objetivo del proyecto

Este repositorio busca centralizar pequeñas herramientas que resuelven problemas específicos de forma rápida y sencilla, sin necesidad de configuraciones complejas.