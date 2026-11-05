# Tarea: revisión de los Objetivos 2 y 3 (correcciones, verificaciones, explicaciones y glosario)

Creada: 2026-11-04 · Rama: `feat/results-obj3` · Punto de partida: commit `52a357b`

**Criterio general.** La carrera entrega un producto de software: pesan más la construcción del software y la aplicación de las metodologías y técnicas que el rigor metodológico. La hipótesis del TGA se mantiene, pero breve. En la tesis se escribe solo «implementado», nunca «implantado», y no se dice de quién es la cuenta de Meta.

**Repos para verificar** (en `../bellidental-app/`): `bellidental-backend` (Spring Boot, `src/`, `docs/`, `deploy/`), `bellidental-agent` (Python, `app/`, `tests/`, `docs/`), `bellidental-frontend` (Angular) y `schema.dbml`.

**Productos de la tarea**
1. Las ediciones en los `.tex` (bloques B y F).
2. `tareas/RESPUESTAS-REVISION.md`: respuesta a cada duda, con la evidencia del repo (archivo:línea) y el veredicto (cierto, falso o matizar).
3. `tareas/GLOSARIO-TECNOLOGIAS.md`: el glosario (bloque E). Opcional: publicarlo como página.
4. Dos diagramas sencillos de apoyo, solo para el autor: recursos del servidor compartido, y recorrido del webhook por HTTPS.
5. Compilar (`latexmk`, el log está en `Build/main.log`) y hacer commit al final.

**Estado (2026-11-05): ejecutada.** Respuestas en `tareas/RESPUESTAS-REVISION.md`; glosario en `tareas/GLOSARIO-TECNOLOGIAS.md`.

Orden de ejecución: A → C (verificar antes de editar) → B → F → D/E → compilar.

---

## A. Revisar las correcciones propias del autor

- [x] A1. `git diff 52a357b -- tex/` sobre las supresiones del autor (frases, oraciones, párrafos).
- [x] A2. Por cada supresión, comprobar:
  - referencias rotas (`\ref`, `\cite`, tablas o figuras huérfanas o citadas sin existir);
  - coherencia de la cadena PC → BN → RF → diseño → tarjeta → verificación;
  - que no quede ningún RF o requerimiento sin justificación ni ninguna figura sin texto que la cite.
- [x] A3. Informar en tres grupos: «sin impacto», «impacto menor (propuesta)» y «rompe integridad (propuesta obligatoria)». No revertir nada sin consultar.

## B. Ediciones solicitadas

### Objetivo 2
- [x] B1. `ob2/intro-impulsores.tex:5`: reescribir «La Tabla 34 traza cada evidencia del análisis hasta el requerimiento…» en un tono menos técnico.
- [x] B2. `ob2/metodologia.tex:5`: la cita de RAD (`martin1991rapid`) existe y se resuelve en la compilación actual. Confirmar en `Build/main.pdf`. El [?] venía de un PDF antiguo.
- [x] B3. `ob2/metodologia.tex:33`: después de «Scrum supone… XP… cliente en sitio», añadir brevemente que la clínica está en otra ciudad, a una hora en autobús, lo que impide un cliente en sitio permanente. Solo si refuerza el argumento, y en una frase.
- [x] B4. `ob2/proceso-tobe.tex:3`: quitar «del Objetivo 1» y dejar solo «(Figuras 9, 10 y 11)».
- [x] B5. `ob2/tecnologias.tex:100` (motor de BD): matizar «única alternativa con una restricción de exclusión nativa» según la verificación C1.
- [x] B6. `ob2/tecnologias-agente.tex:37`: «diseño guiado por atributos». Ver C2. Si no tiene respaldo bibliográfico, reescribirlo como «según los atributos de calidad priorizados» o citar la fuente (Bass, Clements y Kazman, *Software Architecture in Practice*: ADD, *Attribute-Driven Design*).
- [x] B7. `ob2/tecnologias-agente.tex:62` (Santhosh): la cita existe. Confirmar que se resuelve; si no, eliminar la mención.
- [x] B8. `ob2/tecnologias-agente.tex:64`: «frases de ejemplo etiquetadas por intención». Explicarlo en RESPUESTAS; si el enfoque descartado no lo necesita, simplificar la frase.
- [x] B9. `ob2/tecnologias-agente.tex:102`: cita de Jurafsky. Confirmar que se resuelve.
- [x] B10. Tabla de motores conversacionales (`ob2/tecnologias-agente.tex` ≈113–124):
  - explicar qué compara (motores o enfoques de diálogo, no modelos de lenguaje) y por qué aparece «Módulo dentro de la API»;
  - si la categoría confunde, renombrarla o aclararla en una línea;
  - explicar el criterio «Consumo de recursos en el servidor compartido» con un diagrama de apoyo (D-diagrama 1).
