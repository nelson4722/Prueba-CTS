<template>
  <div>
    <h2>Login Administrador</h2>
    <input v-model="usuario" placeholder="Usuario" />
    <input v-model="clave" type="password" placeholder="Contraseña" />
    <button @click="login">Ingresar</button>
    <p v-if="mensaje">{{ mensaje }}</p>
  </div>
</template>

<script>
export default {
  data() { 
    return { 
      usuario: "", 
      clave: "", 
      mensaje: "" 
    }; 
  },
  methods: {
    async login() {
      try {
        const res = await fetch("http://localhost:8000/api/login/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          credentials: "include",  // para manejar cookies/sesión
          body: JSON.stringify({
            username: this.usuario,
            password: this.clave
          })
        });

        if (res.ok) {
          this.mensaje = "Login exitoso";
          this.$router.push('/paneladmin');
        } else {
          this.mensaje = "Credenciales inválidas";
        }
      } catch (error) {
        this.mensaje = "Error de red: " + error.message;
      }
    }

  }
}
</script>
