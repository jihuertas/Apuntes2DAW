

````md
## 🔑 Generar y usar una clave SSH personalizada para GitHub

1. **Generar la clave SSH con nombre personalizado**  
   Ejecuta en la terminal:

   ```bash
   ssh-keygen -t ed25519 -C "tu_email@ejemplo.com"
````

Cuando pregunte dónde guardar la clave, escribe un nombre personalizado, por ejemplo:

```
Enter file in which to save the key (/home/usuario/.ssh/id_ed25519): /home/usuario/.ssh/id_github
```

Esto generará dos archivos:

* `~/.ssh/id_github` → clave privada (NO compartir).
* `~/.ssh/id_github.pub` → clave pública (esta es la que se copia a GitHub).

---

2. **Añadir la clave privada al `ssh-agent`**
   Activa el agente SSH y añade la clave:

   ```bash
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_github
   ```

---

3. **Copiar la clave pública en GitHub**
   Muestra la clave pública con:

   ```bash
   cat ~/.ssh/id_github.pub
   ```

   Copia el contenido y añádelo en GitHub:

   * Ve a **Settings > SSH and GPG keys > New SSH key**
   * Pega la clave y guarda.

---

4. **Configurar el archivo `~/.ssh/config` (opcional, recomendado si tienes varias claves)**
   Edita el archivo:

   ```bash
   nano ~/.ssh/config
   ```

   Y añade:

   ```
   Host github.com
     HostName github.com
     User git
     IdentityFile ~/.ssh/id_github
   ```

---

5. **Probar la conexión**

   ```bash
   ssh -T git@github.com
   ```

   Si todo está correcto, verás un mensaje como:

   ```
   Hi usuario! You've successfully authenticated, but GitHub does not provide shell access.
   ```

---

✅ Listo, ahora puedes clonar y hacer `git push/pull` con tu clave personalizada.

```

---

¿Quieres que te arme también la **Opción 1 (usar el nombre por defecto `id_ed25519`)** en el mismo estilo para que tengas las dos comparadas en tu documentación?
```