- [x] B11. `ob2/arquitectura-general.tex:144`: eliminar «los cambios de la agenda… se publican como eventos que programan los recordatorios». Recomendación previa: quitar del Objetivo 2 las menciones operativas a recordatorios, botones y plantillas, y conservar RF14 en la tabla de requerimientos y en el plan como «Debería». Inventario con `grep -rn -i "recordatorio\|plantilla\|botones"`.
- [x] B12. `ob2/tecnologias-agente.tex:27` y `ob2/arquitectura-agente.tex:188`: quitar la fila «Mensajes interactivos» (listas y botones) si no se implementó. Verificar en C9 si las listas del menú sí existen; en ese caso, dejar solo las listas.
- [x] B13. `ob2/arquitectura-agente.tex:190`: ventana de 24 h. Verificar (C10) y ajustar.
- [x] B14. `ob2/modelo-datos.tex:32`: quitar la entidad «Recordatorio» de la tabla de entidades principales, o marcarla según B11. Revisar también el anexo (`appointment_reminders`) y `Ob3_ER_Cobros_Agente`.
- [x] B15. `ob2/modelo-datos.tex:41`: valores calculados (saldo, edad, CPO y ceo). Verificar (C11) y explicar cómo se calculan.
- [x] B16. `ob2/modelo-datos.tex:85`: explicar «vinculada a la original» (C12) y, si hace falta, aclararlo en el texto.
- [x] B17. `ob2/despliegue.tex:3`: ampliar la introducción «El sistema y el agente comparten una única infraestructura» (dos o tres líneas: un servidor, contenedores, proxy, dominio y subdominios).
- [x] B18. `ob2/despliegue.tex:39`: quitar «las plantillas de mensaje aprobadas por Meta». Explicar el webhook por HTTPS (D-diagrama 2).
- [x] B19. `ob2/plan-desarrollo.tex:5`: redactar el boceto sin tono de posibilidad («posible distribución» → distribución de las tarjetas).
- [x] B20. `ob2/plan-desarrollo.tex:14`: quitar la mención de las tarjetas en negrita y la negrita de la tabla `tab:ob2_tarjetas`.

### Objetivo 3
- [x] B21. `ob3/intro.tex`: quitar el comentario de la primera línea y dejar el texto más limpio. Revisar si sobra la enumeración de apartados.
- [x] B22. `ob3/diseno-usuario.tex`: redactar 3.3.1 como wireframes con colores y distribución, una versión menos elaborada de los mismos elementos de las pantallas finales.
- [x] B23. `ob3/base-tecnica.tex:6`: mejorar «La construcción (Tabla 36) empezó con la tarjeta 0 del plan (Tabla 56)…».
- [x] B24. Reducir las menciones de «tarjeta 0» en el Objetivo 3 a donde sean necesarias (`grep -rn "tarjeta 0"`). Incluye `base-tecnica.tex:111` («La tarjeta 0 dejó listo el entorno de pruebas…»).
- [x] B25. `ob3/base-tecnica.tex:111`: verificar Testcontainers (C13) y ajustar. Lo mismo en `ob2/tecnologias.tex:122`.
- [x] B26. CIE-10: comprobar que esté definido la primera vez que aparece (sigla desarrollada y qué es, en el marco teórico o en el Obj. 1). Si no lo está, añadir una definición breve en la primera aparición.
- [x] B27. `ob3/tarjetas.tex:77`: «queda inmutable» (receta emitida). Verificar (C14) y ajustar.
- [x] B28. `ob3/agente-desarrollo.tex:128`: renombrar «Reglas y dónde se aplican» con un título formal, por ejemplo «Ubicación de las reglas de negocio por capa».
- [x] B29. `ob3/agente-desarrollo.tex:130`: quitar el tono justificativo («la capa que puede garantizarla») y lo coloquial («lo que vale para todos los canales» → «aplica a ambos canales»).
- [x] B30. Tabla de reglas del agente (`ob3/agente-desarrollo.tex` ≈145–161): verificar fila por fila (C15–C19). Corregir o eliminar lo que no esté en el código y aclarar el límite de citas (agente frente a recepción).
- [x] B31. `ob3/agente-desarrollo.tex:35/157`: urgencia. Explicar el flujo y ajustarlo según C18.
- [x] B32. `ob3/agente-desarrollo.tex:167`: «los dos mensajes anteriores, ya enmascarados». Explicarlo con un ejemplo y verificarlo (C20).
- [x] B33. `ob3/agente-desarrollo.tex:201`: aclarar «cuando la conversación está libre» (fuera de un flujo guiado) en el texto.
- [x] B34. `ob3/agente-desarrollo.tex:212`: «webhook y firma». Explicar la firma HMAC de Meta (C21) y, si conviene, precisarlo en el texto.
- [x] B35. `ob3/whatsapp.tex:23–24`: explicar cómo se configuró el webhook (verificación por *challenge*, suscripción a `messages`, firma) y el token permanente de usuario del sistema (C22). Ajustar la redacción si algo no coincide.

