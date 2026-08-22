# Prédicas — Comunidad Cristiana La Dehesa

> **29 prédicas publicadas** · junio 2025 – agosto 2026

Página web de la biblioteca de prédicas. Un solo archivo, `index.html`, sin
dependencias ni servidor. Los audios viven en Google Drive; la página solo los
enlaza y los reproduce.

---

## 1. Requisito previo: abrir los permisos del Drive

**Sin esto la página se ve pero no suena.** Los audios están privados.

1. Abrir la carpeta **2 - BIBLIOTECA** en Google Drive
2. Clic derecho → **Compartir** → **Compartir**
3. En "Acceso general" cambiar *Restringido* por **Cualquier persona con el enlace**
4. Dejar el rol en **Lector** → **Listo**

Se aplica a toda la carpeta y a los audios que se agreguen después.

---

## 2. Publicar en GitHub Pages

Una sola vez:

1. Crear cuenta en [github.com](https://github.com) (gratis)
2. **New repository**
   - Nombre: `predicas-ccld`
   - Visibilidad: **Public** — obligatorio para que Pages sea gratis
   - No marcar nada más → **Create repository**
3. En el repo vacío: **uploading an existing file** → arrastrar `index.html`
   → **Commit changes**
4. Pestaña **Settings** → menú lateral **Pages**
   - *Source*: **Deploy from a branch**
   - *Branch*: **main** y carpeta **/ (root)** → **Save**
5. Esperar 1–2 minutos y recargar. Arriba aparece la dirección:

```
https://TU-USUARIO.github.io/predicas-ccld/
```

Esa es la dirección para compartir con la congregación.

---

## 3. Agregar una prédica nueva — todo desde github.com, sin instalar nada

No necesitas Git ni la terminal. Se edita en el navegador y GitHub republica solo.

Cada domingo, después de subir el audio a Drive:

1. En Drive, clic derecho sobre el audio → **Compartir** → **Copiar vínculo**.
   El vínculo se ve así:
   `https://drive.google.com/file/d/`**`1AbC...xyz`**`/view?usp=drivesdk`
   El pedazo en negrita es el **ID del archivo**. Cópialo.
2. En GitHub, abrir `index.html` → ícono del **lápiz** (Edit this file)
3. Buscar el bloque `<section class="month">` del mes que corresponda.
   Si el mes no existe todavía, copiar una sección completa y cambiarle el título.
4. Pegar este bloque **arriba de los demás** del mismo mes (van de más nueva a más antigua):

```html
        <li class="item" data-p="NOMBRE DEL PREDICADOR" data-s="nombre del predicador mes ano dd-mm-aaaa">
          <div class="row">
            <div class="day"><span class="n">DD</span><span class="d">Mes</span></div>
            <div class="item-body">
              <h4>NOMBRE DEL PREDICADOR</h4>
              <p class="sub">Prédica del domingo</p>
            </div>
            <button class="play play--ghost" type="button" data-id="ID_DE_DRIVE" aria-expanded="false">
              <svg class="ico-play" width="11" height="13" viewBox="0 0 13 15" aria-hidden="true"><path d="M0 0l13 7.5L0 15z" fill="currentColor"></path></svg>
              <span class="play-label">Escuchar</span>
            </button>
          </div>
          <div class="player" hidden></div>
        </li>
```

Qué cambiar:

| Dónde | Con qué |
|---|---|
| `data-p="…"` | Nombre exacto del predicador (sirve para el filtro) |
| `data-s="…"` | Lo mismo pero **sin tildes y en minúsculas**, más el mes, el año y la fecha. Es lo que usa el buscador |
| `<span class="n">DD</span>` | Día del mes, dos dígitos: `05`, `19` |
| `<span class="d">Mes</span>` | `Ene` `Feb` `Mar` `Abr` `May` `Jun` `Jul` `Ago` `Sep` `Oct` `Nov` `Dic` |
| `<h4>…</h4>` | Nombre del predicador tal como debe verse |
| `<p class="sub">…</p>` | "Prédica del domingo", o el título si lo tiene |
| `data-id="…"` | El ID de Drive del paso 1 |

5. Abajo: **Commit changes**. En un minuto la página ya está actualizada.

### Si quieres mostrar el pasaje bíblico

Agregar esta línea justo después del `<p class="sub">`:

```html
              <span class="passage">Juan 6:1-40</span>
```

### Si el predicador es nuevo

Para que aparezca su botón de filtro, agregar una línea en el bloque `<div class="chips">`:

```html
        <button class="chip" type="button" data-p="Nombre Nuevo" aria-pressed="false">Nombre Nuevo</button>
```

### El ciclo completo, resumido

```
Domingo    → grabas la prédica
           → la subes a Drive, a 2 - BIBLIOTECA / 2026 / 2026-09 septiembre
           → clic derecho → Compartir → Copiar vínculo  (de ahí sacas el ID)
GitHub     → abres index.html → lápiz → pegas el bloque con ese ID
           → Commit changes
1 minuto   → la página ya está actualizada para toda la iglesia
```

### Si algo se rompe

GitHub guarda cada versión. En la pestaña **Commits** (arriba del listado de archivos)
puedes ver todos los cambios y volver a cualquier versión anterior. No se pierde nada.

### Consejo

Haz el primer cambio de prueba un día de semana, no un domingo apurado. Cambia cualquier
cosa mínima —una coma en el texto de bienvenida— y confirma que la página se actualiza.
Así el domingo ya sabes que funciona.

---

## 4. Dominio propio (opcional, más adelante)

Si la iglesia compra un dominio (por ejemplo `predicasccld.cl`), se conecta en
**Settings → Pages → Custom domain**. La página sigue siendo la misma y no cambia
nada del contenido.

---

## Identidad visual

Colores tomados del logo de la iglesia:

| | Hex | Uso |
|---|---|---|
| Verde oliva | `#4D5A2F` | etiquetas de pasaje bíblico |
| Naranja quemado | `#A9551E` | acento, botón activo |
| Granate | `#661E24` | destacados |
| Gris pizarra | `#495459` | filtro seleccionado |

Tipografías: **Archivo** (títulos y datos) y **Source Serif 4** (texto), ambas de
Google Fonts. La página se adapta sola al modo claro u oscuro del teléfono.

---

## Cómo está hecho por dentro

- Un solo archivo, sin frameworks ni build
- El reproductor de cada prédica se crea **solo al tocar "Escuchar"**, así la
  página carga liviana aunque haya cien prédicas
- El buscador ignora tildes: "cristian" encuentra "Cristián"
- Solo un reproductor abierto a la vez

Si prefieres no editar HTML a mano, el archivo `build_site.py` genera el
`index.html` completo desde una lista de prédicas en Python.

---

## Aviso importante sobre los formatos

Al revisar los audios uno por uno se detectó que **casi todos los archivos con extensión
`.mp3` no son mp3**: por dentro son MP4/AAC, solo traían la extensión equivocada. El único
mp3 real del lote es `Felipe Burgos 03` (320 kbps).

Para la página web da lo mismo — el reproductor de Drive los abre igual. **Pero para Spotify
sí importa:** los distribuidores rechazan un archivo cuya extensión no corresponde a su
contenido. Antes de la Fase 3 hay que convertir de verdad a mp3. En Drive ya quedaron con la
extensión `.m4a` corregida, que es lo que realmente son.

## Aviso sobre las fechas

La fecha de grabación de un audio vive dentro del archivo. En los audios exportados de Notas
de Voz el 21 de agosto **esa fecha se sobrescribió con la fecha de exportación**, así que se
perdió y no hay forma de recuperarla desde el archivo.

De todo el lote solo dos conservaban la fecha original, y se recuperaron leyendo el archivo:
`2026-06-14` y `2026-07-05`. Después el usuario confirmó ambas por su cuenta, así que el
método quedó validado.

Quedan **10 audios sin fecha** en `PENDIENTE - falta fecha`. Para esos la única fuente es
**Notas de Voz en el iPhone**, donde cada grabación sigue mostrando su fecha bajo el nombre.
Importante: **anotar la fecha antes de exportar**, porque exportar es justamente lo que la
borra.
