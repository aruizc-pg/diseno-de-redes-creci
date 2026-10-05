# Diseño y Configuración de Red en Escenario de Nube

En el contexto de operaciones en la nube, es crucial diseñar y configurar redes virtuales que permitan la conectividad y el enrutamiento necesarios para diferentes servicios. El objetivo es crear una red que soporte enrutamiento entre cuentas, configuraciones para escaneo de tráfico y reglas de NAT en un escenario de mediana complejidad.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | diseño de redes |
| **Nivel** | advanced-l2 |
| **Tipo** | practical |
| **Tiempo estimado** | 4-5 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Diseño Inicial de la Red

**Objetivo:** Definir la arquitectura básica de la red incluyendo VPC, segmentos y reglas de enrutamiento.

**Tiempo estimado:** 1 hora

**Instrucciones:**

- Identifica los componentes clave de la red que necesitarás para cumplir con los requisitos del escenario.
- Define la estructura de la VPC incluyendo subredes y segmentos de red.
- Establece las reglas de enrutamiento iniciales para permitir la conectividad básica.

**Entregable:** Diagrama de la red con VPC, subredes y reglas de enrutamiento iniciales.

<details>
<summary>Pistas de conocimiento</summary>

- Considera la segmentación de la red para mejorar la seguridad y el rendimiento.
- Piensa en cómo las reglas de enrutamiento afectarán la conectividad entre diferentes partes de la red.

</details>

### Fase 2: Configuración de Conectividad y Enrutamiento

**Objetivo:** Configurar la conectividad a internet y el enrutamiento entre cuentas.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Configura una puerta de enlace de internet para permitir la conectividad a internet desde tu red.
- Establece las reglas de NAT necesarias para permitir el tráfico saliente.
- Configura el enrutamiento entre cuentas para permitir la comunicación entre diferentes VPCs.

**Entregable:** Configuración de la red con puerta de enlace de internet, reglas de NAT y enrutamiento entre cuentas.

<details>
<summary>Pistas de conocimiento</summary>

- Recuerda que las reglas de NAT son necesarias para permitir el tráfico saliente desde tu red.
- Piensa en cómo el enrutamiento entre cuentas afectará la comunicación entre diferentes servicios.

</details>

### Fase 3: Configuración de Escaneo de Tráfico

**Objetivo:** Configurar el escaneo de tráfico en la VPC para mejorar la seguridad y el monitoreo.

**Tiempo estimado:** 1 hora

**Instrucciones:**

- Configura un servicio de escaneo de tráfico para monitorear el tráfico en tu VPC.
- Establece las reglas necesarias para permitir el escaneo de tráfico sin afectar la conectividad.
- Define los criterios para el escaneo de tráfico, incluyendo qué tipos de tráfico deben ser monitoreados y con qué frecuencia.

**Entregable:** Configuración de escaneo de tráfico en la VPC con reglas y criterios definidos.

<details>
<summary>Pistas de conocimiento</summary>

- Recuerda que el escaneo de tráfico debe ser configurado de manera que no afecte la conectividad de la red.
- Piensa en qué tipos de tráfico son más importantes de monitorear y con qué frecuencia.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es una VPC y por qué es importante en el diseño de redes en la nube?
- **paraQueSirve**: ¿Para qué sirve el escaneo de tráfico en una VPC y cómo puede mejorar la seguridad y el monitoreo?
- **comoSeUsa**: ¿Cómo se usan las reglas de NAT para permitir el tráfico saliente en una red de nube?
- **erroresComunes**: ¿Cuáles son algunos errores comunes al configurar el enrutamiento entre cuentas y cómo pueden ser evitados?
- **queDecisionesImplica**: ¿Qué decisiones implica la configuración de un servicio de escaneo de tráfico en una VPC y cómo pueden afectar la conectividad y el rendimiento de la red?

## Criterios de Evaluacion

- Definir la arquitectura básica de la red incluyendo VPC, segmentos y reglas de enrutamiento.
- Configurar la conectividad a internet y el enrutamiento entre cuentas.
- Configurar el escaneo de tráfico en la VPC con reglas y criterios definidos.

---

*Reto generado automaticamente por Challenge Generator - Pragma*
