<template>
  <div>
    <input v-model="id" placeholder="ID Usuario recibido por correo" />
    <button @click="verificar">Verificar</button>
    <p v-if="mensaje">{{ mensaje }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return { id: "", mensaje: "" };
  },
  mounted() {
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('id')) {
      this.id = urlParams.get('id');
    }
  },
  methods: {
    async verificar() {
      if (!this.id) {
        this.mensaje = "Ingrese un ID válido";
        return;
      }
      try {
        const res = await fetch("http://localhost:8000/api/verificar-correo/", {
          method: "POST",
          body: JSON.stringify({ id: this.id }),
          headers: { "Content-Type": "application/json" }
        });
        const data = await res.json();
        this.mensaje = data.mensaje || data.error;
      } catch (error) {
        this.mensaje = "Error de red: " + error.message;
      }
    }
  }
};
</script>