## C. Verificaciones en los repos (cierto / falso / matizar)

Para cada una: archivo y línea del repo, el veredicto y la acción en la tesis.

- [x] C1. ¿PostgreSQL es el único motor con restricción de exclusión nativa? Comparado con MySQL, MariaDB y SQL Server. ¿Cómo funciona `EXCLUDE USING gist` con `btree_gist`? Es una restricción declarativa del esquema, no un procedimiento ni un *trigger*. Ubicar la migración de Flyway que la crea.
- [x] C2. ¿«Diseño guiado por atributos» viene de algún antecedente o de la bibliografía? Buscar en los `.bib` y en las fichas.
- [x] C3. Uso de `pg_trgm` e índices GIN: tablas, columnas y consultas (CIE-10, medicamentos, pacientes).
- [x] C4. Bloqueo de la interfaz interna de la API desde internet (`ob2/arquitectura-agente.tex:41`, `arquitectura-general.tex:65`): ¿Caddyfile con rutas bloqueadas, red interna de Docker o *token* interno? Revisar `deploy/` y el Caddyfile.
- [x] C5. ¿Por qué agente y API se comunican por HTTP sin TLS dentro del servidor? Red interna de Docker, sin exposición pública y con autenticación interna. Verificar en `docker-compose`.
- [x] C6. Regla anticruce para ambos canales (`ob2/arquitectura-agente.tex:52`): confirmar que recepción y agente escriben por la misma API y la misma tabla, y que el conflicto devuelve 409.
- [x] C7. `ob2/arquitectura-agente.tex:161`: ¿la identificación solo se pide para agendar o reprogramar? ¿El estado se guarda en memoria y caduca a los 30 min? ¿Qué pasa con un reinicio? Lo mismo en `ob3/agente-desarrollo.tex:107`.
- [x] C8. `ob2/arquitectura-agente.tex:153` y `ob3/agente-desarrollo.tex:155`: ¿reprogramar o cancelar hasta 2 h antes?
- [x] C9. ¿El menú usa listas interactivas o botones de WhatsApp?
- [x] C10. Ventana de servicio de 24 h de WhatsApp y plantillas fuera de ella (política de Meta). ¿El agente la maneja en el código?
- [x] C11. ¿Saldo, edad e índices CPO/ceo se calculan y no se almacenan? ¿Dónde y con qué fórmula?
- [x] C12. Reprogramación: ¿hay una FK de la cita nueva a la original (p. ej. `rescheduled_from_id`) y la original pasa a `RESCHEDULED`?
- [x] C13. ¿Hay pruebas con Testcontainers (PostgreSQL real en contenedor) para la agenda? ¿Qué clases?
- [x] C14. ¿La receta emitida es inmutable (sin endpoint de edición, validación de estado o restricción)?
- [x] C15. Enmascarado de secuencias de 7 o más dígitos ante el modelo, y la cédula fuera del historial: ubicar la función en el agente.
- [x] C16. Límite de citas activas: una por paciente y especialidad, y hasta tres por teléfono, solo para las del agente. ¿Dónde se aplica y qué significa «las de recepción no cuentan»?
- [x] C17. Plazos de 8 s para el modelo y 10 s para la API, con menú o derivación al vencer: ubicar la configuración.
- [x] C18. Urgencia: detección (intención o palabras clave), los tres primeros horarios de hoy o mañana y el texto fijo de emergencia.
- [x] C19. Cualquier otra fila de la tabla de reglas que no aparezca en el código.
- [x] C20. Contexto enviado al modelo: ¿mensaje actual más los dos anteriores, enmascarados? Preparar un ejemplo.
- [x] C21. Validación de la firma `X-Hub-Signature-256` (HMAC-SHA256 con el secreto de la aplicación) y respuesta 200 inmediata con deduplicación por id de mensaje. ¿Es política de Meta (reintentos) o decisión propia? Documentar ambas.
- [x] C22. Token permanente de usuario del sistema (Meta Business), guardado solo en el servidor (variables de entorno o secretos).
- [x] C23. fail2ban en el VPS: si está instalado, la *jail* de sshd y dónde se configuró.
- [x] C24. httpx y Uvicorn en el agente: cómo se usan (cliente asíncrono con *timeout*, servidor ASGI de FastAPI).
- [x] C25. JJWT y Hibernate Envers en el backend: dónde se usan (emisión y validación de *tokens*; auditoría `@Audited` con tablas `*_aud`). Contrastar con el anexo, que dice «implementación posterior».
- [x] C26. Angular CDK en el frontend: qué componentes usa (overlay, drag & drop, a11y…).

