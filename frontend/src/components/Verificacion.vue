<template>
  <div>
    <input v-model="id" placeholder="ID Usuario recibido por correo" />
    <button @click="verificar">Verificar</button>
    <p v-if="mensaje">{{ mensaje }}</p>
  </div>
</template>
<script>
export default {
  data() { return { id: "", mensaje: "" }; },
  methods: {
    async verificar() {
      const res = await fetch("http://localhost:8000/api/verificar-correo/", {
        method: "POST",
        body: JSON.stringify({ id: this.id }),
        headers: { "Content-Type": "application/json" }
      });
      const data = await res.json();
      this.mensaje = data.mensaje || data.error;
    }
  }
}
</script>
