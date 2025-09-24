<template>
  <div>
    <button @click="generarGanador">Generar ganador</button>
    <p v-if="ganador">{{ ganador }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      ganador: ""
    };
  },
  methods: {
    async generarGanador() {
      try {
        const res = await fetch("http://localhost:8000/api/generar-ganador/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        credentials: "include"  
      });
        const data = await res.json();
        this.ganador = data.ganador ? `${data.ganador} (${data.correo})` : data.error;
      } catch (e) {
        this.ganador = "Error de red o respuesta inesperada";
      }
    }
  }
};
</script>