## D. Explicaciones para el autor (no van a la tesis)

Se responden en `tareas/RESPUESTAS-REVISION.md`, en lenguaje sencillo y cada una con la evidencia de C:

- Política anticruce: qué es, cómo funciona y la restricción `appointments_no_overlap`, desglosada línea por línea.
- Diseño guiado por atributos (ADD), con una o dos referencias para leer.
- Frases de ejemplo etiquetadas por intención (clasificador tradicional frente a LLM).
- Qué compara la tabla de motores conversacionales y qué significa «Módulo dentro de la API».
- Consumo de recursos en el servidor compartido → **diagrama 1** (contenedores sobre un VPS de 4 vCPU y 8 GB).
- HTTPS, certificado TLS, Let's Encrypt y ACME: por qué Meta lo exige, cómo lo obtiene y renueva Caddy, y cómo se llama la operación (*handshake* TLS y desafío ACME) → **diagrama 2** (Meta → DNS → Caddy :443 → agente).
- Cómo se bloquea la interfaz interna, por qué se usa HTTP interno y cómo la regla vale para los dos canales.
- Por qué se responde 200 al webhook y qué es la firma.
- Índices de trigramas.
- Ejemplo de los mensajes enmascarados.
- «Conversación libre» frente a flujo guiado.
- fail2ban, webhook, token de Meta, httpx, Uvicorn, JJWT, Envers y Angular CDK.

## E. Glosario de tecnologías (`tareas/GLOSARIO-TECNOLOGIAS.md`)

Por término: qué es, para qué se usó en Bellidental, dónde está en el repo y por qué se eligió (una o dos líneas cada uno). Agrupado:

- **Base de datos:** PostgreSQL, restricción EXCLUDE, GiST y `btree_gist`, `pg_trgm` (trigramas), índices GIN, `tstzrange`, Flyway (migraciones).
- **API:** Spring Boot, monolito modular, JWT y JJWT, Spring Security, Hibernate/JPA, Hibernate Envers, Testcontainers, JUnit.
- **Interfaz:** Angular, Angular CDK, SPA, nginx.
- **Agente:** Python, FastAPI, Uvicorn (ASGI), httpx, máquina de estados, LLM con salida estructurada, intención y *slots*, enmascaramiento, idempotencia y deduplicación.
- **WhatsApp:** WhatsApp Cloud API, Graph API, webhook, verificación por *challenge*, firma HMAC `X-Hub-Signature-256`, ventana de 24 h, plantillas, mensajes interactivos, token de usuario del sistema.
- **Infraestructura:** VPS, Docker, Docker Compose, red interna, GHCR, GitHub Actions (CI/CD), DNS y Cloudflare, subdominios, Caddy (proxy inverso), HTTPS y TLS, Let's Encrypt y ACME, SSH con llaves, fail2ban, cortafuegos (UFW, si aplica).
- **Dominio clínico:** CIE-10, Formulario 033, odontograma, índices CPO y ceo.

Incluir solo lo que se confirme en los repos; si algo no está, se omite o se marca.

## F. Ocultar la sección de verificación

- [x] F1. Comentar `\input{tex/ResultsAndDiscussion/ob3/verificacion}` en `results-ob3.tex`. El contenido se discutirá al final de los resultados.
- [x] F2. Resolver las referencias que dependían de ella: `tab:ob3_verificacion`, `tab:ob3_brechas`, `fig:ob3_tablero` y las referencias a RNF06 en la evaluación. Hacer `grep` y reubicar o quitar cada una.
- [x] F3. Decidir con el autor si el tablero Kanban final (`fig:ob3_tablero`) pasa a otra sección o se omite.

## Decisiones del autor (2026-11-04)

- B3: sí, se menciona brevemente la distancia (una hora en autobús).
- B11/B14: se adopta la recomendación: quitar del Objetivo 2 las menciones operativas a recordatorios (eventos, entidad, botones, plantillas) y mantener RF14 como «Debería» en los requerimientos y en el plan.
- F3: pendiente. Recomendación: mover la figura del tablero final al cierre de 3.3, después de las tarjetas, si se toma la captura de Planka; si no, omitirla.
