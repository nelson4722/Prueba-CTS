<template>
  <form @submit.prevent="registrar">
    <input v-model="nombre" placeholder="Nombre" required />
    <input v-model="email" placeholder="Correo" required />
    <input v-model="telefono" placeholder="Teléfono" required />
    <button type="submit">Registrarse</button>
    <p v-if="mensaje">{{ mensaje }}</p>
  </form>
</template>

<script>
export default {
  data() {
    return {
      nombre: "", email: "", telefono: "", mensaje: "",
    };
  },
  methods: {
    async registrar() {
      const res = await fetch("http://localhost:8000/api/registro/", {
        method: "POST",
        body: JSON.stringify({ username: this.nombre, email: this.email, telefono: this.telefono, password: "123456" }),
        headers: { "Content-Type": "application/json" }
      });
      const data = await res.json();
      this.mensaje = data.mensaje || data.error;
    }
  }
}
</script>
