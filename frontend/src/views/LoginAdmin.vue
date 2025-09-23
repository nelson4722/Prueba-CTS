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
  data() { return { usuario: "", clave: "", mensaje: "" }; },
  methods: {
    async login() {
      // Ejemplo simple, se debe implementar autenticación real JWT/Session
      if (this.usuario === "admin" && this.clave === "adminpass") {
        this.mensaje = "Login exitoso";
      } else {
        this.mensaje = "Credenciales inválidas";
      }
    }
  }
}
</script>
