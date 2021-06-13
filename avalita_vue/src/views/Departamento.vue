<template>
  <div class="page-departamento">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">{{ departamento.name }}</h2>
      </div>

      <p v-for="disciplina in departamento.disciplinas" :key="disciplina.id">
        {{ disciplina }}
      </p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Departamento",
  data() {
    return {
      departamento: {},
    };
  },
  mounted() {
    this.getDepartamento();
  },
  watch: {
    $route(to, from) {
      if (to.name === "Departamento") {
        this.getDepartamento();
      }
    },
  },
  methods: {
    async getDepartamento() {
      this.$store.commit("setIsLoading", true);
      const departamento_slug = this.$route.params.departamento_slug;
      await axios
        .get(`/api/v1/dpto/${departamento_slug}`)
        .then((response) => {
          this.departamento = response.data;
          document.title = this.departamento.name + " | Avalita";
        })
        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>