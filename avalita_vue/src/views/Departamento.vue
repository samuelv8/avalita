<template>
  <div class="page-departamento">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">{{ departamento.name }}</h2>
      </div>

      <ul v-if="departamento.disciplinas.length">
        <li v-for="disciplina in departamento.disciplinas" :key="disciplina.id">
          <router-link :to="disciplina.get_absolute_url">
            <strong>
              {{
                get_disciplina_slug_from_url(
                  disciplina.get_absolute_url
                ).toUpperCase()
              }}
            </strong>
            - {{ disciplina.name }}
          </router-link>
        </li>
      </ul>
      <p v-else>Não há disciplinas desse departamento.</p>
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
    get_disciplina_slug_from_url(url) {
      const arr = url.split("/");
      const slug = arr[arr.length - 1];
      return slug;
    },
  },
};
</script>