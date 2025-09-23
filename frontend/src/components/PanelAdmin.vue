<template>
  <div>
    <button @click="generarGanador">Generar ganador</button>
    <p v-if="ganador">{{ ganador }}</p>
  </div>
</template>
<script>
export default {
  data() { return { ganador: "" }; },
  methods: {
    async generarGanador() {
      const res = await fetch("http://localhost:8000/api/generar-ganador/", { method: "POST" });
      const data = await res.json();
      this.ganador = `${data.ganador ? data.ganador + " (" + data.correo + ")" : data.error}`;
    }
  }
}
</script>
